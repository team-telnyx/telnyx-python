from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestAccessControlIp(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.AccessControlIp.list()
        request_mock.assert_requested("get", "/v2/access_control_ips")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AccessControlIp)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.AccessControlIp.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/access_control_ips/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.AccessControlIp)

    def test_is_creatable(self, request_mock):
        resource = telnyx.AccessControlIp.create()
        request_mock.assert_requested("post", "/v2/access_control_ips")
        assert isinstance(resource, telnyx.AccessControlIp)

    def test_is_saveable(self, request_mock):
        access_control_ip = telnyx.AccessControlIp.retrieve(TEST_RESOURCE_ID)
        access_control_ip.description = "Signaling IP for system1"
        access_control_ip.ip_address = "100.101.102.103"
        resource = access_control_ip.save()
        request_mock.assert_requested(
            "patch", "/v2/access_control_ips/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AccessControlIp)
        assert resource is access_control_ip

    def test_is_deletable(self, request_mock):
        resource = telnyx.AccessControlIp.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/access_control_ips/%s" % TEST_RESOURCE_ID
        )
