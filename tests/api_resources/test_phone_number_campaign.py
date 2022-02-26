from __future__ import absolute_import, division, print_function

import telnyx
import pytest

TEST_RESOURCE_ID = "1293384261075731499"


@pytest.mark.skip(reason="Unreleased")
class TestPhoneNumberCampaign(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.PhoneNumberCampaign.list()
        request_mock.assert_requested("get", "/10dlc/phoneNumberCampaign")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.PhoneNumberCampaign)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.PhoneNumberCampaign.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/10dlc/phoneNumberCampaign/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PhoneNumberCampaign)

    def test_is_creatable(self, request_mock):
        resource = telnyx.PhoneNumberCampaign.create(
            phoneNumber="1920324562",
            campaignID=TEST_RESOURCE_ID,
        )
        request_mock.assert_requested("post", "/10dlc/phoneNumberCampaign")
        assert isinstance(resource, telnyx.PhoneNumberCampaign)

    def test_is_modifiable(self, request_mock):
        resource = telnyx.PhoneNumberCampaign.modify(
            TEST_RESOURCE_ID,)
        request_mock.assert_requested(
            "patch", "/10dlc/phoneNumberCampaign/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.PhoneNumberCampaign)

    def test_is_deletable(self, request_mock):
        resource = telnyx.PhoneNumberCampaign.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/10dlc/phoneNumberCampaign/%s" % TEST_RESOURCE_ID
        )
