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
    "DataPercentileLatency_0",
    "DataPercentileLatency_100",
    "DataPercentileLatency_25",
    "DataPercentileLatency_50",
    "DataPercentileLatency_75",
    "DataPercentileLatency_90",
    "DataPercentileLatency_99",
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


class DataPercentileLatency_0(BaseModel):
    amount: Optional[float] = None
    """The minimum latency."""

    unit: Optional[str] = None
    """The unit of the minimum latency."""


class DataPercentileLatency_100(BaseModel):
    amount: Optional[float] = None
    """The maximum latency."""

    unit: Optional[str] = None
    """The unit of the maximum latency."""


class DataPercentileLatency_25(BaseModel):
    amount: Optional[float] = None
    """The 25th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 25th percentile latency."""


class DataPercentileLatency_50(BaseModel):
    amount: Optional[float] = None
    """The 50th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 50th percentile latency."""


class DataPercentileLatency_75(BaseModel):
    amount: Optional[float] = None
    """The 75th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 75th percentile latency."""


class DataPercentileLatency_90(BaseModel):
    amount: Optional[float] = None
    """The 90th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 90th percentile latency."""


class DataPercentileLatency_99(BaseModel):
    amount: Optional[float] = None
    """The 99th percentile latency."""

    unit: Optional[str] = None
    """The unit of the 99th percentile latency."""


class DataPercentileLatency(BaseModel):
    api_0: Optional[DataPercentileLatency_0] = FieldInfo(alias="0", default=None)

    api_100: Optional[DataPercentileLatency_100] = FieldInfo(alias="100", default=None)

    api_25: Optional[DataPercentileLatency_25] = FieldInfo(alias="25", default=None)

    api_50: Optional[DataPercentileLatency_50] = FieldInfo(alias="50", default=None)

    api_75: Optional[DataPercentileLatency_75] = FieldInfo(alias="75", default=None)

    api_90: Optional[DataPercentileLatency_90] = FieldInfo(alias="90", default=None)

    api_99: Optional[DataPercentileLatency_99] = FieldInfo(alias="99", default=None)


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
