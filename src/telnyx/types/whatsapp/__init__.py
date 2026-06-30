# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .template_list_params import TemplateListParams as TemplateListParams
from .template_create_params import TemplateCreateParams as TemplateCreateParams
from .user_data_update_params import UserDataUpdateParams as UserDataUpdateParams
from .phone_number_list_params import PhoneNumberListParams as PhoneNumberListParams
from .phone_number_verify_params import PhoneNumberVerifyParams as PhoneNumberVerifyParams
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
    from .template_create_response import TemplateCreateResponse as TemplateCreateResponse
    from .user_data_update_response import UserDataUpdateResponse as UserDataUpdateResponse
    from .phone_number_list_response import PhoneNumberListResponse as PhoneNumberListResponse
    from .user_data_retrieve_response import UserDataRetrieveResponse as UserDataRetrieveResponse
    from .business_account_list_response import BusinessAccountListResponse as BusinessAccountListResponse
    from .business_account_retrieve_response import BusinessAccountRetrieveResponse as BusinessAccountRetrieveResponse
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
    if name == "PhoneNumberRetrieveConversationWindowResponse":
        from .phone_number_retrieve_conversation_window_response import PhoneNumberRetrieveConversationWindowResponse

        return PhoneNumberRetrieveConversationWindowResponse
    if name == "WhatsappUserData":
        from .whatsapp_user_data import WhatsappUserData

        return WhatsappUserData
    if name == "UserDataRetrieveResponse":
        from .user_data_retrieve_response import UserDataRetrieveResponse

        return UserDataRetrieveResponse
    if name == "UserDataUpdateResponse":
        from .user_data_update_response import UserDataUpdateResponse

        return UserDataUpdateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
