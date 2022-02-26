from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("refresh", path="actions/refresh", operations=["create"])
class Fax(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "fax"

    @classmethod
    def class_url(cls):
        return "/v2/faxes"

    def refresh(self, **params):
        return Fax.create_refresh(self.id, **params)
