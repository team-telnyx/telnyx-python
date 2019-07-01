from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "12ade33a-21c0-473b-b055-b3c836e1c292"


class TestNumberOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NumberOrder.list()
        request_mock.assert_requested("get", "/v2/number_orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.NumberOrder)

    @pytest.mark.skip(reason="We just can retrieve an existing order")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.NumberOrder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/number_orders/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.NumberOrder)

    @pytest.mark.skip(
        reason="We just can create an order from a valid available number"
    )
    def test_is_creatable(self, request_mock):
        resource = telnyx.NumberOrder.create(
            phone_numbers=[
                {"phone_number": "+12223334444", "regulatory_requirements": []}
            ],
            customer_reference="MY REF 001",
            connection_id="442191469269222625",
            messaging_profile_id="730911e3-8488-40a8-a818-dc0a5df8bc03",
        )
        request_mock.assert_requested("post", "/v2/number_orders")
        assert isinstance(resource, telnyx.NumberOrder)

    @pytest.mark.skip(reason="We just can save an existing order")
    def test_is_saveable(self, request_mock):
        number_order = telnyx.NumberOrder.retrieve(TEST_RESOURCE_ID)
        number_order.customer_reference = "value"
        resource = number_order.save()
        request_mock.assert_requested(
            "patch", "/v2/number_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.NumberOrder)
        assert resource is number_order

    @pytest.mark.skip(reason="We just can modify an existing order")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.NumberOrder.modify(
            TEST_RESOURCE_ID, customer_reference="Test"
        )
        request_mock.assert_requested(
            "patch", "/v2/number_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.NumberOrder)
