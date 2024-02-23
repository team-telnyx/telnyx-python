from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class MdrDetailReport(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "mdr_detail_report"
