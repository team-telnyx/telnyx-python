import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestSubNumberOrder(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.SubNumberOrder.list()
        request_mock.assert_requested("get", "/v2/sub_number_orders")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.SubNumberOrder)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.SubNumberOrder.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/sub_number_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SubNumberOrder)

    def test_is_modifiable(self, request_mock):
        resource = telnyx.SubNumberOrder.modify(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "patch", "/v2/sub_number_orders/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SubNumberOrder)
