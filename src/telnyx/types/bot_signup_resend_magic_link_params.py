# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BotSignupResendMagicLinkParams"]


class BotSignupResendMagicLinkParams(TypedDict, total=False):
    email: Required[str]
    """Email address of the bot signup account to resend the magic link to."""
