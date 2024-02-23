from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "remove_private_wireless_gateway",
    path="actions/remove_private_wireless_gateway",
    operations=["create"],
)
@nested_resource_class_methods(
    "set_private_wireless_gateway",
    path="actions/set_private_wireless_gateway",
    operations=["create"],
)
class SIMCardGroup(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "sim_card_group"

    def remove_private_wireless_gateway(self, **params):
        return self.create_remove_private_wireless_gateway(**params)

    def set_private_wireless_gateway(self, **params):
        return self.create_set_private_wireless_gateway(**params)
