# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypedDict

__all__ = ["PortoutListRejectionCodesParams", "Filter"]


class PortoutListRejectionCodesParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[code], filter[code][in]
    """


class Filter(TypedDict, total=False):
    code: Union[int, Iterable[int]]
    """Filter rejections of a specific code"""
