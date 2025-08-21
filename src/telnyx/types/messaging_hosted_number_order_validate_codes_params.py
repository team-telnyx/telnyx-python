# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MessagingHostedNumberOrderValidateCodesParams", "VerificationCode"]


class MessagingHostedNumberOrderValidateCodesParams(TypedDict, total=False):
    verification_codes: Required[Iterable[VerificationCode]]


class VerificationCode(TypedDict, total=False):
    code: Required[str]

    phone_number: Required[str]
