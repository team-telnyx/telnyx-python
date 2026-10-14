# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .agent_input_param import AgentInputParam as AgentInputParam
from .loa_render_params import LoaRenderParams as LoaRenderParams
from .loa_update_params import LoaUpdateParams as LoaUpdateParams
from .number_list_params import NumberListParams as NumberListParams
from .remediation_status import RemediationStatus as RemediationStatus
from .number_refresh_params import NumberRefreshParams as NumberRefreshParams
from .number_retrieve_params import NumberRetrieveParams as NumberRetrieveParams
from .number_associate_params import NumberAssociateParams as NumberAssociateParams
from .remediation_list_params import RemediationListParams as RemediationListParams
from .reputation_number_source import ReputationNumberSource as ReputationNumberSource
from .remediation_create_params import RemediationCreateParams as RemediationCreateParams
from .reputation_ownership_status import ReputationOwnershipStatus as ReputationOwnershipStatus
from .external_verification_status import ExternalVerificationStatus as ExternalVerificationStatus
from .number_ownership_confirm_params import NumberOwnershipConfirmParams as NumberOwnershipConfirmParams
from .external_verification_create_params import ExternalVerificationCreateParams as ExternalVerificationCreateParams

if TYPE_CHECKING:
    from .remediation_request import RemediationRequest as RemediationRequest
    from .number_refresh_response import NumberRefreshResponse as NumberRefreshResponse
    from .reputation_phone_number import ReputationPhoneNumber as ReputationPhoneNumber
    from .remediation_list_response import RemediationListResponse as RemediationListResponse
    from .remediation_request_wrapped import RemediationRequestWrapped as RemediationRequestWrapped
    from .reputation_phone_number_list import ReputationPhoneNumberList as ReputationPhoneNumberList
    from .external_verification_wrapped import ExternalVerificationWrapped as ExternalVerificationWrapped
    from .remediation_per_number_results import RemediationPerNumberResults as RemediationPerNumberResults
    from .number_retrieve_ownership_response import NumberRetrieveOwnershipResponse as NumberRetrieveOwnershipResponse
    from .reputation_phone_number_with_reputation import (
        ReputationPhoneNumberWithReputation as ReputationPhoneNumberWithReputation,
    )


def __getattr__(name: str) -> Any:
    if name == "ReputationPhoneNumber":
        from .reputation_phone_number import ReputationPhoneNumber

        return ReputationPhoneNumber
    if name == "ReputationPhoneNumberList":
        from .reputation_phone_number_list import ReputationPhoneNumberList

        return ReputationPhoneNumberList
    if name == "ReputationPhoneNumberWithReputation":
        from .reputation_phone_number_with_reputation import ReputationPhoneNumberWithReputation

        return ReputationPhoneNumberWithReputation
    if name == "NumberRefreshResponse":
        from .number_refresh_response import NumberRefreshResponse

        return NumberRefreshResponse
    if name == "NumberRetrieveOwnershipResponse":
        from .number_retrieve_ownership_response import NumberRetrieveOwnershipResponse

        return NumberRetrieveOwnershipResponse
    if name == "RemediationPerNumberResults":
        from .remediation_per_number_results import RemediationPerNumberResults

        return RemediationPerNumberResults
    if name == "RemediationRequest":
        from .remediation_request import RemediationRequest

        return RemediationRequest
    if name == "RemediationRequestWrapped":
        from .remediation_request_wrapped import RemediationRequestWrapped

        return RemediationRequestWrapped
    if name == "RemediationListResponse":
        from .remediation_list_response import RemediationListResponse

        return RemediationListResponse
    if name == "ExternalVerificationWrapped":
        from .external_verification_wrapped import ExternalVerificationWrapped

        return ExternalVerificationWrapped
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
