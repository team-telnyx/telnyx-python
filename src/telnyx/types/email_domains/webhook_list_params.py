# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to return (offset pagination)"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of records per page"""

    sort: Literal["created_at", "-created_at"]
    """Field to sort by. Prefix with `-` for descending order."""
