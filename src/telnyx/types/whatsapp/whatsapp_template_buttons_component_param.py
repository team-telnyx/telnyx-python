# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WhatsappTemplateButtonsComponentParam", "Button"]


class Button(TypedDict, total=False):
    type: Required[Literal["URL", "PHONE_NUMBER", "QUICK_REPLY", "OTP", "COPY_CODE", "FLOW"]]

    autofill_text: str
    """Custom autofill button text for ONE_TAP OTP buttons."""

    example: SequenceNotStr[str]
    """Sample values for URL variable."""

    flow_action: Literal["navigate", "data_exchange"]
    """Flow action type for FLOW-type buttons."""

    flow_id: str
    """Flow ID for FLOW-type buttons."""

    navigate_screen: str
    """Target screen name for FLOW buttons with navigate action."""

    otp_type: Literal["COPY_CODE", "ONE_TAP"]

    package_name: str
    """Android package name. Required for ONE_TAP OTP buttons."""

    phone_number: str
    """Phone number in E.164 format."""

    signature_hash: str
    """Android app signing key hash. Required for ONE_TAP OTP buttons."""

    text: str
    """Button label text.

    Maximum 25 characters. Required for URL, PHONE_NUMBER, and QUICK_REPLY buttons.
    Not required for OTP buttons (Meta supplies the label).
    """

    url: str
    """URL for URL-type buttons. Supports one variable ({{1}})."""

    zero_tap_terms_accepted: bool
    """Whether zero-tap terms have been accepted."""


class WhatsappTemplateButtonsComponentParam(TypedDict, total=False):
    """Optional interactive buttons. Maximum 3 buttons per template."""

    buttons: Required[Iterable[Button]]
    """Array of button objects. Meta supports various combinations of button types."""

    type: Required[Literal["BUTTONS"]]
