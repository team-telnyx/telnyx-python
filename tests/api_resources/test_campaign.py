from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


@pytest.mark.skip(reason="Not implemented yet")
class TestCampaign(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.Campaign.list()
        request_mock.assert_requested("get", "/10dlc/campaign")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.Campaign)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.Campaign.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v2/campaign/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, telnyx.Campaign)

    def test_is_creatable(self, request_mock):
        resource = telnyx.FaxApplication.create(
            active=True,
            application_name="Test Name",
            webhook_event_url="https://test.com",
        )
        request_mock.assert_requested("post", "/v2/fax_applications")
        assert isinstance(resource, telnyx.FaxApplication)

    def test_is_deletable(self, request_mock):
        resource = telnyx.Campaign.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested("delete", "/10dlc/campaign/%s" % TEST_RESOURCE_ID)
