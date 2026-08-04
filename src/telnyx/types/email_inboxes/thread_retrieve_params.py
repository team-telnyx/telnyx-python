# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreadRetrieveParams"]


class ThreadRetrieveParams(TypedDict, total=False):
    inbox_id: Required[str]

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque message cursor returned by the previous thread-detail page."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of thread messages to return. Defaults to 25; maximum is 100."""
