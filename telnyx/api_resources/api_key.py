from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class APIKey(CreateableAPIResource, ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "api_key"
