from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "35146afd-df93-4963-b1e9-1a085e2ae874"


class TestAuthenticationProvider(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.AuthenticationProvider.list()
        request_mock.assert_requested("get", "/v2/authentication_providers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.AuthenticationProvider)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.AuthenticationProvider.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/authentication_providers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AuthenticationProvider)

    @pytest.mark.skip(reason="Formatting for setting param is off")
    def test_is_creatable(self, request_mock):
        resource = telnyx.AuthenticationProvider.create(
            name="Okta", setting=[], short_name="myorg"
        )
        request_mock.assert_requested("post", "/v2/authentication_providers")
        assert isinstance(resource, telnyx.AuthenticationProvider)

    def test_is_saveable(self, request_mock):
        authentication_provider = telnyx.AuthenticationProvider.retrieve(
            TEST_RESOURCE_ID
        )
        authentication_provider.name = "value"
        resource = authentication_provider.save()
        request_mock.assert_requested(
            "patch", "/v2/authentication_providers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AuthenticationProvider)
        assert resource is authentication_provider

    def test_is_modifiable(self, request_mock):
        resource = telnyx.AuthenticationProvider.modify(TEST_RESOURCE_ID, active=False)
        request_mock.assert_requested(
            "patch", "/v2/authentication_providers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.AuthenticationProvider)

    def test_is_deletable(self, request_mock):
        resource = telnyx.AuthenticationProvider.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/authentication_providers/%s" % TEST_RESOURCE_ID
        )
