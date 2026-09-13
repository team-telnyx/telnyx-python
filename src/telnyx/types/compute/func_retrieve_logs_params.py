# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FuncRetrieveLogsParams"]


class FuncRetrieveLogsParams(TypedDict, total=False):
    end_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return records at or before this RFC 3339 timestamp."""

    limit: int
    """Maximum records to return."""

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return records at or after this RFC 3339 timestamp."""

    type: Literal["runtime", "invocations"]
    """Log stream to return."""
