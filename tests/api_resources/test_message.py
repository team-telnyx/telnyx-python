from __future__ import absolute_import, division, print_function

import telnyx

TEST_MESSAGING_PROFILE_ID = "d120432d-2e77-4583-87f8-1db837cee559"
TEST_SRC_LONG_CODE = "+13125550100"
TEST_SRC_ALPHANUMERIC = "Testing 123"
TEST_DST = "+17735550100"
TEST_MESSAGE_BODY = "Hello!"


class TestMessage(object):
    def test_can_create_standard_message(self, request_mock):
        resource = telnyx.Message.create(
            from_=TEST_SRC_LONG_CODE, to=TEST_DST, text=TEST_MESSAGE_BODY
        )
        request_mock.assert_requested("post", "/v2/messages")
        assert isinstance(resource, telnyx.Message)

    def test_can_create_alphanumeric_sender_id_message(self, request_mock):
        resource = telnyx.Message.send_from_alphanumeric_sender_id(
            messaging_profile_id=TEST_MESSAGING_PROFILE_ID,
            from_=TEST_SRC_ALPHANUMERIC,
            to=TEST_DST,
            text=TEST_MESSAGE_BODY,
        )
        request_mock.assert_requested("post", "/v2/messages/alphanumeric_sender_id")
        assert isinstance(resource, telnyx.Message)
