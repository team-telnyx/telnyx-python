from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import DeletableAPIResource, ListableAPIResource


class RoomRecording(DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "room_recording"
