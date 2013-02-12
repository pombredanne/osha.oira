from five import grok
from Products.CMFCore.utils import getToolByName
from euphorie.deployment.browser.sitemenu import EuphorieSitemenu
from osha.oira import _
from osha.oira.interfaces import IOSHAContentSkinLayer
from plonetheme.nuplone import MessageFactory as nu_

class OiraSitemenu(EuphorieSitemenu):
    grok.layer(IOSHAContentSkinLayer)

    def organise(self):
        menu = super(OiraSitemenu, self).organise()
        if menu is not None:
            children = menu["children"]
        else:
            menu = {"title": nu_("menu_organise", default=u"Organise")}
            children = menu["children"] = []

        urltool = getToolByName(self.context, 'portal_url')
        portal_url = urltool.getPortalObject().absolute_url()

        children.append(
                {"title": _("menu_statistics", default=u"Statistics"),
                 "url": "%s/@@show-statistics" % portal_url})

        if children:
            return menu
        else:
            return None
