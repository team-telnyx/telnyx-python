# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionRefreshClientTokenParams"]


class ActionRefreshClientTokenParams(TypedDict, total=False):
    refresh_token: Required[str]

    token_ttl_secs: int
    """
    The time to live in seconds of the Client Token, after that time the Client
    Token is invalid and can't be used to join a Room.
    """
