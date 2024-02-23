from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("refresh", path="actions/refresh", operations=["create"])
@nested_resource_class_methods("cancel", path="actions/cancel", operations=["create"])
class Fax(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "fax"

    @classmethod
    def class_url(cls):
        return "/v2/faxes"

    def refresh(self, **params):
        return self.create_refresh(**params)

    def cancel(self, **params):
        return self.create_cancel(**params)
