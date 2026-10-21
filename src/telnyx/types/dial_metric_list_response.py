# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DialMetricListResponse", "Dials", "DialsRejected"]


class DialsRejected(BaseModel):
    """Dial attempts rejected by a limit."""

    daily_limit: Optional[int] = None
    """Rejected by a daily limit."""

    dps_limit: Optional[int] = None
    """Rejected by the dials-per-second limit."""

    hourly_limit: Optional[int] = None
    """Rejected by an hourly limit."""


class Dials(BaseModel):
    """Dial attempt counts in the bucket."""

    accepted: Optional[int] = None
    """Dial attempts that were not rejected by a limit."""

    rejected: Optional[DialsRejected] = None
    """Dial attempts rejected by a limit."""

    total: Optional[int] = None
    """All dial attempts, rejected ones included: accepted plus every rejected count."""


class DialMetricListResponse(BaseModel):
    """Dial counts and rates for one region in one time bucket.

    One record per region per bucket.
    """

    average_dps: Optional[float] = None
    """
    `dials.total` divided by the bucket duration in seconds, rounded to 4 decimal
    places. Counts every dial attempt, rejected ones included.
    """

    dials: Optional[Dials] = None
    """Dial attempt counts in the bucket."""

    dps_limit: Optional[int] = None
    """
    DPS limit in force during the busiest 5-second window, so it compares directly
    with `peak_dps`. `null` means unlimited. Enforcement near the limit is
    approximate; `dials.rejected.dps_limit` is the authoritative signal that the
    limit was reached.
    """

    end_time: Optional[datetime] = None
    """End of the bucket (exclusive), UTC.

    Five seconds, one minute or one hour after `start_time`, depending on
    `granularity`.
    """

    peak_dps: Optional[float] = None
    """
    Dials per second, rounded to 4 decimal places, in the busiest 5-second window of
    the bucket, summed across all call-processing nodes of the region. Counts every
    dial attempt, rejected ones included, so `peak_dps` above `dps_limit` is
    expected when dials were rejected. For `granularity=second` it equals
    `average_dps`.
    """

    record_type: Optional[Literal["dial_metric"]] = None

    region: Optional[str] = None
    """Region where the dials were handled.

    Current values are `us`, `eu`, `australia`, `middle_east`, `canada` and `india`.
    New values can be added, so clients must tolerate values not listed here.
    Buckets of different regions are separate records.
    """

    start_time: Optional[datetime] = None
    """Start of the bucket (inclusive), UTC."""
