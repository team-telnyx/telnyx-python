# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessIPAddressCreateParams"]


class AccessIPAddressCreateParams(TypedDict, total=False):
    ip_address: Required[str]

    description: str
