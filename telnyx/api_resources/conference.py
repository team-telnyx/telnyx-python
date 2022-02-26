from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("join", path="actions/join", operations=["create"])
@nested_resource_class_methods("mute", path="actions/mute", operations=["create"])
@nested_resource_class_methods("unmute", path="actions/unmute", operations=["create"])
@nested_resource_class_methods("hold", path="actions/hold", operations=["create"])
@nested_resource_class_methods("unhold", path="actions/unhold", operations=["create"])
@nested_resource_class_methods("speak", path="actions/speak", operations=["create"])
@nested_resource_class_methods("play", path="actions/play", operations=["create"])
@nested_resource_class_methods("stop", path="actions/stop", operations=["create"])
@nested_resource_class_methods(
    "record_start", path="actions/record_start", operations=["create"]
)
@nested_resource_class_methods(
    "record_stop", path="actions/record_stop", operations=["create"]
)
@nested_resource_class_methods("update", path="actions/update", operations=["create"])
@nested_resource_class_methods("leave", path="actions/leave", operations=["create"])
@nested_resource_class_methods(
    "dial_participant", path="actions/dial_participant", operations=["create"]
)
@nested_resource_class_methods("participants", path="participants", operations=["list"])
class Conference(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "conference"

    def join(self, **params):
        return Conference.create_join(self.id, **params)

    def dial_participant(self, **params):
        return Conference.create_dial_participant(self.id, **params)

    def mute(self, **params):
        return Conference.create_mute(self.id, **params)

    def unmute(self, **params):
        return Conference.create_unmute(self.id, **params)

    def hold(self, **params):
        return Conference.create_hold(self.id, **params)

    def unhold(self, **params):
        return Conference.create_unhold(self.id, **params)

    def speak(self, **params):
        return Conference.create_speak(self.id, **params)

    def play(self, **params):
        return Conference.create_play(self.call_control_id, **params)

    def stop(self, **params):
        return Conference.create_stop(self.call_control_id, **params)

    def record_start(self, **params):
        return Conference.create_record_start(self.id, **params)

    def record_stop(self, **params):
        return Conference.create_record_stop(self.id, **params)

    def update(self, **params):
        return Conference.create_update(self.id, **params)

    def leave(self, **params):
        return Conference.create_leave(self.id, **params)

    def participants(self, **params):
        return Conference.create_participants(self.name, **params)
