from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "provision", path="actions/provision", operations=["create"]
)
class VirtualCrossConnect(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "virtual_cross_connect"

    def provision(self, **params):
        return self.create_provision(**params)
