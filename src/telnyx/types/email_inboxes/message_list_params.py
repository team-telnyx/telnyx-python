# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    filter_from: Annotated[str, PropertyInfo(alias="filter[from]")]
    """Case-insensitive literal substring of the sender address."""

    filter_label: Annotated[str, PropertyInfo(alias="filter[label]")]
    """Returns only messages carrying this label.

    Matching is exact and case-sensitive. Reserved `telnyx:` labels can be filtered
    on even though they cannot be written by customers.
    """

    filter_read: Annotated[bool, PropertyInfo(alias="filter[read]")]
    """Whether the message has a read timestamp."""

    filter_received_after: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[received_after]", format="iso8601")
    ]
    """Inclusive ISO 8601 lower bound for the received timestamp."""

    filter_received_before: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[received_before]", format="iso8601")
    ]
    """Inclusive ISO 8601 upper bound for the received timestamp."""

    filter_search: Annotated[str, PropertyInfo(alias="filter[search]")]
    """Full-text query over subject and body, up to 500 characters."""

    filter_subject: Annotated[str, PropertyInfo(alias="filter[subject]")]
    """Case-insensitive literal substring of the subject."""

    filter_unread: Annotated[bool, PropertyInfo(alias="filter[unread]")]
    """Whether the message has no read timestamp.

    Set to `true` to return only unread messages.
    """

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor returned by the previous page."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results to return. Defaults to 25; maximum is 100."""
