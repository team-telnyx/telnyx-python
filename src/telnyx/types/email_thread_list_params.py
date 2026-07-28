# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailThreadListParams"]


class EmailThreadListParams(TypedDict, total=False):
    filter_inbox_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="filter[inbox_id]")]
    """Restrict results to one or more inboxes.

    Repeat the parameter (`filter[inbox_id][]=...&filter[inbox_id][]=...`) or pass a
    comma-separated list. Omit to list every inbox in the account. Inboxes outside
    the account are silently excluded. If the filter is present, it must contain at
    least one non-empty UUID.
    """

    filter_label: Annotated[str, PropertyInfo(alias="filter[label]")]
    """Returns only threads carrying this label.

    Matching is exact and case-sensitive. Thread labels are independent of the
    labels on the thread's messages.
    """

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor returned by the previous page."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results to return. Defaults to 25; maximum is 100."""
