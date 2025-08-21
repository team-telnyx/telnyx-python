# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Verification"]


class Verification(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    custom_code: Optional[str] = None
    """Send a self-generated numeric code to the end-user"""

    phone_number: Optional[str] = None
    """+E164 formatted phone number."""

    record_type: Optional[Literal["verification"]] = None
    """The possible verification record types."""

    status: Optional[Literal["pending", "accepted", "invalid", "expired", "error"]] = None
    """The possible statuses of the verification request."""

    timeout_secs: Optional[int] = None
    """This is the number of seconds before the code of the request is expired.

    Once this request has expired, the code will no longer verify the user. Note:
    this will override the `default_verification_timeout_secs` on the Verify
    profile.
    """

    type: Optional[Literal["sms", "call", "flashcall"]] = None
    """The possible types of verification."""

    updated_at: Optional[str] = None

    verify_profile_id: Optional[str] = None
    """The identifier of the associated Verify profile."""
