from __future__ import absolute_import, division, print_function

import telnyx


class TestNotificationEvent(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NotificationEvent.list()
        request_mock.assert_requested("get", "/v2/notification_events")
        assert isinstance(resources.data, list)
