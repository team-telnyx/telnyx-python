# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionGenerateJoinClientTokenParams"]


class ActionGenerateJoinClientTokenParams(TypedDict, total=False):
    refresh_token_ttl_secs: int
    """
    The time to live in seconds of the Refresh Token, after that time the Refresh
    Token is invalid and can't be used to refresh Client Token.
    """

    token_ttl_secs: int
    """
    The time to live in seconds of the Client Token, after that time the Client
    Token is invalid and can't be used to join a Room.
    """
