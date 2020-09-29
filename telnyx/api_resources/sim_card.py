from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("enable", path="actions/enable", operations=["create"])
@nested_resource_class_methods("disable", path="actions/disable", operations=["create"])
@nested_resource_class_methods(
    "register", path="/v2/actions/register/sim_cards", operations=["create"]
)
class SIMCard(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "sim_card"

    def enable(self, **params):
        return SIMCard.create_enable(self.id, **params)

    def disable(self, **params):
        return SIMCard.create_disable(self.id, **params)

    @classmethod
    def register(cls, **params):
        return SIMCard.create_register(None, **params)
