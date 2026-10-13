# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TokenGroupListParams"]


class TokenGroupListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    page_snapshot: Annotated[str, PropertyInfo(alias="page[snapshot]")]
    """
    Required after page 1; account/filter-bound 15-minute stable snapshot;
    expired/mismatch 409.
    """
