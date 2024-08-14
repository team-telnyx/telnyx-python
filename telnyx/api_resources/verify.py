from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("sms", path="verifications/sms", operations=["create"])
@nested_resource_class_methods("call", path="verifications/call", operations=["create"])
@nested_resource_class_methods("flashcall", path="verifications/flashcall", operations=["create"])
@nested_resource_class_methods("verify", path="verifications/{verification_id}/actions/verify", operations=["create"])
class Verify(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "verify"

    def create_verification_sms(self, **params):
        return self.create_sms(**params)

    def create_verification_call(self, **params):
        return self.create_call(**params)

    def verify_verification_code_by_id(self, verification_id, **params):
        return self.create_verify(verification_id=verification_id, **params)
