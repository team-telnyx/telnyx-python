import pytest

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestWebhookDeliveries(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.WebhookDeliveries.list()
        request_mock.assert_requested("get", "/v2/webhook_deliveries")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.WebhookDeliveries.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/webhook_deliveries/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.WebhookDeliveries)
