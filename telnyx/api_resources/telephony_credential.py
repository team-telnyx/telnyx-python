from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("token", path="token", operations=["create"])
class TelephonyCredential(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "telephony_credential"
    API_RECORD_TYPE_NAME = "credential"

    def token(self, **params):
        return TelephonyCredential.create_token(self.id, **params)
