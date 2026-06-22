# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WhatsappTemplateFooterComponentParam"]


class WhatsappTemplateFooterComponentParam(TypedDict, total=False):
    """Optional footer displayed at the bottom of the message.

    Does not support variables.
    """

    type: Required[Literal["FOOTER"]]

    code_expiration_minutes: int
    """OTP code expiration time in minutes.

    Used in AUTHENTICATION template footers instead of free-form text.
    """

    text: str
    """Footer text. Maximum 60 characters. For non-authentication templates."""
