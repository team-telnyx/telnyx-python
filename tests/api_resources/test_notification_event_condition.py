from __future__ import absolute_import, division, print_function

import telnyx


class TestNotificationEventCondition(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.NotificationEventCondition.list()
        request_mock.assert_requested("get", "/v2/notification_event_conditions")
        assert isinstance(resources.data, list)
