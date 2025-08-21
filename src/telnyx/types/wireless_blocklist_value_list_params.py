# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WirelessBlocklistValueListParams"]


class WirelessBlocklistValueListParams(TypedDict, total=False):
    type: Required[Literal["country", "mcc", "plmn"]]
    """
    The Wireless Blocklist type for which to list possible values (e.g., `country`,
    `mcc`, `plmn`).
    """
