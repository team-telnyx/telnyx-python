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
from .remediation_create_params import RemediationCreateParams as RemediationCreateParams

if TYPE_CHECKING:
    from .number_refresh_response import NumberRefreshResponse as NumberRefreshResponse
    from .reputation_phone_number import ReputationPhoneNumber as ReputationPhoneNumber
    from .remediation_list_response import RemediationListResponse as RemediationListResponse
    from .remediation_request_wrapped import RemediationRequestWrapped as RemediationRequestWrapped
    from .reputation_phone_number_list import ReputationPhoneNumberList as ReputationPhoneNumberList
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
    if name == "RemediationRequestWrapped":
        from .remediation_request_wrapped import RemediationRequestWrapped

        return RemediationRequestWrapped
    if name == "RemediationListResponse":
        from .remediation_list_response import RemediationListResponse

        return RemediationListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
