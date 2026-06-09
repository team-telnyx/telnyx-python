# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["RemediationCreateParams"]


class RemediationCreateParams(TypedDict, total=False):
    call_purpose: Required[str]
    """How the numbers are used (free text)."""

    phone_numbers: Required[SequenceNotStr[str]]
    """Phone numbers in E.164 format.

    Each must belong to this enterprise. Maximum 2,000 per request.
    """

    contact_email: str
    """Optional contact email for this remediation request."""

    webhook_url: str
    """Optional https:// URL for status notifications."""
