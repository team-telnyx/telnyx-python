from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestAddress(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Address.list()
        request_mock.assert_requested("get", "/v2/addresses")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.Address)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.Address.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/addresses/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Address)

    def test_is_creatable(self, request_mock):
        resource = telnyx.Address.create(name="my-profile")
        request_mock.assert_requested("post", "/v2/addresses")
        assert isinstance(resource, telnyx.Address)

    def test_is_deletable(self, request_mock):
        resource = telnyx.Address.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested("delete", "/v2/addresses/%s" % TEST_RESOURCE_ID)
