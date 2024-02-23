from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    UpdateableAPIResource,
)


class BulkCredential(
    CreateableAPIResource, DeletableAPIResource, UpdateableAPIResource
):
    OBJECT_NAME = "bulk_credential"
