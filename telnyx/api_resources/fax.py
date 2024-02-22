from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("refresh", path="actions/refresh", operations=["create"])
@nested_resource_class_methods("cancel", path="actions/cancel", operations=["create"])
class ProgrammableFaxCommand(
    CreateableAPIResource, DeletableAPIResource, ListableAPIResource
):
    OBJECT_NAME = "programmable_fax_command"

    def refresh(self, **params):
        return self.create_refresh(**params)

    def cancel(self, **params):
        return self.create_cancel(**params)
