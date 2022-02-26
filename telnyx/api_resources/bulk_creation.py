from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "detailed_status", path="detailedStatus", operations=["list"]
)
class BulkCreation(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "bulk_creation"

    @classmethod
    def class_url(cls):
        return "/10dlc/bulkCreation"

    def detailed_status(self, **params):
        return BulkCreation.list_detailed_status(self.name, **params)
