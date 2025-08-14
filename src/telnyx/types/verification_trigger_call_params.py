# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["VerificationTriggerCallParams"]


class VerificationTriggerCallParams(TypedDict, total=False):
    phone_number: Required[str]
    """+E164 formatted phone number."""

    verify_profile_id: Required[str]
    """The identifier of the associated Verify profile."""

    custom_code: Optional[str]
    """Send a self-generated numeric code to the end-user"""

    timeout_secs: int
    """The number of seconds the verification code is valid for."""
