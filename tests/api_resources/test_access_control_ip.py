from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0"


@pytest.mark.skip(reason="Prism Mock returns unexpected non-200 response")
class TestAddress(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.AccessControlIP.list()
        request_mock.assert_requested("get", "/v2/access_control_ips")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AccessControlIP)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.AccessControlIP.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/access_control_ips/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AccessControlIP)

    def test_is_creatable(self, request_mock):
        resource = telnyx.AccessControlIP.create(ip_address="100.101.102.103")
        request_mock.assert_requested("post", "/v2/access_control_ips")
        assert isinstance(resource, telnyx.AccessControlIP)

    def test_is_deletable(self, request_mock):
        resource = telnyx.AccessControlIP.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/access_control_ips/%s" % TEST_RESOURCE_ID
        )
