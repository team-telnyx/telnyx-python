from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class AccessIPAddress(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "access_ip_address"

    @classmethod
    def class_url(cls):
        return "/v2/access_ip_address"
