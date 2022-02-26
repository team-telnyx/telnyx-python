from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestWhatsappMessage(object):
    @pytest.mark.skip(reason="API response structure fix needed")
    def test_is_createable(self, request_mock):
        resource = telnyx.WhatsappMessage.create(
            to="96214131231", whatsapp_user_id="1231244123412"
        )
        request_mock.assert_requested("post", "/v2/whatsapp_messages")
        assert isinstance(resource, telnyx.WhatsappMessage)

    @pytest.mark.skip(reason="Response code 204, not 200 (passes)")
    def test_is_updateable(self, request_mock):
        resource = telnyx.WhatsappMessage(TEST_RESOURCE_ID)
        resource.status = "read"
        resource.whatsapp_user_id = "1512551212"
        resource.save()
