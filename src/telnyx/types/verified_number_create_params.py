# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerifiedNumberCreateParams"]


class VerifiedNumberCreateParams(TypedDict, total=False):
    phone_number: Required[str]

    verification_method: Required[Literal["sms", "call"]]
    """Verification method."""
