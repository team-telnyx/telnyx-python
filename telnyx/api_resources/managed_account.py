from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("enable", path="actions/enable", operations=["create"])
@nested_resource_class_methods("disable", path="actions/disable", operations=["create"])
class ManagedAccount(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "managed_account"

    def enable(self, **params):
        return self.create_enable(**params)

    def disable(self, **params):
        return self.create_disable(**params)
