from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "activate", path="actions/activate", operations=["create"]
)
@nested_resource_class_methods(
    "deactivate", path="actions/deactivate", operations=["create"]
)
@nested_resource_class_methods(
    "register", path="/v2/actions/register/sim_cards", operations=["create"]
)
class SIMCard(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "sim_card"

    def activate(self, **params):
        return SIMCard.create_activate(self.id, **params)

    def deactivate(self, **params):
        return SIMCard.create_deactivate(self.id, **params)

    @classmethod
    def register(cls, **params):
        return SIMCard.create_register(None, **params)
