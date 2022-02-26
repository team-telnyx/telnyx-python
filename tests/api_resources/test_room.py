import telnyx
import pytest

TEST_RESOURCE_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"


class TestRoom(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Room.list()
        request_mock.assert_requested("get", "/v2/rooms")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.Room.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/rooms/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Room)

    def test_is_creatable(self, request_mock):
        telnyx.Room.create()
        request_mock.assert_requested("post", "/v2/rooms")

    def test_is_modifiable(self, request_mock):
        resource = telnyx.Room.modify(
            TEST_RESOURCE_ID,
            enable_recording=False,
            max_participants=20,
        )
        request_mock.assert_requested(
            "patch", "/v2/rooms/%s" % TEST_RESOURCE_ID
        )

    @pytest.mark.skip(reason="204 Response (silent)")
    def test_is_deletable(self, request_mock):
        resource = telnyx.Room.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/rooms/%s" % TEST_RESOURCE_ID
        )

    @pytest.mark.skip(reason="Nest List")
    def test_can_list_sessions(self, request_mock):
        resource = telnyx.Room.retrieve(TEST_RESOURCE_ID)
        resource.list_sessions()

    def test_can_generate_token(self, request_mock):
        resource = telnyx.Room.retrieve(TEST_RESOURCE_ID)
        resource.create_generate_token(id=TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v2/rooms/%s/actions/generate_join_client_token" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.Room)

    @pytest.mark.skip(reason="Needs token")
    def test_can_refresh_token(self, request_mock):
        resource = telnyx.Room.retrieve(TEST_RESOURCE_ID)
        resource.create_refresh_token(id="TEST_RESOURCE_ID")
        request_mock.assert_requested(
            "post", "/v2/rooms/%s/actions/refresh_client_token" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.Room)
