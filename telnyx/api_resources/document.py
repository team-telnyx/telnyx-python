from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("download", path="download", operations=["list"])
class Document(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "document"

    def download(self, **params):
        return Document.list_download(self.name, **params)


class DocumentLink(ListableAPIResource):
    OBJECT_NAME = "document_link"
