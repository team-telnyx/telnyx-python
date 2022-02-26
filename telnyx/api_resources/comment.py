from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (ListableAPIResource, CreateableAPIResource)


class Comment(ListableAPIResource, CreateableAPIResource):
    OBJECT_NAME = "comment"
