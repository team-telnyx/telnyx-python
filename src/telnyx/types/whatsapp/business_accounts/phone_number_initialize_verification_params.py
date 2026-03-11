# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PhoneNumberInitializeVerificationParams"]


class PhoneNumberInitializeVerificationParams(TypedDict, total=False):
    display_name: Required[str]

    phone_number: Required[str]

    language: str

    verification_method: Literal["sms", "voice"]
