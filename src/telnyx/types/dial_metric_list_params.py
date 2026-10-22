# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DialMetricListParams"]


class DialMetricListParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Exclusive end of the range, ISO 8601.

    Must be after `start_time`. Buckets that start before this time are returned.
    """

    granularity: Required[Literal["second", "minute", "hour"]]
    """Bucket size.

    `second` returns 5-second buckets (the finest resolution) and is kept for the
    last 48 hours. `minute` and `hour` are kept for the last 30 days.
    """

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive start of the range, ISO 8601 (for example `2026-09-29T12:00:00.000Z`).

    Buckets that start at or after this time are returned. A `start_time` older than
    the retention window of the chosen `granularity` is moved forward to the start
    of that window, and `meta.start_time` returns the start actually used.
    """

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Opaque cursor from `meta.cursors.after` of the previous page.

    Do not parse or construct it. A cursor that matches no records returns an empty
    page whose `meta.cursors.after` and `meta.cursors.before` both echo the given
    cursor.
    """

    page_limit: Annotated[int, PropertyInfo(alias="page[limit]")]
    """Maximum number of buckets per page.

    Values outside the range are clamped to 1-10,000.
    """

    sort: Literal["-start_time", "start_time"]
    """Sort order of the buckets by `start_time`.

    `-start_time` (default) returns the newest first, `start_time` the oldest first.
    `region` follows the same direction for buckets with the same `start_time`. To
    read the live rate, use `granularity=second` and `sort=-start_time`, then take
    the first record of each `region`.
    """
