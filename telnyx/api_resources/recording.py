from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("delete", path="actions/delete", operations=["delete"])
class Recording(
    DeletableAPIResource,
    ListableAPIResource,
):
    OBJECT_NAME = "recording"

    def delete(self, **params):
        return self.delete_delete(self.id, nested_id=None, **params)
