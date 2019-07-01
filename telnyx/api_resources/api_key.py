from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource
from telnyx.api_resources.abstract import DeletableAPIResource
from telnyx.api_resources.abstract import ListableAPIResource


class APIKey(CreateableAPIResource, ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "api_key"
