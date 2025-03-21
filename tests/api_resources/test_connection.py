from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestConnection(object):
    connection_types = (
        telnyx.IPConnection,
        telnyx.CredentialConnection,
        telnyx.IP,
        telnyx.FQDNConnection,
        telnyx.FQDN,
    )

    def test_is_listable(self, request_mock):
        resources = telnyx.Connection.list()
        request_mock.assert_requested("get", "/v2/connections")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], self.connection_types)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.Connection.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/connections/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, self.connection_types)
        
    def test_active_calls_instance_method(self, request_mock):
        connection = telnyx.Connection.retrieve(TEST_RESOURCE_ID)
        connection.active_calls()
        request_mock.assert_requested(
            "get", "/v2/connections/%s/active_calls" % TEST_RESOURCE_ID
        )
        
    def test_active_calls_class_method(self, request_mock):
        telnyx.Connection.list_active_calls(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/connections/%s/active_calls" % TEST_RESOURCE_ID
        )
