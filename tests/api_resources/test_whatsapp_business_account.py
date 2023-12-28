import pytest

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


@pytest.mark.skip(reason="Prism Mock returns unexpected non-200 response")
class TestWhatsappBusinessAccount(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.WhatsappBusinessAccount.list()
        request_mock.assert_requested("get", "/v2/whatsapp_business_accounts")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.WhatsappBusinessAccount.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/whatsapp_business_accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.WhatsappBusinessAccount)
