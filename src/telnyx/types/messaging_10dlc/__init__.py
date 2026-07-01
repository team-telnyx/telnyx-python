# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .vertical import Vertical as Vertical
from .entity_type import EntityType as EntityType
from .task_status import TaskStatus as TaskStatus
from .stock_exchange import StockExchange as StockExchange
from .brand_list_params import BrandListParams as BrandListParams
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .alt_business_id_type import AltBusinessIDType as AltBusinessIDType
from .campaign_list_params import CampaignListParams as CampaignListParams
from .brand_identity_status import BrandIdentityStatus as BrandIdentityStatus
from .campaign_update_params import CampaignUpdateParams as CampaignUpdateParams
from .brand_retrieve_response import BrandRetrieveResponse as BrandRetrieveResponse
from .brand_verify_sms_otp_params import BrandVerifySMSOtpParams as BrandVerifySMSOtpParams
from .brand_trigger_sms_otp_params import BrandTriggerSMSOtpParams as BrandTriggerSMSOtpParams
from .partner_campaign_list_params import PartnerCampaignListParams as PartnerCampaignListParams
from .campaign_submit_appeal_params import CampaignSubmitAppealParams as CampaignSubmitAppealParams
from .campaign_builder_submit_params import CampaignBuilderSubmitParams as CampaignBuilderSubmitParams
from .partner_campaign_update_params import PartnerCampaignUpdateParams as PartnerCampaignUpdateParams
from .campaign_accept_sharing_response import CampaignAcceptSharingResponse as CampaignAcceptSharingResponse
from .phone_number_campaign_list_params import PhoneNumberCampaignListParams as PhoneNumberCampaignListParams
from .phone_number_campaign_create_params import PhoneNumberCampaignCreateParams as PhoneNumberCampaignCreateParams
from .phone_number_campaign_update_params import PhoneNumberCampaignUpdateParams as PhoneNumberCampaignUpdateParams
from .brand_get_sms_otp_by_reference_params import BrandGetSMSOtpByReferenceParams as BrandGetSMSOtpByReferenceParams
from .campaign_get_operation_status_response import (
    CampaignGetOperationStatusResponse as CampaignGetOperationStatusResponse,
)
from .partner_campaign_list_shared_by_me_params import (
    PartnerCampaignListSharedByMeParams as PartnerCampaignListSharedByMeParams,
)
from .phone_number_assignment_by_profile_assign_params import (
    PhoneNumberAssignmentByProfileAssignParams as PhoneNumberAssignmentByProfileAssignParams,
)
from .partner_campaign_retrieve_sharing_status_response import (
    PartnerCampaignRetrieveSharingStatusResponse as PartnerCampaignRetrieveSharingStatusResponse,
)
from .phone_number_assignment_by_profile_list_phone_number_status_params import (
    PhoneNumberAssignmentByProfileListPhoneNumberStatusParams as PhoneNumberAssignmentByProfileListPhoneNumberStatusParams,
)
from .phone_number_assignment_by_profile_retrieve_phone_number_status_params import (
    PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusParams as PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusParams,
)

if TYPE_CHECKING:
    from .telnyx_brand import TelnyxBrand as TelnyxBrand
    from .brand_list_response import BrandListResponse as BrandListResponse
    from .telnyx_campaign_csp import TelnyxCampaignCsp as TelnyxCampaignCsp
    from .brand_sms_otp_status import BrandSMSOtpStatus as BrandSMSOtpStatus
    from .phone_number_campaign import PhoneNumberCampaign as PhoneNumberCampaign
    from .campaign_list_response import CampaignListResponse as CampaignListResponse
    from .campaign_sharing_status import CampaignSharingStatus as CampaignSharingStatus
    from .brand_optional_attributes import BrandOptionalAttributes as BrandOptionalAttributes
    from .telnyx_downstream_campaign import TelnyxDownstreamCampaign as TelnyxDownstreamCampaign
    from .brand_get_feedback_response import BrandGetFeedbackResponse as BrandGetFeedbackResponse
    from .campaign_deactivate_response import CampaignDeactivateResponse as CampaignDeactivateResponse
    from .brand_trigger_sms_otp_response import BrandTriggerSMSOtpResponse as BrandTriggerSMSOtpResponse
    from .campaign_submit_appeal_response import CampaignSubmitAppealResponse as CampaignSubmitAppealResponse
    from .profile_assignment_phone_numbers import ProfileAssignmentPhoneNumbers as ProfileAssignmentPhoneNumbers
    from .campaign_get_mno_metadata_response import CampaignGetMnoMetadataResponse as CampaignGetMnoMetadataResponse
    from .campaign_get_sharing_status_response import (
        CampaignGetSharingStatusResponse as CampaignGetSharingStatusResponse,
    )
    from .partner_campaign_list_shared_by_me_response import (
        PartnerCampaignListSharedByMeResponse as PartnerCampaignListSharedByMeResponse,
    )
    from .phone_number_assignment_by_profile_assign_response import (
        PhoneNumberAssignmentByProfileAssignResponse as PhoneNumberAssignmentByProfileAssignResponse,
    )
    from .phone_number_assignment_by_profile_retrieve_status_response import (
        PhoneNumberAssignmentByProfileRetrieveStatusResponse as PhoneNumberAssignmentByProfileRetrieveStatusResponse,
    )
    from .phone_number_assignment_by_profile_list_phone_number_status_response import (
        PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse as PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse,
    )
    from .phone_number_assignment_by_profile_retrieve_phone_number_status_response import (
        PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse as PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "BrandOptionalAttributes":
        from .brand_optional_attributes import BrandOptionalAttributes

        return BrandOptionalAttributes
    if name == "BrandSMSOtpStatus":
        from .brand_sms_otp_status import BrandSMSOtpStatus

        return BrandSMSOtpStatus
    if name == "TelnyxBrand":
        from .telnyx_brand import TelnyxBrand

        return TelnyxBrand
    if name == "BrandListResponse":
        from .brand_list_response import BrandListResponse

        return BrandListResponse
    if name == "BrandGetFeedbackResponse":
        from .brand_get_feedback_response import BrandGetFeedbackResponse

        return BrandGetFeedbackResponse
    if name == "BrandTriggerSMSOtpResponse":
        from .brand_trigger_sms_otp_response import BrandTriggerSMSOtpResponse

        return BrandTriggerSMSOtpResponse
    if name == "CampaignSharingStatus":
        from .campaign_sharing_status import CampaignSharingStatus

        return CampaignSharingStatus
    if name == "TelnyxCampaignCsp":
        from .telnyx_campaign_csp import TelnyxCampaignCsp

        return TelnyxCampaignCsp
    if name == "CampaignListResponse":
        from .campaign_list_response import CampaignListResponse

        return CampaignListResponse
    if name == "CampaignDeactivateResponse":
        from .campaign_deactivate_response import CampaignDeactivateResponse

        return CampaignDeactivateResponse
    if name == "CampaignGetMnoMetadataResponse":
        from .campaign_get_mno_metadata_response import CampaignGetMnoMetadataResponse

        return CampaignGetMnoMetadataResponse
    if name == "CampaignGetSharingStatusResponse":
        from .campaign_get_sharing_status_response import CampaignGetSharingStatusResponse

        return CampaignGetSharingStatusResponse
    if name == "CampaignSubmitAppealResponse":
        from .campaign_submit_appeal_response import CampaignSubmitAppealResponse

        return CampaignSubmitAppealResponse
    if name == "TelnyxDownstreamCampaign":
        from .telnyx_downstream_campaign import TelnyxDownstreamCampaign

        return TelnyxDownstreamCampaign
    if name == "PartnerCampaignListSharedByMeResponse":
        from .partner_campaign_list_shared_by_me_response import PartnerCampaignListSharedByMeResponse

        return PartnerCampaignListSharedByMeResponse
    if name == "PhoneNumberCampaign":
        from .phone_number_campaign import PhoneNumberCampaign

        return PhoneNumberCampaign
    if name == "ProfileAssignmentPhoneNumbers":
        from .profile_assignment_phone_numbers import ProfileAssignmentPhoneNumbers

        return ProfileAssignmentPhoneNumbers
    if name == "PhoneNumberAssignmentByProfileAssignResponse":
        from .phone_number_assignment_by_profile_assign_response import PhoneNumberAssignmentByProfileAssignResponse

        return PhoneNumberAssignmentByProfileAssignResponse
    if name == "PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse":
        from .phone_number_assignment_by_profile_list_phone_number_status_response import (
            PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse,
        )

        return PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse
    if name == "PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse":
        from .phone_number_assignment_by_profile_retrieve_phone_number_status_response import (
            PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
        )

        return PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse
    if name == "PhoneNumberAssignmentByProfileRetrieveStatusResponse":
        from .phone_number_assignment_by_profile_retrieve_status_response import (
            PhoneNumberAssignmentByProfileRetrieveStatusResponse,
        )

        return PhoneNumberAssignmentByProfileRetrieveStatusResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
