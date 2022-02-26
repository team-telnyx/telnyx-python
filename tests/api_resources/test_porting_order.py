from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "f1486bae-f067-460c-ad43-73a92848f902"


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

    def test_is_creatable(self, request_mock):
        resource = telnyx.PortingOrder.create(
            phone_numbers=["13035550000", "13035550001", "13035550002"],
        )
        request_mock.assert_requested("post", "/v2/porting_orders")
        assert isinstance(resource.data[0], telnyx.PortingOrder)

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

    @pytest.mark.skip(reason="Needs live confirm")
    def test_can_confirm_porting_order_action(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.create_confirm(id=TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v2/porting_orders/%s/actions/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="Needs live cancel")
    def test_can_cancel_porting_order_action(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.create_cancel(id=TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v2/porting_orders/%s/actions/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="PDF endpoint not supported by mock currently")
    def test_can_get_loa_template(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.loaTemplate()
        request_mock.assert_requested(
            "get", "/v2/porting_orders/%s/loa_template" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="Unreleased")
    def test_can_list_allowed_foc_dates(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.allowed_foc_windows()
        request_mock.assert_requested(
            "get", "/v2/porting_orders/%s/allowed_foc_windows" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="Unreleased")
    def test_can_list_activation_jobs(self, request_mock):
        resource = telnyx.PortingOrder.retrieve(TEST_RESOURCE_ID)
        resource.activation_jobs()
        request_mock.assert_requested(
            "get", "/v2/porting_orders/%s/activation_jobs" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PortingOrder)

    @pytest.mark.skip(reason="Unreleased")
    def test_can_list_exception_types(self, request_mock):
        telnyx.PortingOrder.create_exception_types()
        request_mock.assert_requested(
            "get", "/v2/porting_orders/exception_types"
        )

    def test_can_list_porting_phone_numbers(self, request_mock):
        resource = telnyx.PortingPhoneNumber.list()
        request_mock.assert_requested("get", "/v2/porting_phone_numbers")
        assert isinstance(resource.data, list)
        assert isinstance(resource.data[0], telnyx.PortingPhoneNumber)



