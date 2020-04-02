from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class Address(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "address"

    @classmethod
    def class_url(cls):
        return "/v2/addresses"
