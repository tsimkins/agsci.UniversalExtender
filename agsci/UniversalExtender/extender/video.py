from ..interfaces import IVideoPage, IVideoPlaylist
from archetypes.schemaextender.interfaces import ISchemaExtender, ISchemaModifier, IBrowserLayerAwareExtender
from . import BaseExtender, _ExtensionStringField, _ExtensionBooleanField, _ExtensionTextField, _ExtensionLinesField, _ExtensionDateTimeField, _ExtensionReferenceField, _ExtensionBlobField, _ExtensionIntegerField
from Products.Archetypes.public import StringField, StringWidget, BooleanField, BooleanWidget, TextField, RichWidget, LinesField, LinesWidget, InAndOutWidget, DateTimeField, CalendarWidget, ReferenceField, FileWidget, IntegerField, IntegerWidget, SelectionWidget
from zope.component import adapts
from zope.interface import implements

class VideoPageExtender(BaseExtender):
    adapts(IVideoPage)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    fields = [
        _ExtensionStringField(
            "media_id",
            required=False,
            widget=StringWidget(
                label=u"Limelight Media Id",
                description=u"",
                condition="python:member.has_role('Manager', object) or member.has_role('Video Editor', object)",
            ),
        ),
        _ExtensionStringField(
            "player_format",
            default="",
            required=False,
            schemata="settings",
            widget=StringWidget(
                label=u"Player Format",
                description=u"Leave blank for default",
                condition="python:member.has_role('Manager', object)",
            ),
        ),
    ]


class VideoPlaylistExtender(BaseExtender):
    adapts(IVideoPlaylist)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    fields = [
        _ExtensionStringField(
            "playlist_id",
            required=False,
            widget=StringWidget(
                label=u"Limelight Playlist Id",
                description=u"",
                condition="python:member.has_role('Manager', object) or member.has_role('Video Editor', object)",
            ),
        ),
        _ExtensionStringField(
            "player_format",
            default="",
            required=False,
            schemata="settings",
            widget=StringWidget(
                label=u"Player Format",
                description=u"Leave blank for default",
                condition="python:member.has_role('Manager', object)",
            ),
        ),
    ]