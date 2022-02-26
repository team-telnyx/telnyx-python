import telnyx

TEST_RESOURCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestRoomParticipant(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.RoomParticipant.list()
        request_mock.assert_requested("get", "/v2/room_participants")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.RoomParticipant)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.RoomParticipant.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/room_participants/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.RoomParticipant)
