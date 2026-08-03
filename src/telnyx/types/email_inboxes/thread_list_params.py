# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThreadListParams"]


class ThreadListParams(TypedDict, total=False):
    filter_label: Annotated[str, PropertyInfo(alias="filter[label]")]
    """Returns only threads carrying this label.

    Thread labels are independent of the labels on the thread's messages.
    """

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor returned by the previous page."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results to return. Defaults to 25; maximum is 100."""
