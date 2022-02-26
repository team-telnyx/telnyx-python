from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "sessions", path="sessions", operations=["list", "retrieve"]
)
@nested_resource_class_methods(
    "generate_token", path="actions/generate_join_client_token", operations=["create"]
)
@nested_resource_class_methods(
    "refresh_token", path="actions/refresh_client_token", operations=["create"]
)
class Room(
    CreateableAPIResource,
    ListableAPIResource,
    DeletableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "room"

    def list_sessions(self, **params):
        return Room.list_sessions(self.name, **params)

    def generate_token(self, **params):
        return Room.create_generate_token(self.id, **params)

    def refresh_token(self, **params):
        return Room.create_refresh_token(self.id, **params)
