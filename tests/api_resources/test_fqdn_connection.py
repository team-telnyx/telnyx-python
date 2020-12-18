from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestFQDNConnection(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.FQDNConnection.list()
        request_mock.assert_requested("get", "/v2/fqdn_connections")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.FQDNConnection)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.FQDNConnection.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/fqdn_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FQDNConnection)

    def test_is_creatable(self, request_mock):
        resource = telnyx.FQDNConnection.create(active=True,
                                                connection_name="Test Name")
        request_mock.assert_requested("post", "/v2/fqdn_connections")
        assert isinstance(resource, telnyx.FQDNConnection)

    def test_is_saveable(self, request_mock):
        fqdn_connection = telnyx.FQDNConnection.retrieve(TEST_RESOURCE_ID)
        fqdn_connection.active = False
        resource = fqdn_connection.save()
        request_mock.assert_requested(
            "patch", "/v2/fqdn_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FQDNConnection)
        assert resource is fqdn_connection

    def test_is_modifiable(self, request_mock):
        resource = telnyx.FQDNConnection.modify(TEST_RESOURCE_ID, active=False)
        request_mock.assert_requested(
            "patch", "/v2/fqdn_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FQDNConnection)

    def test_is_deletable(self, request_mock):
        resource = telnyx.FQDNConnection.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/fqdn_connections/%s" % TEST_RESOURCE_ID
        )
