import pytest

import telnyx

TEST_RESOURCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestRoomSessions(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.RoomSession.list()
        request_mock.assert_requested("get", "/v2/room_sessions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.RoomSession)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.RoomSession.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/room_sessions/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.RoomSession)

    def test_can_call_create_mute(self, request_mock):
        resource = telnyx.RoomSession.retrieve(TEST_RESOURCE_ID)
        resource.create_mute(id=TEST_RESOURCE_ID, particpants="all")
        request_mock.assert_requested(
            "post", "/v2/room_sessions/%s/actions/mute" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.RoomSession)

    def test_can_call_create_unmute(self, request_mock):
        resource = telnyx.RoomSession.retrieve(TEST_RESOURCE_ID)
        resource.create_unmute(id=TEST_RESOURCE_ID, particpants="all")
        request_mock.assert_requested(
            "post", "/v2/room_sessions/%s/actions/unmute" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.RoomSession)

    def test_can_call_kick(self, request_mock):
        resource = telnyx.RoomSession.retrieve(TEST_RESOURCE_ID)
        resource.create_kick(id=TEST_RESOURCE_ID, particpants="all")
        request_mock.assert_requested(
            "post", "/v2/room_sessions/%s/actions/kick" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.RoomSession)

    @pytest.mark.skip(reason="Participant list ")
    def test_can_list_participants(self, request_mock):
        resource = telnyx.RoomSession.retrieve(TEST_RESOURCE_ID)
        resource.active = True
        participants = resource.list_participants()
        request_mock.assert_requested(
            "get", "/v2/room_sessions/%s/participants" % resource.name
        )
        assert isinstance(participants.data[0], telnyx.RoomSession)
