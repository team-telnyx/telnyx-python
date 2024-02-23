from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("verify", path="actions/verify", operations=["create"])
class Verify(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "verify"

    def verify(self, **params):
        return self.create_verify(**params)
