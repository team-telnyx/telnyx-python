# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_share_params import ActionShareParams as ActionShareParams
from .comment_list_params import CommentListParams as CommentListParams
from .comment_create_params import CommentCreateParams as CommentCreateParams
from .activation_job_list_params import ActivationJobListParams as ActivationJobListParams
from .activation_job_update_params import ActivationJobUpdateParams as ActivationJobUpdateParams
from .verification_code_list_params import VerificationCodeListParams as VerificationCodeListParams
from .verification_code_send_params import VerificationCodeSendParams as VerificationCodeSendParams
from .action_requirement_list_params import ActionRequirementListParams as ActionRequirementListParams
from .phone_number_block_list_params import PhoneNumberBlockListParams as PhoneNumberBlockListParams
from .additional_document_list_params import AdditionalDocumentListParams as AdditionalDocumentListParams
from .verification_code_verify_params import VerificationCodeVerifyParams as VerificationCodeVerifyParams
from .phone_number_block_create_params import PhoneNumberBlockCreateParams as PhoneNumberBlockCreateParams
from .additional_document_create_params import AdditionalDocumentCreateParams as AdditionalDocumentCreateParams
from .action_requirement_initiate_params import ActionRequirementInitiateParams as ActionRequirementInitiateParams
from .phone_number_extension_list_params import PhoneNumberExtensionListParams as PhoneNumberExtensionListParams
from .associated_phone_number_list_params import AssociatedPhoneNumberListParams as AssociatedPhoneNumberListParams
from .phone_number_extension_create_params import PhoneNumberExtensionCreateParams as PhoneNumberExtensionCreateParams
from .associated_phone_number_create_params import (
    AssociatedPhoneNumberCreateParams as AssociatedPhoneNumberCreateParams,
)
from .phone_number_configuration_list_params import (
    PhoneNumberConfigurationListParams as PhoneNumberConfigurationListParams,
)
from .phone_number_configuration_create_params import (
    PhoneNumberConfigurationCreateParams as PhoneNumberConfigurationCreateParams,
)

if TYPE_CHECKING:
    from .action_share_response import ActionShareResponse as ActionShareResponse
    from .action_cancel_response import ActionCancelResponse as ActionCancelResponse
    from .porting_orders_comment import PortingOrdersComment as PortingOrdersComment
    from .action_confirm_response import ActionConfirmResponse as ActionConfirmResponse
    from .comment_create_response import CommentCreateResponse as CommentCreateResponse
    from .action_activate_response import ActionActivateResponse as ActionActivateResponse
    from .porting_verification_code import PortingVerificationCode as PortingVerificationCode
    from .porting_action_requirement import PortingActionRequirement as PortingActionRequirement
    from .porting_phone_number_block import PortingPhoneNumberBlock as PortingPhoneNumberBlock
    from .porting_additional_document import PortingAdditionalDocument as PortingAdditionalDocument
    from .activation_job_update_response import ActivationJobUpdateResponse as ActivationJobUpdateResponse
    from .porting_phone_number_extension import PortingPhoneNumberExtension as PortingPhoneNumberExtension
    from .porting_associated_phone_number import PortingAssociatedPhoneNumber as PortingAssociatedPhoneNumber
    from .activation_job_retrieve_response import ActivationJobRetrieveResponse as ActivationJobRetrieveResponse
    from .verification_code_verify_response import VerificationCodeVerifyResponse as VerificationCodeVerifyResponse
    from .phone_number_block_create_response import PhoneNumberBlockCreateResponse as PhoneNumberBlockCreateResponse
    from .phone_number_block_delete_response import PhoneNumberBlockDeleteResponse as PhoneNumberBlockDeleteResponse
    from .porting_phone_number_configuration import PortingPhoneNumberConfiguration as PortingPhoneNumberConfiguration
    from .additional_document_create_response import (
        AdditionalDocumentCreateResponse as AdditionalDocumentCreateResponse,
    )
    from .action_requirement_initiate_response import (
        ActionRequirementInitiateResponse as ActionRequirementInitiateResponse,
    )
    from .phone_number_extension_create_response import (
        PhoneNumberExtensionCreateResponse as PhoneNumberExtensionCreateResponse,
    )
    from .phone_number_extension_delete_response import (
        PhoneNumberExtensionDeleteResponse as PhoneNumberExtensionDeleteResponse,
    )
    from .associated_phone_number_create_response import (
        AssociatedPhoneNumberCreateResponse as AssociatedPhoneNumberCreateResponse,
    )
    from .associated_phone_number_delete_response import (
        AssociatedPhoneNumberDeleteResponse as AssociatedPhoneNumberDeleteResponse,
    )
    from .phone_number_configuration_create_response import (
        PhoneNumberConfigurationCreateResponse as PhoneNumberConfigurationCreateResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "PortingPhoneNumberConfiguration":
        from .porting_phone_number_configuration import PortingPhoneNumberConfiguration

        return PortingPhoneNumberConfiguration
    if name == "PhoneNumberConfigurationCreateResponse":
        from .phone_number_configuration_create_response import PhoneNumberConfigurationCreateResponse

        return PhoneNumberConfigurationCreateResponse
    if name == "ActionActivateResponse":
        from .action_activate_response import ActionActivateResponse

        return ActionActivateResponse
    if name == "ActionCancelResponse":
        from .action_cancel_response import ActionCancelResponse

        return ActionCancelResponse
    if name == "ActionConfirmResponse":
        from .action_confirm_response import ActionConfirmResponse

        return ActionConfirmResponse
    if name == "ActionShareResponse":
        from .action_share_response import ActionShareResponse

        return ActionShareResponse
    if name == "ActivationJobRetrieveResponse":
        from .activation_job_retrieve_response import ActivationJobRetrieveResponse

        return ActivationJobRetrieveResponse
    if name == "ActivationJobUpdateResponse":
        from .activation_job_update_response import ActivationJobUpdateResponse

        return ActivationJobUpdateResponse
    if name == "PortingAdditionalDocument":
        from .porting_additional_document import PortingAdditionalDocument

        return PortingAdditionalDocument
    if name == "AdditionalDocumentCreateResponse":
        from .additional_document_create_response import AdditionalDocumentCreateResponse

        return AdditionalDocumentCreateResponse
    if name == "PortingOrdersComment":
        from .porting_orders_comment import PortingOrdersComment

        return PortingOrdersComment
    if name == "CommentCreateResponse":
        from .comment_create_response import CommentCreateResponse

        return CommentCreateResponse
    if name == "PortingVerificationCode":
        from .porting_verification_code import PortingVerificationCode

        return PortingVerificationCode
    if name == "VerificationCodeVerifyResponse":
        from .verification_code_verify_response import VerificationCodeVerifyResponse

        return VerificationCodeVerifyResponse
    if name == "PortingActionRequirement":
        from .porting_action_requirement import PortingActionRequirement

        return PortingActionRequirement
    if name == "ActionRequirementInitiateResponse":
        from .action_requirement_initiate_response import ActionRequirementInitiateResponse

        return ActionRequirementInitiateResponse
    if name == "PortingAssociatedPhoneNumber":
        from .porting_associated_phone_number import PortingAssociatedPhoneNumber

        return PortingAssociatedPhoneNumber
    if name == "AssociatedPhoneNumberCreateResponse":
        from .associated_phone_number_create_response import AssociatedPhoneNumberCreateResponse

        return AssociatedPhoneNumberCreateResponse
    if name == "AssociatedPhoneNumberDeleteResponse":
        from .associated_phone_number_delete_response import AssociatedPhoneNumberDeleteResponse

        return AssociatedPhoneNumberDeleteResponse
    if name == "PortingPhoneNumberBlock":
        from .porting_phone_number_block import PortingPhoneNumberBlock

        return PortingPhoneNumberBlock
    if name == "PhoneNumberBlockCreateResponse":
        from .phone_number_block_create_response import PhoneNumberBlockCreateResponse

        return PhoneNumberBlockCreateResponse
    if name == "PhoneNumberBlockDeleteResponse":
        from .phone_number_block_delete_response import PhoneNumberBlockDeleteResponse

        return PhoneNumberBlockDeleteResponse
    if name == "PortingPhoneNumberExtension":
        from .porting_phone_number_extension import PortingPhoneNumberExtension

        return PortingPhoneNumberExtension
    if name == "PhoneNumberExtensionCreateResponse":
        from .phone_number_extension_create_response import PhoneNumberExtensionCreateResponse

        return PhoneNumberExtensionCreateResponse
    if name == "PhoneNumberExtensionDeleteResponse":
        from .phone_number_extension_delete_response import PhoneNumberExtensionDeleteResponse

        return PhoneNumberExtensionDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
