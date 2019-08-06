from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import UpdateableAPIResource
from telnyx.api_resources.abstract import ListableAPIResource


class ShortCode(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "short_code"
