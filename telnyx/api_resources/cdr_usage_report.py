from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class CdrUsageReport(ListableAPIResource):
    OBJECT_NAME = "cdr_usage_report"
