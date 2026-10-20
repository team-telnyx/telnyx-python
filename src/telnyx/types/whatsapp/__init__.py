# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .signup_list_params import SignupListParams as SignupListParams
from .template_list_params import TemplateListParams as TemplateListParams
from .template_create_params import TemplateCreateParams as TemplateCreateParams
from .phone_number_get_params import PhoneNumberGetParams as PhoneNumberGetParams
from .user_data_update_params import UserDataUpdateParams as UserDataUpdateParams
from .phone_number_list_params import PhoneNumberListParams as PhoneNumberListParams
from .hosted_signup_list_params import HostedSignupListParams as HostedSignupListParams
from .phone_number_verify_params import PhoneNumberVerifyParams as PhoneNumberVerifyParams
from .hosted_signup_create_params import HostedSignupCreateParams as HostedSignupCreateParams
from .business_account_list_params import BusinessAccountListParams as BusinessAccountListParams
from .whatsapp_template_body_component_param import (
    WhatsappTemplateBodyComponentParam as WhatsappTemplateBodyComponentParam,
)
from .phone_number_resend_verification_params import (
    PhoneNumberResendVerificationParams as PhoneNumberResendVerificationParams,
)
from .whatsapp_template_footer_component_param import (
    WhatsappTemplateFooterComponentParam as WhatsappTemplateFooterComponentParam,
)
from .whatsapp_template_header_component_param import (
    WhatsappTemplateHeaderComponentParam as WhatsappTemplateHeaderComponentParam,
)
from .whatsapp_template_buttons_component_param import (
    WhatsappTemplateButtonsComponentParam as WhatsappTemplateButtonsComponentParam,
)
from .whatsapp_template_carousel_component_param import (
    WhatsappTemplateCarouselComponentParam as WhatsappTemplateCarouselComponentParam,
)
from .phone_number_retrieve_conversation_window_params import (
    PhoneNumberRetrieveConversationWindowParams as PhoneNumberRetrieveConversationWindowParams,
)

if TYPE_CHECKING:
    from .whatsapp_user_data import WhatsappUserData as WhatsappUserData
    from .signup_list_response import SignupListResponse as SignupListResponse
    from .template_create_response import TemplateCreateResponse as TemplateCreateResponse
    from .phone_number_get_response import PhoneNumberGetResponse as PhoneNumberGetResponse
    from .user_data_update_response import UserDataUpdateResponse as UserDataUpdateResponse
    from .phone_number_list_response import PhoneNumberListResponse as PhoneNumberListResponse
    from .hosted_signup_list_response import HostedSignupListResponse as HostedSignupListResponse
    from .user_data_retrieve_response import UserDataRetrieveResponse as UserDataRetrieveResponse
    from .hosted_signup_create_response import HostedSignupCreateResponse as HostedSignupCreateResponse
    from .business_account_list_response import BusinessAccountListResponse as BusinessAccountListResponse
    from .hosted_signup_retrieve_response import HostedSignupRetrieveResponse as HostedSignupRetrieveResponse
    from .signup_retrieve_status_response import SignupRetrieveStatusResponse as SignupRetrieveStatusResponse
    from .business_account_retrieve_response import BusinessAccountRetrieveResponse as BusinessAccountRetrieveResponse
    from .phone_number_retrieve_phone_number_response import (
        PhoneNumberRetrievePhoneNumberResponse as PhoneNumberRetrievePhoneNumberResponse,
    )
    from .phone_number_retrieve_conversation_window_response import (
        PhoneNumberRetrieveConversationWindowResponse as PhoneNumberRetrieveConversationWindowResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "BusinessAccountRetrieveResponse":
        from .business_account_retrieve_response import BusinessAccountRetrieveResponse

        return BusinessAccountRetrieveResponse
    if name == "BusinessAccountListResponse":
        from .business_account_list_response import BusinessAccountListResponse

        return BusinessAccountListResponse
    if name == "TemplateCreateResponse":
        from .template_create_response import TemplateCreateResponse

        return TemplateCreateResponse
    if name == "PhoneNumberListResponse":
        from .phone_number_list_response import PhoneNumberListResponse

        return PhoneNumberListResponse
    if name == "PhoneNumberGetResponse":
        from .phone_number_get_response import PhoneNumberGetResponse

        return PhoneNumberGetResponse
    if name == "PhoneNumberRetrieveConversationWindowResponse":
        from .phone_number_retrieve_conversation_window_response import PhoneNumberRetrieveConversationWindowResponse

        return PhoneNumberRetrieveConversationWindowResponse
    if name == "PhoneNumberRetrievePhoneNumberResponse":
        from .phone_number_retrieve_phone_number_response import PhoneNumberRetrievePhoneNumberResponse

        return PhoneNumberRetrievePhoneNumberResponse
    if name == "WhatsappUserData":
        from .whatsapp_user_data import WhatsappUserData

        return WhatsappUserData
    if name == "UserDataRetrieveResponse":
        from .user_data_retrieve_response import UserDataRetrieveResponse

        return UserDataRetrieveResponse
    if name == "UserDataUpdateResponse":
        from .user_data_update_response import UserDataUpdateResponse

        return UserDataUpdateResponse
    if name == "SignupListResponse":
        from .signup_list_response import SignupListResponse

        return SignupListResponse
    if name == "SignupRetrieveStatusResponse":
        from .signup_retrieve_status_response import SignupRetrieveStatusResponse

        return SignupRetrieveStatusResponse
    if name == "HostedSignupCreateResponse":
        from .hosted_signup_create_response import HostedSignupCreateResponse

        return HostedSignupCreateResponse
    if name == "HostedSignupRetrieveResponse":
        from .hosted_signup_retrieve_response import HostedSignupRetrieveResponse

        return HostedSignupRetrieveResponse
    if name == "HostedSignupListResponse":
        from .hosted_signup_list_response import HostedSignupListResponse

        return HostedSignupListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
