# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerifiedNumberCreateParams"]


class VerifiedNumberCreateParams(TypedDict, total=False):
    phone_number: Required[str]

    verification_method: Required[Literal["sms", "call"]]
    """Verification method."""

    extension: str
    """Optional DTMF extension sequence to dial after the call is answered.

    This parameter enables verification of phone numbers behind IVR systems that
    require extension dialing. Valid characters: digits 0-9, letters A-D, symbols \\**
    and #. Pauses: w = 0.5 second pause, W = 1 second pause. Maximum length: 50
    characters. Only works with 'call' verification method.
    """
