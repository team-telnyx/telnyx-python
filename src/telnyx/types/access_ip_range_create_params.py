# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessIPRangeCreateParams"]


class AccessIPRangeCreateParams(TypedDict, total=False):
    cidr_block: Required[str]

    description: str
