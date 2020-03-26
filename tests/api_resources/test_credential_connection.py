from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestCredentialConnection(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.CredentialConnection.list()
        request_mock.assert_requested("get", "/v2/credential_connections")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.CredentialConnection)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.CredentialConnection.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/credential_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CredentialConnection)

    def test_is_creatable(self, request_mock):
        resource = telnyx.CredentialConnection.create(active=True)
        request_mock.assert_requested("post", "/v2/credential_connections")
        assert isinstance(resource, telnyx.CredentialConnection)

    def test_is_saveable(self, request_mock):
        credential_connection = telnyx.CredentialConnection.retrieve(TEST_RESOURCE_ID)
        credential_connection.active = False
        resource = credential_connection.save()
        request_mock.assert_requested(
            "patch", "/v2/credential_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CredentialConnection)
        assert resource is credential_connection

    def test_is_modifiable(self, request_mock):
        resource = telnyx.CredentialConnection.modify(TEST_RESOURCE_ID, active=False)
        request_mock.assert_requested(
            "patch", "/v2/credential_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CredentialConnection)

    def test_is_deletable(self, request_mock):
        resource = telnyx.CredentialConnection.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/credential_connections/%s" % TEST_RESOURCE_ID
        )
