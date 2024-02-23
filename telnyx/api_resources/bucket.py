from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)


class Bucket(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "bucket"
