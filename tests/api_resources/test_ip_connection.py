from __future__ import absolute_import, division, print_function

import pytest
import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestIPConnection(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.IPConnection.list()
        request_mock.assert_requested("get", "/v2/ip_connections")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.IPConnection)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.IPConnection.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/ip_connections/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.IPConnection)

    def test_is_creatable(self, request_mock):
        resource = telnyx.IPConnection.create()
        request_mock.assert_requested("post", "/v2/ip_connections")
        assert isinstance(resource, telnyx.IPConnection)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_saveable(self, request_mock):
        ip_connection = telnyx.IPConnection.retrieve(TEST_RESOURCE_ID)
        ip_connection.active = False
        resource = ip_connection.save()
        request_mock.assert_requested(
            "patch", "/v2/ip_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.IPConnection)
        assert resource is ip_connection

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.IPConnection.modify(TEST_RESOURCE_ID, active=False)
        request_mock.assert_requested(
            "patch", "/v2/ip_connections/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.IPConnection)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_deletable(self, request_mock):
        resource = telnyx.IPConnection.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/ip_connections/%s" % TEST_RESOURCE_ID
        )
