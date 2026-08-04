# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DraftListParams"]


class DraftListParams(TypedDict, total=False):
    filter_status: Annotated[Literal["draft", "sending", "sent"], PropertyInfo(alias="filter[status]")]
    """Restrict results to drafts in this state."""

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor returned by the previous page."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results to return. Defaults to 25; maximum is 100."""
