# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessagingHostedNumberOrderCheckEligibilityResponse", "PhoneNumber"]


class PhoneNumber(BaseModel):
    detail: Optional[str] = None
    """Detailed information about the eligibility status."""

    eligible: Optional[bool] = None
    """Whether the phone number is eligible for hosted messaging."""

    eligible_status: Optional[
        Literal[
            "NUMBER_CAN_NOT_BE_REPEATED",
            "NUMBER_CAN_NOT_BE_VALIDATED",
            "NUMBER_CAN_NOT_BE_WIRELESS",
            "NUMBER_CAN_NOT_BE_ACTIVE_IN_YOUR_ACCOUNT",
            "NUMBER_CAN_NOT_HOSTED_WITH_A_TELNYX_SUBSCRIBER",
            "NUMBER_CAN_NOT_BE_IN_TELNYX",
            "NUMBER_IS_NOT_A_US_NUMBER",
            "NUMBER_IS_NOT_A_VALID_ROUTING_NUMBER",
            "NUMBER_IS_NOT_IN_E164_FORMAT",
            "BILLING_ACCOUNT_CHECK_FAILED",
            "BILLING_ACCOUNT_IS_ABOLISHED",
            "ELIGIBLE",
        ]
    ] = None
    """The eligibility status of the phone number."""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class MessagingHostedNumberOrderCheckEligibilityResponse(BaseModel):
    phone_numbers: Optional[List[PhoneNumber]] = None
    """List of phone numbers with their eligibility status."""
