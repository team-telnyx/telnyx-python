from __future__ import absolute_import, division, print_function

import telnyx
import pytest

TEST_RESOURCE_ID = "1293384261075731499"


class TestManagedAccount(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.ManagedAccount.list()
        request_mock.assert_requested("get", "/v2/managed_accounts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.ManagedAccount)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.ManagedAccount.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/managed_accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.ManagedAccount)

    def test_is_creatable(self, request_mock):
        resource = telnyx.ManagedAccount.create(
            business_name="Larry's Cat Food Inc"
        )
        request_mock.assert_requested("post", "/v2/managed_accounts")

    def test_is_modifiable(self, request_mock):
        resource = telnyx.ManagedAccount.modify(
            TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "patch", "/v2/managed_accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.ManagedAccount)

    @pytest.mark.skip(reason="Empty body")
    def test_can_enable(self, request_mock):
        resource = telnyx.ManagedAccount.retrieve(TEST_RESOURCE_ID)
        resource.enable()
        request_mock.assert_requested(
            "post", "/v2/managed_accounts/%s/actions/enable" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.ManagedAccount)

    @pytest.mark.skip(reason="Empty body")
    def test_can_disable(self, request_mock):
        resource = telnyx.ManagedAccount.retrieve(TEST_RESOURCE_ID)
        resource.disable()
        request_mock.assert_requested(
            "post", "/v2/managed_accounts/%s/actions/disable" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.ManagedAccount)