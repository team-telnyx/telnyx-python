from __future__ import absolute_import, division, print_function

import telnyx


class TestAvailablePhoneNumber(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.AvailablePhoneNumber.list(
            filter={
                "limit": 1,
                "features": ["sms", "mms"],
                "phone_number": {"contains": "555"},
            }
        )
        request_mock.assert_requested("get", "/v2/available_phone_numbers")
        assert isinstance(resources.data, list)
        assert len(resources.data) == 1
        assert isinstance(resources.data[0], telnyx.AvailablePhoneNumber)
