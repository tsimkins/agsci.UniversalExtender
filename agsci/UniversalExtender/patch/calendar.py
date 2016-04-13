from cStringIO import StringIO

from DateTime import DateTime

from Products.ATContentTypes.lib.calendarsupport import ICS_EVENT_START, ICS_EVENT_END, rfc2445dt, vformat, foldLine

def getICal(self):
    """get iCal data
    """
    out = StringIO()
    map = {
        'dtstamp': rfc2445dt(DateTime()),
        'created': rfc2445dt(DateTime(self.CreationDate())),
        'uid': self.UID(),
        'modified': rfc2445dt(DateTime(self.ModificationDate())),
        'summary': vformat(self.Title()),
        'startdate': rfc2445dt(self.start()),
        'enddate': rfc2445dt(self.end()),
        }
    out.write(ICS_EVENT_START % map)

    description = self.Description()
    if description:
        out.write(foldLine('DESCRIPTION:%s\n' % vformat(description)))

    location = self.getLocation()
    if location:
        map_link = getattr(self, 'map_link', None)

        if map_link:
            out.write('LOCATION:%s ( %s )\n' % (vformat(location), map_link))
        else:
            out.write('LOCATION:%s\n' % vformat(location))

    subject = self.Subject()
    if subject:
        out.write('CATEGORIES:%s\n' % ', '.join(subject))

    # TODO  -- NO! see the RFC; ORGANIZER field is not to be used for non-group-scheduled entities
    #ORGANIZER;CN=%(name):MAILTO=%(email)
    #ATTENDEE;CN=%(name);ROLE=REQ-PARTICIPANT:mailto:%(email)

    cn = []
    contact = self.contact_name()
    if contact:
        cn.append(contact)
    phone = self.contact_phone()
    if phone:
        cn.append(phone)
    email = self.contact_email()
    if email:
        cn.append(email)
    if cn:
        out.write('CONTACT:%s\n' % vformat(', '.join(cn)))

    url = self.event_url()
    if url:
        out.write('URL:%s\n' % url)

    out.write(ICS_EVENT_END)
    return out.getvalue()

