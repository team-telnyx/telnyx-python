from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestWhatsappContact(object):
    def test_is_creatable(self, request_mock):
        resource = telnyx.WhatsappContact.create(
            contacts=["19201234567"],
            whatsapp_user_id="15125551234"
        )
        request_mock.assert_requested("post", "/v2/whatsapp_contacts")
        #assert isinstance(resource, telnyx.WhatsappContact)
