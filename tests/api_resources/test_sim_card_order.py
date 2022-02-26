from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestSIMCardOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.SIMCardOrder.list()
        request_mock.assert_requested("get", "/v2/sim_card_orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.SIMCardOrder)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.SIMCardOrder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/sim_card_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SIMCardOrder)

    def test_is_creatable(self, request_mock):
        resource = telnyx.SIMCardOrder.create(address_id=TEST_RESOURCE_ID, quantity=23)
        request_mock.assert_requested("post", "/v2/sim_card_orders")
        assert isinstance(resource, telnyx.SIMCardOrder)

    def test_can_sim_preview(self, request_mock):
        telnyx.SIMCardOrderPreview.create(
            address_id=TEST_RESOURCE_ID, quantity=23
        )
