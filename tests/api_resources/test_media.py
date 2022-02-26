from __future__ import absolute_import, division, print_function

import telnyx
import pytest

TEST_RESOURCE_ID = "1293384261075731499"


class TestMedia(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Media.list()
        request_mock.assert_requested("get", "/v2/media")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.Media.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/media/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.Media)

    def test_is_creatable(self, request_mock):
        resource = telnyx.Media.create(
            media_url="http://www.example.com/audio.mp3",
        )
        request_mock.assert_requested("post", "/v2/media")

    @pytest.mark.skip(reason="Request body /w object")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.Media.putify(
            TEST_RESOURCE_ID,
        )
        request_mock.assert_requested(
            "put", "/v2/media/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.Media)

    @pytest.mark.skip(reason="Invalid Url")
    def test_is_deletable(self, request_mock):
        resource = telnyx.Media.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/media/%s" % TEST_RESOURCE_ID
        )

    @pytest.mark.skip(reason="Nested download")
    def test_can_download(self, request_mock):
        resource = telnyx.Media.retrieve(TEST_RESOURCE_ID)
        resource.download(id=TEST_RESOURCE_ID)
