# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionUploadFileResponse", "Data", "DataPhoneNumber"]


class DataPhoneNumber(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    phone_number: Optional[str] = None
    """The messaging hosted phone number (+E.164 format)"""

    record_type: Optional[str] = None

    status: Optional[
        Literal[
            "deleted",
            "failed",
            "failed_activation",
            "failed_carrier_rejected",
            "failed_ineligible_carrier",
            "failed_number_already_hosted",
            "failed_number_not_found",
            "failed_ownership_verification",
            "failed_timeout",
            "pending",
            "provisioning",
            "successful",
        ]
    ] = None


class Data(BaseModel):
    id: Optional[str] = None
    """Resource unique identifier."""

    messaging_profile_id: Optional[str] = None
    """
    Automatically associate the number with this messaging profile ID when the order
    is complete.
    """

    phone_numbers: Optional[List[DataPhoneNumber]] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[
        Literal[
            "carrier_rejected",
            "compliance_review_failed",
            "deleted",
            "failed",
            "incomplete_documentation",
            "incorrect_billing_information",
            "ineligible_carrier",
            "loa_file_invalid",
            "loa_file_successful",
            "pending",
            "provisioning",
            "successful",
        ]
    ] = None


class ActionUploadFileResponse(BaseModel):
    data: Optional[Data] = None
