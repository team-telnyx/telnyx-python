# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OAuthGrantsParams"]


class OAuthGrantsParams(TypedDict, total=False):
    allowed: Required[bool]
    """Whether the grant is allowed"""

    consent_token: Required[str]
    """Consent token"""
