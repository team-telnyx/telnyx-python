from __future__ import absolute_import, division, print_function

import telnyx
from telnyx.six.moves.urllib.parse import quote_plus


TEST_RESOURCE_ID = "+18005554000"


class TestMessagingPhoneNumber(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingPhoneNumber.list()
        request_mock.assert_requested("get", "/v2/messaging_phone_numbers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingPhoneNumber)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingPhoneNumber.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_phone_numbers/%s" % quote_plus(TEST_RESOURCE_ID)
        )
        assert isinstance(resource, telnyx.MessagingPhoneNumber)

    def test_is_saveable(self, request_mock):
        messaging_phone_number = telnyx.MessagingPhoneNumber.retrieve(TEST_RESOURCE_ID)
        messaging_phone_number.name = "value"
        resource = messaging_phone_number.save()
        request_mock.assert_requested(
            "patch", "/v2/messaging_phone_numbers/%s" % quote_plus(TEST_RESOURCE_ID)
        )
        assert isinstance(resource, telnyx.MessagingPhoneNumber)
        assert resource is messaging_phone_number

    def test_is_modifiable(self, request_mock):
        resource = telnyx.MessagingPhoneNumber.modify(TEST_RESOURCE_ID, name="Test")
        request_mock.assert_requested(
            "patch", "/v2/messaging_phone_numbers/%s" % quote_plus(TEST_RESOURCE_ID)
        )
        assert isinstance(resource, telnyx.MessagingPhoneNumber)
