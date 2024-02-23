from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "check_registration_status",
    path="actions/check_registration_status",
    operations=["create"],
)
class CredentialConnection(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "credential_connection"

    def check_registration_status(self, **params):
        return self.create_check_registration_status(**params)
