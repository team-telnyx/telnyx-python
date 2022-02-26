from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "comments", path="comments", operations=["create", "list"], pluralize_path=False
)
@nested_resource_class_methods(
    "supporting_documents",
    path="supporting_documents",
    operations=["create", "list"],
    pluralize_path=False,
)
class PortOut(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "portout"

    def list_comments(self, **params):
        return PortOut.list_comments(self.id, **params)

    def create_comments(self, **params):
        return PortOut.create_comments(self, **params)

    def list_supporting_documents(self, **params):
        return PortOut.list_supporting_documents(self.id, **params)

    def create_supporting_documents(self, **params):
        return PortOut.create_supporting_documents(self, **params)
