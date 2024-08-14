from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "1293384261075731499"


class TestCallControlApplication(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.CallControlApplication.list()
        request_mock.assert_requested("get", "/v2/call_control_applications")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.CallControlApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.CallControlApplication.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/call_control_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CallControlApplication)

    def test_is_creatable(self, request_mock):
        resource = telnyx.CallControlApplication.create(
            connection_name="foo",
            webhook_event_url="http://foo.com",
            application_name="foo",
        )
        request_mock.assert_requested("post", "/v2/call_control_applications")
        assert isinstance(resource, telnyx.CallControlApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_saveable(self, request_mock):
        call_control_application = telnyx.CallControlApplication.retrieve(
            TEST_RESOURCE_ID
        )
        call_control_application.connection_name = "foo"
        call_control_application.webhook_event_url = "http://foo.com"
        call_control_application.application_name = "foo"
        resource = call_control_application.save()
        request_mock.assert_requested(
            "patch", "/v2/call_control_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CallControlApplication)
        assert resource is call_control_application

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_modifiable(self, request_mock):
        resource = telnyx.CallControlApplication.modify(
            TEST_RESOURCE_ID,
            connection_name="foo",
            webhook_event_url="http://foo.com",
            application_name="foo",
        )
        request_mock.assert_requested(
            "patch", "/v2/call_control_applications/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.CallControlApplication)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_is_deletable(self, request_mock):
        resource = telnyx.CallControlApplication.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/call_control_applications/%s" % TEST_RESOURCE_ID
        )
