# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSetWirelessBlocklistParams"]


class ActionSetWirelessBlocklistParams(TypedDict, total=False):
    wireless_blocklist_id: Required[str]
    """The identification of the related Wireless Blocklist resource."""
