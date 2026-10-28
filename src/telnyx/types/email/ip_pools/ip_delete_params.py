# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPDeleteParams"]


class IPDeleteParams(TypedDict, total=False):
    id: Required[str]

    drain: bool
    """Set together with `force=true` to remove the last IP in the pool.

    Acknowledges that mail routed to the emptied pool is held until the pool has a
    sendable IP again.
    """

    force: bool
    """Set together with `drain=true` to remove the last IP in the pool.

    Either flag alone has no effect.
    """
