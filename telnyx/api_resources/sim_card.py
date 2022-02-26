from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("enable", path="actions/enable", operations=["create"])
@nested_resource_class_methods("disable", path="actions/disable", operations=["create"])
@nested_resource_class_methods(
    "register", path="/v2/actions/register/sim_cards", operations=["create"]
)
@nested_resource_class_methods(
    "set_standby", path="actions/set_standby", operations=["create"]
)
@nested_resource_class_methods(
    "remove_public_ip", path="actions/remove_public_ip", operations=["create"]
)
@nested_resource_class_methods(
    "set_public_ip", path="actions/set_public_ip", operations=["create"]
)
@nested_resource_class_methods(
    "wireless_logs", path="wireless_connectivity_logs", operations=["list"]
)
class SIMCard(
    ListableAPIResource,
    UpdateableAPIResource,
    CreateableAPIResource,
    DeletableAPIResource,
):
    OBJECT_NAME = "sim_card"

    def enable(self, **params):
        return SIMCard.create_enable(self.id, **params)

    def disable(self, **params):
        return SIMCard.create_disable(self.id, **params)

    def set_standby(self, **params):
        return SIMCard.create_set_standby(self.id, **params)

    def remove_public_ip(self, **params):
        return SIMCard.create_remove_public_ip(self.id, **params)

    def set_public_ip(self, **params):
        return SIMCard.create_set_public_ip(self.id, **params)

    """ deprecated?
    def wireless_logs(self, **params):
        return SIMCard.list_wireless_logs(self.id, **params)
    """

    @classmethod
    def register(cls, **params):
        return SIMCard.create_register(None, **params)
