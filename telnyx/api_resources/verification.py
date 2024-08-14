from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
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
    "verify_by_phone_number", path="by_phone_number/{phone_number}/actions/verify", operations=["create"]
)
@nested_resource_class_methods(
    "verify_by_id", path="actions/verify", operations=["create"]
)
@nested_resource_class_methods(
    "by_phone_number", path="by_phone_number/{phone_number}", operations=["retrieve"]
)
class Verification(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
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
    def verify_by_phone_number(cls, phone_number, **params):
        return Verification.create_verify_by_phone_number(phone_number, **params)

    @classmethod
    def verify_by_id(cls, verification_id, **params):
        return Verification.create_verify_by_id(verification_id, **params)

    @classmethod
    def by_phone_number(cls, phone_number):
        return Verification.retrieve_by_phone_number(phone_number)
