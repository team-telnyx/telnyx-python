# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionAnalysisRetrieveParams"]


class SessionAnalysisRetrieveParams(TypedDict, total=False):
    record_type: Required[str]

    date_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 timestamp to narrow index selection for faster lookups."""

    expand: Literal["record", "none"]
    """Controls what data to expand on each event node."""

    include_children: bool
    """Whether to include child events in the response."""

    max_depth: int
    """Maximum traversal depth for the event tree."""
