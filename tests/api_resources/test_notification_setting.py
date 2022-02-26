from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestNotificationSetting(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NotificationSetting.list()
        request_mock.assert_requested("get", "/v2/notification_settings")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.NotificationSetting.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/notification_settings/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.NotificationSetting)

    @pytest.mark.skip(reason="Create mismatch")
    def test_is_creatable(self, request_mock):
        resource = telnyx.NotificationSetting.create()
        request_mock.assert_requested("post", "/v2/notification_settings")
        assert isinstance(resource, telnyx.NotificationSetting)

    @pytest.mark.skip(reason="Not released, no path yet")
    def test_is_deletable(self, request_mock):
        resource = telnyx.NotificationSetting.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/notification_settings/%s" % TEST_RESOURCE_ID
        )
