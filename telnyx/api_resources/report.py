from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource, ListableAPIResource


class Report(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "report"
