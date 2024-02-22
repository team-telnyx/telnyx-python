from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "file_upload", path="actions/file_upload", operations=["create"]
)
class MessagingHostedNumber(
    CreateableAPIResource, DeletableAPIResource, ListableAPIResource
):
    OBJECT_NAME = "messaging_hosted_number"

    def file_upload(self, **params):
        return self.create_file_upload(**params)
