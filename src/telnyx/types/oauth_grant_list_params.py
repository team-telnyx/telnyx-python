# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OAuthGrantListParams"]


class OAuthGrantListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results per page"""
