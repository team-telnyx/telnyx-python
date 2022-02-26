from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "6a09cdc3-8948-47f0-aa62-74ac943d6c58"


class TestWirelessDetailRecords(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.WirelessDetailRecordsReports.list()
        request_mock.assert_requested("get", "/v2/wireless/detail_records_reports")
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, request_mock):
        telnyx.WirelessDetailRecordsReports.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/wireless/detail_records_reports/%s" % TEST_RESOURCE_ID
        )

    def test_is_creatable(self, request_mock):
        telnyx.WirelessDetailRecordsReports.create()
        request_mock.assert_requested("post", "/v2/wireless/detail_records_reports")

    def test_is_deletable(self, request_mock):
        resource = telnyx.WirelessDetailRecordsReports.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/wireless/detail_records_reports/%s" % TEST_RESOURCE_ID
        )
