from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestSIMCardGroups(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.SIMCardGroup.list()
        request_mock.assert_requested("get", "/v2/sim_card_groups")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.SIMCardGroup)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.SIMCardGroup.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/sim_card_groups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SIMCardGroup)

    def test_is_creatable(self, request_mock):
        resource = telnyx.SIMCardGroup.create(
            name="My Test Group",
        )
        request_mock.assert_requested("post", "/v2/sim_card_groups")
        assert isinstance(resource, telnyx.SIMCardGroup)

    def test_is_saveable(self, request_mock):
        sim_card_group = telnyx.SIMCardGroup.retrieve(TEST_RESOURCE_ID)
        sim_card_group.name = "My Test Group"
        resource = sim_card_group.save()
        request_mock.assert_requested(
            "patch", "/v2/sim_card_groups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SIMCardGroup)
        assert resource is sim_card_group

    def test_is_modifiable(self, request_mock):
        resource = telnyx.SIMCardGroup.modify(
            TEST_RESOURCE_ID,
            name="Updated Name",
        )
        request_mock.assert_requested(
            "patch", "/v2/sim_card_groups/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.SIMCardGroup)

    def test_is_deletable(self, request_mock):
        resource = telnyx.SIMCardGroup.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/sim_card_groups/%s" % TEST_RESOURCE_ID
        )
