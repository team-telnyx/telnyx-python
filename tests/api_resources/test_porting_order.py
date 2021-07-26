from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestPortingOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PortingOrder.list()
        request_mock.assert_requested("get", "/v2/porting_orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.PortingOrder)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/porting_orders/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="We just can create an order from a valid number")
    def test_is_creatable(self, request_mock):
        resource = telnyx.PortingOrder.create(
            phone_number=["13035550000", "13035550001", "13035550002"],
        )
        request_mock.assert_requested("post", "/v2/porting_orders")
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="We just can save an existing order")
    def test_is_saveable(self, request_mock):
        porting_order = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        porting_order.webhook_event = "https://update.com"
        porting_order.customer_reference = "updated name"
        resource = porting_order.save()
        request_mock.assert_requested(
            "patch", "/v2/porting_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)
        assert resource is porting_order

    @pytest.mark.skip(reason="We just can modify an existing order")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.PortingOrder.modify(
            TEST_RESOURCE_ID,
            webhook_event="https://update.com",
            customer_reference="updated name",
        )
        request_mock.assert_requested(
            "patch", "/v2/porting_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="We just can delete an existing order")
    def test_is_deletable(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/porting_orders/%s" % TEST_RESOURCE_ID
        )
