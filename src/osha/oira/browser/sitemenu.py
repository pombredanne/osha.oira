from Acquisition import aq_inner, aq_parent
from five import grok
from euphorie.content.sectorcontainer import ISectorContainer
from euphorie.content.sector import ISector
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

        context = aq_inner(self.context)
        context_url = context.absolute_url()
        if ISectorContainer.providedBy(context) or \
           ISectorContainer.providedBy(aq_parent(context)) or \
           ISector.providedBy(self.context):
            children.append(
                    {"title": _("title_statistics", default=u"Statistics Reporting"),
                     "url": "%s/@@show-statistics" % context_url})

        if children:
            return menu
        else:
            return None
