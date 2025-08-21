# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WirelessBlocklistCreateParams"]


class WirelessBlocklistCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the Wireless Blocklist."""

    type: Required[Literal["country", "mcc", "plmn"]]
    """The type of wireless blocklist."""

    values: Required[List[str]]
    """Values to block. The values here depend on the `type` of Wireless Blocklist."""
