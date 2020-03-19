from __future__ import absolute_import, division, print_function

import telnyx.request_metrics


class TestRequestMetrics(object):
    def test_payload(self):
        metrics = telnyx.request_metrics.RequestMetrics("1", 1000)

        assert metrics.payload() == {"request_id": "1", "request_duration_ms": 1000}
