# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPCreateParams"]


class IPCreateParams(TypedDict, total=False):
    dedicated_ip_id: Required[str]
    """The dedicated IP to add.

    It must belong to the account, must not be released, and must not already be in
    a pool.
    """

    weight: int
    """Relative routing weight for this IP in the pool.

    Positive integer; defaults to 100.
    """
