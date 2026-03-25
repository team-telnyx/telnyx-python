# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NumberRetrieveParams"]


class NumberRetrieveParams(TypedDict, total=False):
    enterprise_id: Required[str]

    fresh: bool
    """When true, fetches fresh reputation data (incurs API cost).

    When false, returns cached data.
    """
