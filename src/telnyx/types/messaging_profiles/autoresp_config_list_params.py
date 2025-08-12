# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AutorespConfigListParams", "CreatedAt", "UpdatedAt"]


class AutorespConfigListParams(TypedDict, total=False):
    country_code: str

    created_at: CreatedAt
    """Consolidated created_at parameter (deepObject style).

    Originally: created_at[gte], created_at[lte]
    """

    updated_at: UpdatedAt
    """Consolidated updated_at parameter (deepObject style).

    Originally: updated_at[gte], updated_at[lte]
    """


class CreatedAt(TypedDict, total=False):
    gte: str

    lte: str


class UpdatedAt(TypedDict, total=False):
    gte: str

    lte: str
