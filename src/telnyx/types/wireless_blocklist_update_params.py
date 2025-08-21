# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WirelessBlocklistUpdateParams"]


class WirelessBlocklistUpdateParams(TypedDict, total=False):
    name: str
    """The name of the Wireless Blocklist."""

    type: Literal["country", "mcc", "plmn"]
    """The type of wireless blocklist."""

    values: List[str]
    """Values to block. The values here depend on the `type` of Wireless Blocklist."""
