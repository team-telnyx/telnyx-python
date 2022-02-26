from __future__ import absolute_import, division, print_function

import pytest

import telnyx

TEST_RESOURCE_ID = "45f45a04-b4be-4592-95b1-9306b9db2b21"


@pytest.mark.skip(reason="Filter looking for 'filter%5bphone_number%5d', typo")
class TestInventoryCoverage(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.InventoryCoverage.list(
            filter={"groupBy": "npa"}
        )
        request_mock.assert_requested(
            "get", "/v2/inventory_coverage"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.InventoryCoverage)
