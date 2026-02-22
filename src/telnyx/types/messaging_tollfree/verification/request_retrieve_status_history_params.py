# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RequestRetrieveStatusHistoryParams"]


class RequestRetrieveStatusHistoryParams(TypedDict, total=False):
    page_number: Required[Annotated[int, PropertyInfo(alias="page[number]")]]

    page_size: Required[Annotated[int, PropertyInfo(alias="page[size]")]]
    """Request this many records per page.

    This value is automatically clamped if the provided value is too large.
    """
