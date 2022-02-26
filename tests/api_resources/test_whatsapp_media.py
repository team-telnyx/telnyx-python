from __future__ import absolute_import, division, print_function

import pytest

import telnyx


TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"
TEST_RESOURCE_ID_2 = "92ade33a-21c0-473b-b055-b3c836e1c292"


class TestWhatsappMedia(object):
    @pytest.mark.skip(reason="Need to make test for media uploads")
    def test_is_creatable(self, request_mock):
        resource = telnyx.WhatsappMedia.create(
            media_content_type=["19201234567"],
            upload_file="This is a test",
            whatsapp_user_id="123144121"
        )
        request_mock.assert_requested("post", "/v2/whatsapp_media")
        assert isinstance(resource, telnyx.WhatsappMedia)
