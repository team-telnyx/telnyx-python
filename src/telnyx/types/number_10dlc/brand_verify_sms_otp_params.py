# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandVerifySMSOtpParams"]


class BrandVerifySMSOtpParams(TypedDict, total=False):
    otp_pin: Required[Annotated[str, PropertyInfo(alias="otpPin")]]
    """The OTP PIN received via SMS"""
