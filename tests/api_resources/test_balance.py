from __future__ import absolute_import, division, print_function

import telnyx


class TestBalance(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.Balance.retrieve()
        request_mock.assert_requested("get", "/v2/balance")
        assert isinstance(resource, telnyx.Balance)
