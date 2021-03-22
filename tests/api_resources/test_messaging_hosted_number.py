from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"

class TestMessagingHostedNumber(object):
    @pytest.mark.skip(
        reason="Resource not there just yet for endpoint"
    )
    def test_is_deletable(self, request_mock):
        resource = telnyx.MessagingHostedNumber()
        resource.id = TEST_RESOURCE_ID
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/messaging_hosted_numbers/%s" % TEST_RESOURCE_ID
        )
