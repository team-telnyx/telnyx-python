from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "f5586561-8ff0-4291-a0ac-84fe544797bd"


class TestBillingGroup(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.BillingGroup.list()
        request_mock.assert_requested("get", "/v2/billing_groups")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.BillingGroup)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.BillingGroup.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/billing_groups/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.BillingGroup)

    def test_is_creatable(self, request_mock):
        resource = telnyx.BillingGroup.create(name="foo")
        request_mock.assert_requested("post", "/v2/billing_groups")
        assert isinstance(resource, telnyx.BillingGroup)

    def test_is_saveable(self, request_mock):
        billing_group = telnyx.BillingGroup.retrieve(TEST_RESOURCE_ID)
        billing_group.name = "bar"
        resource = billing_group.save()
        request_mock.assert_requested(
            "patch", "/v2/billing_groups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.BillingGroup)
        assert resource is billing_group

    def test_is_modifiable(self, request_mock):
        resource = telnyx.BillingGroup.modify(TEST_RESOURCE_ID, name="foo")
        request_mock.assert_requested(
            "patch", "/v2/billing_groups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.BillingGroup)

    def test_is_deletable(self, request_mock):
        resource = telnyx.BillingGroup.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/billing_groups/%s" % TEST_RESOURCE_ID
        )
