# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentGatewayRetrieveSpendLogsParams"]


class AgentGatewayRetrieveSpendLogsParams(TypedDict, total=False):
    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The window's end, an RFC 3339 timestamp with an offset. Defaults to now."""

    key_id: str
    """Only the requests made with this key."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page to return, counting from 1."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Results per page."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The window's start, an RFC 3339 timestamp with an offset.

    Defaults to 24 hours before `end`.
    """

    team_id: str
    """Only the requests made with this team's keys."""
