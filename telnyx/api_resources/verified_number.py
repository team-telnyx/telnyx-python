from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("verify", path="actions/verify", operations=["create"])
class VerifiedNumber(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "verified_number"

    def verify(self, **params):
        return self.create_verify(**params)
