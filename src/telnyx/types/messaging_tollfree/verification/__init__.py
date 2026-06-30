# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .volume import Volume as Volume
from .url_param import URLParam as URLParam
from .request_list_params import RequestListParams as RequestListParams
from .use_case_categories import UseCaseCategories as UseCaseCategories
from .request_create_params import RequestCreateParams as RequestCreateParams
from .request_update_params import RequestUpdateParams as RequestUpdateParams
from .tf_phone_number_param import TfPhoneNumberParam as TfPhoneNumberParam
from .tf_verification_status import TfVerificationStatus as TfVerificationStatus
from .toll_free_verification_entity_type import TollFreeVerificationEntityType as TollFreeVerificationEntityType
from .request_retrieve_status_history_params import (
    RequestRetrieveStatusHistoryParams as RequestRetrieveStatusHistoryParams,
)

if TYPE_CHECKING:
    from .url import URL as URL
    from .tf_phone_number import TfPhoneNumber as TfPhoneNumber
    from .verification_request_egress import VerificationRequestEgress as VerificationRequestEgress
    from .verification_request_status import VerificationRequestStatus as VerificationRequestStatus
    from .request_retrieve_status_history_response import (
        RequestRetrieveStatusHistoryResponse as RequestRetrieveStatusHistoryResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "TfPhoneNumber":
        from .tf_phone_number import TfPhoneNumber

        return TfPhoneNumber
    if name == "URL":
        from .url import URL

        return URL
    if name == "VerificationRequestEgress":
        from .verification_request_egress import VerificationRequestEgress

        return VerificationRequestEgress
    if name == "VerificationRequestStatus":
        from .verification_request_status import VerificationRequestStatus

        return VerificationRequestStatus
    if name == "RequestRetrieveStatusHistoryResponse":
        from .request_retrieve_status_history_response import RequestRetrieveStatusHistoryResponse

        return RequestRetrieveStatusHistoryResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
