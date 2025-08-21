# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationTriggerFlashcallParams"]


class VerificationTriggerFlashcallParams(TypedDict, total=False):
    phone_number: Required[str]
    """+E164 formatted phone number."""

    verify_profile_id: Required[str]
    """The identifier of the associated Verify profile."""

    timeout_secs: int
    """The number of seconds the verification code is valid for."""
