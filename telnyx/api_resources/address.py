from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "validate", path="actions/validate", operations=["create"]
)
@nested_resource_class_methods(
    "accept_suggestions", path="actions/accept_suggestions", operations=["create"]
)
class Address(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "address"

    @classmethod
    def class_url(cls):
        return "/v2/addresses"

    def validate(self, **params):
        return self.create_validate(**params)

    def accept_suggestions(self, **params):
        return self.create_accept_suggestions(**params)
