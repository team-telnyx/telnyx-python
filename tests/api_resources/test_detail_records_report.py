from __future__ import absolute_import, division, print_function

import telnyx

TEST_RESOURCE_ID = "123"


class TestDetailRecordsReport(object):
    def test_is_listable(self, request_mock):
        resources = telnyx.DetailRecordsReport.list()
        request_mock.assert_requested("get", "/v2/wireless/detail_records_reports")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], telnyx.DetailRecordsReport)

    def test_is_retrievable(self, request_mock):
        resource = telnyx.DetailRecordsReport.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v2/wireless/detail_records_reports/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, telnyx.DetailRecordsReport)

    def test_is_creatable(self, request_mock):
        resource = telnyx.DetailRecordsReport.create(
            start_time="2018-02-02T22:25:27.521Z", end_time="2018-02-02T22:25:27.521Z"
        )
        request_mock.assert_requested("post", "/v2/wireless/detail_records_reports")
        assert isinstance(resource, telnyx.DetailRecordsReport)

    def test_is_deletable(self, request_mock):
        resource = telnyx.DetailRecordsReport.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v2/wireless/detail_records_reports/%s" % TEST_RESOURCE_ID
        )
