from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class RoomComposition(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "room_composition"
