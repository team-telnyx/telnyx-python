from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class WirelessDetailRecordsReports(
    CreateableAPIResource, ListableAPIResource, DeletableAPIResource
):
    OBJECT_NAME = "wireless_detail_records_report"

    @classmethod
    def class_url(cls):
        return "/v2/wireless/detail_records_reports"
