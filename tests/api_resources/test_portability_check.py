from __future__ import absolute_import, division, print_function

import telnyx


class TestPortabilityCheck(object):
    def test_is_creatable(self, request_mock):
        telnyx.PortabilityCheck.create()
        request_mock.assert_requested("post", "/v2/portability_checks")
