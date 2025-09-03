# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["MessagingHostedNumberOrderCreateVerificationCodesParams"]


class MessagingHostedNumberOrderCreateVerificationCodesParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]

    verification_method: Required[Literal["sms", "call", "flashcall"]]
