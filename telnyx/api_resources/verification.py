from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "sms", path="/v2/verifications/sms", operations=["create"]
)
@nested_resource_class_methods(
    "psd2", path="/v2/verifications/psd2", operations=["create"]
)
@nested_resource_class_methods(
    "call", path="/v2/verifications/call", operations=["create"]
)
@nested_resource_class_methods(
    "flashcall", path="/v2/verifications/flashcall", operations=["create"]
)
@nested_resource_class_methods(
    "whatsapp", path="/v2/verifications/whatsapp", operations=["create"]
)
class Verification(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "verification"

    def verify_by_phone_number(self, code, phone_number, verify_profile_id):
        response, api_key = self.request(
            method="post",
            url="/v2/verifications/by_phone_number/{}/actions/verify".format(
                phone_number
            ),
            params={"code": code, "verify_profile_id": verify_profile_id},
        )

    def verify_verification_code_by_id(self, verification_id, code):
        response, api_key = self.request(
            method="post",
            url="/v2/verifications/{}/actions/verify".format(verification_id),
            params={"code": code}
        )
        return response, api_key

    @classmethod
    def psd2(cls, **params):
        return Verification.create_psd2(None, **params)

    @classmethod
    def call(cls, **params):
        return Verification.create_call(None, **params)

    @classmethod
    def flashcall(cls, **params):
        return Verification.create_flashcall(None, **params)

    @classmethod
    def whatsapp(cls, **params):
        return Verification.create_whatsapp(None, **params)

    @classmethod
    def email(cls, **params):
        return Verification.create_email(None, **params)

    @classmethod
    def push(cls, **params):
        return Verification.create_push(None, **params)

    @classmethod
    def smart(cls, **params):
        return Verification.create_smart(None, **params)
