from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("disable", path="actions/disable", operations=["create"])
@nested_resource_class_methods(
    "delete_network_preferences",
    path="actions/delete_network_preferences",
    operations=["create"],
)
@nested_resource_class_methods(
    "bulk_set_network_preferences",
    path="actions/bulk_set_network_preferences",
    operations=["create"],
)
@nested_resource_class_methods(
    "validate_registration_codes",
    path="actions/validate_registration_codes",
    operations=["create"],
)
@nested_resource_class_methods(
    "set_public_ip", path="actions/set_public_ip", operations=["create"]
)
@nested_resource_class_methods(
    "set_network_preferences",
    path="actions/set_network_preferences",
    operations=["create"],
)
@nested_resource_class_methods("enable", path="actions/enable", operations=["create"])
@nested_resource_class_methods(
    "set_standby", path="actions/set_standby", operations=["create"]
)
@nested_resource_class_methods(
    "remove_public_ip", path="actions/remove_public_ip", operations=["create"]
)
@nested_resource_class_methods(
    "bulk_set_public_ips", path="actions/bulk_set_public_ips", operations=["create"]
)
@nested_resource_class_methods(
    "register", path="/v2/actions/register/sim_cards", operations=["create"]
)
class SIMCard(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "sim_card"

    def disable(self, **params):
        return self.create_disable(**params)

    def delete_network_preferences(self, **params):
        return self.create_delete_network_preferences(**params)

    def bulk_set_network_preferences(self, **params):
        return self.create_bulk_set_network_preferences(**params)

    def validate_registration_codes(self, **params):
        return self.create_validate_registration_codes(**params)

    def set_public_ip(self, **params):
        return self.create_set_public_ip(**params)

    def set_network_preferences(self, **params):
        return self.create_set_network_preferences(**params)

    def enable(self, **params):
        return self.create_enable(**params)

    def set_standby(self, **params):
        return self.create_set_standby(**params)

    def remove_public_ip(self, **params):
        return self.create_remove_public_ip(**params)

    def bulk_set_public_ips(self, **params):
        return self.create_bulk_set_public_ips(**params)

    @classmethod
    def register(cls, **params):
        return SIMCard.create_register(None, **params)
