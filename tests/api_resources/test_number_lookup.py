from __future__ import absolute_import, division, print_function

import telnyx


class TestNumberLookup(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.NumberLookup.retrieve("+18665552368")
        request_mock.assert_requested("get", "/v2/number_lookup/%2B18665552368")
        assert isinstance(resource, telnyx.NumberLookup)
