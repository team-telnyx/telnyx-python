from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    APIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("mute", path="actions/mute", operations=["create"])
@nested_resource_class_methods("unmute", path="actions/unmute", operations=["create"])
@nested_resource_class_methods("kick", path="actions/kick", operations=["create"])
@nested_resource_class_methods(
    "participants", path="participants", operations=["list", "retrieve"]
)
class RoomSession(ListableAPIResource):
    OBJECT_NAME = "room_session"

    def mute(self, **params):
        return RoomSession.create_mute(self.id, **params)

    def unmute(self, **params):
        return RoomSession.create_unmute(self.id, **params)

    def kick(self, **params):
        return RoomSession.create_kick(self.id, **params)

    def list_participants(self, **params):
        return RoomSession.list_participants(self.name, **params)


class RoomSessionList(APIResource):
    OBJECT_NAME = "room_session_list"
