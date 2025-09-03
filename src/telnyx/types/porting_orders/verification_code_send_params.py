# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["VerificationCodeSendParams"]


class VerificationCodeSendParams(TypedDict, total=False):
    phone_numbers: SequenceNotStr[str]

    verification_method: Literal["sms", "call"]
