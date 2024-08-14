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
@nested_resource_class_methods(
    "by_id", path="{verification_id}/actions/verify", operations=["create"]
)
@nested_resource_class_methods(
    "by_phone_number", path="by_phone_number/{phone_number}/actions/verify", operations=["create"]
)
class Verification(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "verification"

    @classmethod
    def sms(cls, **params):
        return Verification.create_sms(None, **params)

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
    def by_phone_number(cls, phone_number, **params):
        return Verification.create_by_phone_number(phone_number, **params)
