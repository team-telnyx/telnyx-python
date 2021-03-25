from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestMessagingHostedNumberOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.MessagingHostedNumberOrder.list()
        request_mock.assert_requested("get", "/v2/messaging_hosted_number_orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.MessagingHostedNumberOrder)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.MessagingHostedNumberOrder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/messaging_hosted_number_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.MessagingHostedNumberOrder)

    def test_is_creatable(self, request_mock):
        resource = telnyx.MessagingHostedNumberOrder.create()
        request_mock.assert_requested("post", "/v2/messaging_hosted_number_orders")
        assert isinstance(resource, telnyx.MessagingHostedNumberOrder)
