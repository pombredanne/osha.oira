from zope.interface import Interface
from euphorie.client import interfaces

class IProductLayer(Interface):
    """ Marker interface for requests indicating the osha.oira
        package has been installed.
    """

class IOSHAClientSkinLayer(interfaces.IClientSkinLayer):
    """Marker interface for the OSHA client skin."""

class IOSHAIdentificationPhaseSkinLayer(interfaces.IIdentificationPhaseSkinLayer):
    """Skin layer used during the identification phase."""

class IOSHAReportPhaseSkinLayer(interfaces.IReportPhaseSkinLayer):
    """Skin layer used during the action plan report phase."""

class IOSHAEvaluationPhaseSkinLayer(interfaces.IEvaluationPhaseSkinLayer):
    """Skin layer used during the evaluation phase."""

class IOSHAActionPlanPhaseSkinLayer(interfaces.IActionPlanPhaseSkinLayer):
    """Skin layer used during the action plan phase."""