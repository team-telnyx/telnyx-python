# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HostedNumber"]


class HostedNumber(BaseModel):
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
