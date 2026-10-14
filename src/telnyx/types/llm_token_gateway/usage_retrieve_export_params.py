# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageRetrieveExportParams"]


class UsageRetrieveExportParams(TypedDict, total=False):
    cursor: str
    """Opaque next_cursor from a previous page; not combinable with start_time.

    Bound to the requested types; the account always comes from the credential.
    """

    limit: int

    start_time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    First page only: RFC 3339 with offset, at most 30 days ago and not in the
    future; default now - 24h.
    """

    types: str
    """Comma-separated subset of inference.request,guardrail.evaluation; default both."""
