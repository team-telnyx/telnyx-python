# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ShortCodeUpdateParams"]


class ShortCodeUpdateParams(TypedDict, total=False):
    messaging_profile_id: Required[str]
    """Unique identifier for a messaging profile."""
