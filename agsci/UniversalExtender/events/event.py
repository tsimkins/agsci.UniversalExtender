from Acquisition import aq_parent, aq_inner

from Products.CMFCore.utils import getToolByName
from Products.membrane.interfaces import IMembraneUserObject
from agsci.UniversalExtender import UniversalExtenderMessageFactory as _
from Products.agCommon import ploneify

def setShortName(event):
    """
    Stolen from Products.FacultyStaffDirectory.events.person
    """

    context = event.context

    parent = context.getParentNode()
    
    new_id = ploneify(context.Title())
    
    if new_id != context.getId():
        if new_id in parent.objectIds():
            datestamp = context.start().strftime('%Y%m%d')
            datetimestamp = context.start().strftime('%Y%m%d%H%M')
            if not "%s-%s" % (new_id, datestamp) in parent.objectIds():
                new_id = "%s-%s" % (new_id, datestamp)
            elif not "%s-%s" % (new_id, datetimestamp) in parent.objectIds():
                new_id = "%s-%s" % (new_id, datetimestamp)
            else:
                # giving up!  But someday, we'll work the location into the mix.
                return
    
        context.setId(new_id)
        catalog = getToolByName(context, 'portal_catalog')
        catalog.reindexObject(context)
