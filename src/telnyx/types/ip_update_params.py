# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPUpdateParams"]


class IPUpdateParams(TypedDict, total=False):
    ip_address: Required[str]
    """IP adddress represented by this resource."""

    connection_id: str
    """ID of the IP Connection to which this IP should be attached."""

    port: int
    """Port to use when connecting to this IP."""
