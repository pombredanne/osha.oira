# -*- coding: utf-8 -*-

import logging
from AccessControl import Unauthorized
from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from zope.interface import Interface
from datetime import datetime
from five import grok

from euphorie.content.sectorcontainer import ISectorContainer
from euphorie.content.sector import ISector

from z3c.saconfig import Session
from zope.sqlalchemy import datamanager
import transaction

import urllib2

logger = logging.getLogger("osha.oira/browser.statistics")

class WriteStatistics(grok.View):

    grok.context(IPloneSiteRoot)
    grok.require('cmf.ManagePortal')
    grok.name('write-statistics')

    def _walk(self, root, published=False):
        info_surveys = []
        for country in root.objectValues():
            for sector in country.objectValues():
                for survey_or_group in sector.objectValues():
                    if survey_or_group.portal_type == 'euphorie.survey':
                        surveys = [survey_or_group]
                        survey_parent_path = '/'.join((country.id, sector.id))
                    elif survey_or_group.portal_type == 'euphorie.surveygroup':
                        surveys = survey_or_group.objectValues()
                        survey_parent_path = '/'.join((country.id, sector.id, survey_or_group.id))
                    else:
                        surveys = [] # redundant right now, but in case sth is added below...
                        logger.info('Object is neither survey nor surveygroup, skipping. %s' % '/'.join(survey_or_group.getPhysicalPath()))
                        continue
                    for survey in surveys:
                        survey_path = '/'.join((survey_parent_path, survey.id))
                        if not survey.portal_type == 'euphorie.survey':
                            logger.info('Object is not a survey but inside surveygroup, skipping. %s' % '/'.join(survey.getPhysicalPath()))
                            continue
                        published_date = None
                        if published:
                            if isinstance(survey.published, datetime):
                                published_date = survey.published
                            elif isinstance(survey.published, tuple):
                                published_date = survey.published[2]
                        info_surveys.append((survey_path, survey.Language(),
                            published, published_date, survey.created()))

        return info_surveys

    def render(self):
        urltool = getToolByName(self.context, 'portal_url')
        dbtable_surveys = 'statistics_surveys'

        portal = urltool.getPortalObject()
        # published surveys under /client
        info_surveys_client = self._walk(portal['client'], published=True)
        # unpublished surveys under /sectors
        info_surveys_sectors = self._walk(portal['sectors'], published=False)

        info_surveys = info_surveys_client + info_surveys_sectors

        # write to db
        session = Session()
        session.execute('''DELETE FROM %s;''' % dbtable_surveys)
        def clean(value):
            if isinstance(value, basestring):
                return safe_unicode(value).strip().encode('utf-8')
            return value
        def pg_format(value):
            if value is None:
                return 'NULL'
            if isinstance(value, datetime):
                return "TIMESTAMP '%s'" % value.isoformat()
            return "'%s'" % value
        for line in info_surveys:
            insert = '''INSERT INTO %s VALUES %s;''' % \
                     (dbtable_surveys, '(%s)' % ', '.join(map(pg_format,
                         map(clean,line))))
            session.execute(insert)
        datamanager.mark_changed(session)
        transaction.get().commit()

        from pprint import pformat
        return "Written:\n" + pformat(info_surveys)


class ShowStatistics(grok.View):

    grok.context(Interface)
    grok.name('show-statistics')
    grok.require('zope2.View')

    filename = { 'overview': 'usage_statistics_overview.rptdesign',
                 'country': 'usage_statistics_country.rptdesign',
                 'tool': 'usage_statistics_tool.rptdesign',
               }
    report_path = 'statistics'

    def update(self):
        if ISectorContainer.providedBy(self.context):
            self.report_type = 'overview'
        elif ISectorContainer.providedBy(aq_parent(self.context)):
            self.report_type = 'country'
        elif ISector.providedBy(self.context):
            self.report_type = 'tool'
            sector = self.context.getId()
            country = aq_parent(self.context).getId()
            self.tools = []
            urltool = getToolByName(self.context, 'portal_url')
            portal = urltool.getPortalObject()
            client = portal.get('client')
            def fail():
                self.report_type = None
                return
            country_ob = client.get(country)
            if not country_ob:
                fail()
            sector_ob = country_ob.get(sector)
            if not sector_ob:
                fail()
            for survey_or_group in sector_ob.objectValues():
                if survey_or_group.portal_type == 'euphorie.survey':
                    self.tools.append('/'.join(survey_or_group.getPhysicalPath()[-3:]))
                elif survey_or_group.portal_type == 'euphorie.surveygroup':
                    self.tools.extend(['/'.join(survey.getPhysicalPath()[-4:])
                        for survey in survey_or_group.objectValues()])
        else:
            self.report_type = None
        self.years = range(datetime.now().year, 2010, -1)

    def render(self):
        pm = getToolByName(self.context, 'portal_membership')
        if pm.isAnonymousUser():
            raise Unauthorized, 'must be logged in to view statistics'
        
        report_type = self.report_type
        if report_type is None:
            IStatusMessage(self.request).addStatusMessage(
                    "No statistics available for this context",
                    type=u'error')
            return self.request.response.redirect(self.context.absolute_url())

        if not 'submit' in self.request.form:
            template = ViewPageTemplateFile('templates/statistics.pt')
            return template(self)

        ptool = getToolByName(self.context, 'portal_properties')
        site_properties = ptool.site_properties
        url = site_properties.getProperty('birt_report_url')
        # birt_report_url should look something like this:
        # http://localhost:8080/birt-viewer/frameset?__format=pdf&__pageoverflow=0&__asattachment=true&__overwrite=false

        if not url:
            IStatusMessage(self.request).addStatusMessage(
                    "birt_report_url not set, please contact an administrator",
                    type=u'error')
            return self.request.response.redirect(self.context.absolute_url())

        filename = self.filename[report_type]
        url = "&".join([url, '__report=%s/%s' % (self.report_path, filename)])

        if report_type == 'country':
            url = "&".join([url, 'country=%s' % self.context.getId()])
        elif report_type == 'tool':
            url = "&".join([url, 'tool=%s' % self.request.get('tool')])
        elif report_type == 'overview':
            url = "&".join([url, 'sector=%25'])

        year = self.request.get('year')
        month = 0
        quarter = 0
        if self.request.get('date_method') == 'month':
            month = self.request.get('month')
        elif self.request.get('date_method') == 'quarter':
            quarter = self.request.get('quarter')

        url = "&".join([url, 'year=%d' % year, 'month=%d' % month, 'quarter=%d' %
            quarter])

        try:
            page = urllib2.urlopen(url)
        except urllib2.URLError:
            IStatusMessage(self.request).addStatusMessage(
                    "Statistics server could not be contacted, please try again later",
                    type=u'error')
            return self.request.response.redirect(self.context.absolute_url())
        self.context.REQUEST.response.setHeader('content-type', page.headers.get('content-type') or 'application/pdf')
        self.context.REQUEST.response.setHeader('content-disposition', page.headers.get('content-disposition') or 'inline; filename="report.pdf"')
        return page.read()
        
        
