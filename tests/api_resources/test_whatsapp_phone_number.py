from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestWhatsappPhoneNumber(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.WhatsappPhoneNumber.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/whatsapp_phone_numbers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.WhatsappPhoneNumber)

    def test_is_updateable(self, request_mock):
        resource = telnyx.WhatsappPhoneNumber.retrieve(TEST_RESOURCE_ID)
        resource.save()
        request_mock.assert_requested(
            "get", "/v2/whatsapp_phone_numbers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.WhatsappPhoneNumber)
