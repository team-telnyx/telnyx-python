# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["VerificationCodeVerifyParams", "VerificationCode"]


class VerificationCodeVerifyParams(TypedDict, total=False):
    verification_codes: Iterable[VerificationCode]


class VerificationCode(TypedDict, total=False):
    code: str

    phone_number: str
