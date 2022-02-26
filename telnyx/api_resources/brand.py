from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "list_external_vetting", path="externalVetting", operations=["list"]
)
@nested_resource_class_methods(
    "order_external_vetting", path="externalVetting", operations=["create"]
)
class Brand(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "brand"

    @classmethod
    def class_url(cls):
        return "/10dlc/brand"

    def list_external_vetting(self, **params):
        return Brand.list_external_vetting(self.name, **params)

    def operation_status(self, **params):
        return Brand.create_external_vetting(self.id, **params)
