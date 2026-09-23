# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BotSessionListParams"]


class BotSessionListParams(TypedDict, total=False):
    email: Required[str]
    """Email address associated with the magic link token."""

    portal_redirect_token: Required[str]
    """
    Single-use portal redirect (magic link) token, a UUIDv7 sent to the account
    owner's email.
    """
