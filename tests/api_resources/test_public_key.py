from __future__ import absolute_import, division, print_function

import pytest

import telnyx


class TestPublicKey(object):
    @pytest.mark.skip(reason="Unsure about this endpoint, might be deprecated")
    def test_is_retrievable(self, request_mock):
        resource = telnyx.PublicKey.retrieve()
        request_mock.assert_requested("get", "/v2/public_key")
        assert isinstance(resource, telnyx.PublicKey)
