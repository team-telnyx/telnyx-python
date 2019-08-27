from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "123"


class TestAlphanumericSenderId(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.AlphanumericSenderId.list()
        request_mock.assert_requested("get", "/v2/alphanumeric_sender_ids")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AlphanumericSenderId)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.AlphanumericSenderId.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/alphanumeric_sender_ids/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AlphanumericSenderId)

    def test_is_creatable(self, request_mock):
        resource = telnyx.AlphanumericSenderId.create(country="US", type="custom")
        request_mock.assert_requested("post", "/v2/alphanumeric_sender_ids")
        assert isinstance(resource, telnyx.AlphanumericSenderId)

    def test_is_deletable(self, request_mock):
        resource = telnyx.AlphanumericSenderId.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/alphanumeric_sender_ids/%s" % TEST_RESOURCE_ID
        )
