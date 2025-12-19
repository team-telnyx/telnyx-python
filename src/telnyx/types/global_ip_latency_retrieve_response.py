# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GlobalIPLatencyRetrieveResponse",
    "Data",
    "DataGlobalIP",
    "DataMeanLatency",
    "DataPercentileLatency",
    "P0",
    "P100",
    "P25",
    "P50",
    "P75",
    "P90",
    "P99",
    "DataProberLocation",
]


class DataGlobalIP(BaseModel):
    id: Optional[str] = None
    """Global IP ID."""

    ip_address: Optional[str] = None
    """The Global IP address."""


class DataMeanLatency(BaseModel):
    amount: Optional[float] = None
    """The average latency."""

    unit: Optional[str] = None
    """The unit of the average latency."""


class P0(BaseModel):
    amount: Optional[float] = None
    """The minimum latency."""

    unit: Optional[str] = None
    """The unit of the minimum latency."""


class P100(BaseModel):
    amount: Optional[float] = None
    """The maximum latency."""

    unit: Optional[str] = None
    """The unit of the maximum latency."""


class P25(BaseModel):
    amount: Optional[float] = None
    """The 25th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 25th percentile latency."""


class P50(BaseModel):
    amount: Optional[float] = None
    """The 50th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 50th percentile latency."""


class P75(BaseModel):
    amount: Optional[float] = None
    """The 75th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 75th percentile latency."""


class P90(BaseModel):
    amount: Optional[float] = None
    """The 90th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 90th percentile latency."""


class P99(BaseModel):
    amount: Optional[float] = None
    """The 99th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 99th percentile latency."""


class DataPercentileLatency(BaseModel):
    p0: Optional[P0] = FieldInfo(alias="0", default=None)

    p100: Optional[P100] = FieldInfo(alias="100", default=None)

    p25: Optional[P25] = FieldInfo(alias="25", default=None)

    p50: Optional[P50] = FieldInfo(alias="50", default=None)

    p75: Optional[P75] = FieldInfo(alias="75", default=None)

    p90: Optional[P90] = FieldInfo(alias="90", default=None)

    p99: Optional[P99] = FieldInfo(alias="99", default=None)


class DataProberLocation(BaseModel):
    id: Optional[str] = None
    """Location ID."""

    lat: Optional[float] = None
    """Latitude."""

    lon: Optional[float] = None
    """Longitude."""

    name: Optional[str] = None
    """Location name."""


class Data(BaseModel):
    global_ip: Optional[DataGlobalIP] = None

    mean_latency: Optional[DataMeanLatency] = None

    percentile_latency: Optional[DataPercentileLatency] = None

    prober_location: Optional[DataProberLocation] = None

    timestamp: Optional[datetime] = None
    """The timestamp of the metric."""


class GlobalIPLatencyRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
