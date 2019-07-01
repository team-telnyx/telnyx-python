from __future__ import absolute_import, division, print_function

import telnyx


TEST_RESOURCE_ID = "123"


class TestMessagingShortCode(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingShortCode.list()
        request_mock.assert_requested("get", "/v2/messaging_short_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingShortCode)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingShortCode.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_short_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingShortCode)

    def test_is_saveable(self, request_mock):
        messaging_short_code = telnyx.MessagingShortCode.retrieve(TEST_RESOURCE_ID)
        messaging_short_code.name = "value"
        resource = messaging_short_code.save()
        request_mock.assert_requested(
            "patch", "/v2/messaging_short_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingShortCode)
        assert resource is messaging_short_code

    def test_is_modifiable(self, request_mock):
        resource = telnyx.MessagingShortCode.modify(TEST_RESOURCE_ID, name="Test")
        request_mock.assert_requested(
            "patch", "/v2/messaging_short_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingShortCode)
