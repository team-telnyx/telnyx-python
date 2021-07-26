from __future__ import absolute_import, division, print_function

import telnyx


class TestPortabilityCheck(object):
    # @pytest.mark.skip(reason="We just can create an order from a valid number")
    def test_is_creatable(self, request_mock):
        resource = telnyx.PortabilityCheck.create()
        request_mock.assert_requested("post", "/v2/portability_checks")
        assert isinstance(resource, telnyx.PortabilityCheck)
