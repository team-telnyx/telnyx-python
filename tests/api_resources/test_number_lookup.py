from __future__ import absolute_import, division, print_function

import urllib.parse

import telnyx

TEST_RESOURCE_ID = "+18665552368"


class TestNumberLookup(object):
    def test_is_retrievable(self, request_mock):
        resource = telnyx.NumberLookup.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/number_lookup/%s" % urllib.parse.quote(TEST_RESOURCE_ID)
        )
        assert isinstance(resource, telnyx.NumberLookup)
