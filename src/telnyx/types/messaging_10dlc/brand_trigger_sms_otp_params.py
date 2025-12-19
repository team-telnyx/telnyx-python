# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrandTriggerSMSOtpParams"]


class BrandTriggerSMSOtpParams(TypedDict, total=False):
    pin_sms: Required[Annotated[str, PropertyInfo(alias="pinSms")]]
    """SMS message template to send the OTP.

    Must include `@OTP_PIN@` placeholder which will be replaced with the actual PIN
    """

    success_sms: Required[Annotated[str, PropertyInfo(alias="successSms")]]
    """SMS message to send upon successful OTP verification"""
