# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NetworkInterfaceRegionParam"]


class NetworkInterfaceRegionParam(TypedDict, total=False):
    region_code: str
    """The region the interface should be deployed to."""
