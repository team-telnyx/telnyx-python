from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestFaxApplication(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.FaxApplication.list()
        request_mock.assert_requested("get", "/v2/fax_applications")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.FaxApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.FaxApplication.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/fax_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FaxApplication)

    def test_is_creatable(self, request_mock):
        resource = telnyx.FaxApplication.create(
            active=True,
            application_name="Test Name",
            webhook_event_url="https://test.com",
        )
        request_mock.assert_requested("post", "/v2/fax_applications")
        assert isinstance(resource, telnyx.FaxApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_saveable(self, request_mock):
        fax_application = telnyx.FaxApplication.retrieve(TEST_RESOURCE_ID)
        fax_application.active = False
        fax_application.webhook_event_url = "https://update.com"
        fax_application.application_name = "updated name"
        resource = fax_application.save()
        request_mock.assert_requested(
            "patch", "/v2/fax_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FaxApplication)
        assert resource is fax_application

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.FaxApplication.modify(
            TEST_RESOURCE_ID,
            active=False,
            webhook_event_url="https://update.com",
            application_name="updated name",
        )
        request_mock.assert_requested(
            "patch", "/v2/fax_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.FaxApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_deletable(self, request_mock):
        resource = telnyx.FaxApplication.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/fax_applications/%s" % TEST_RESOURCE_ID
        )
