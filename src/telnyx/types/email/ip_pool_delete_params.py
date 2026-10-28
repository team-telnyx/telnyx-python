# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IPPoolDeleteParams"]


class IPPoolDeleteParams(TypedDict, total=False):
    drain: bool
    """Set together with `force=true` to delete a pool that still has IPs.

    Acknowledges deletion while the pool still has members; this flag does not
    reroute already queued messages.
    """

    force: bool
    """Set together with `drain=true` to delete a pool that still has IPs.

    Either flag alone has no effect.
    """
