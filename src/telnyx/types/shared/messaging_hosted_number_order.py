# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .hosted_number import HostedNumber

__all__ = ["MessagingHostedNumberOrder"]


class MessagingHostedNumberOrder(BaseModel):
    id: Optional[str] = None
    """Resource unique identifier."""

    messaging_profile_id: Optional[str] = None
    """
    Automatically associate the number with this messaging profile ID when the order
    is complete.
    """

    phone_numbers: Optional[List[HostedNumber]] = None

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
