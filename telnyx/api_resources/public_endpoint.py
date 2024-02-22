from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class PublicEndpoint(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "public_endpoint"
