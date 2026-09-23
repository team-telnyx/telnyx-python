# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "ConnectionRetrieveCountResponse",
    "Data",
    "DataCounts",
    "DataLimits",
    "DataLimitsGlobalConnectionLimit",
    "DataLimitsPerTypeConnectionLimits",
]


class DataCounts(BaseModel):
    """Counts of the authenticated user's connections, grouped by connection type.

    Forward-only connections are excluded.
    """

    call_control_applications: int
    """Number of Call Control applications."""

    credential_connections: int
    """Number of credential connections."""

    external_connections: int
    """Number of external connections."""

    fax_connections: int
    """Number of Fax applications."""

    fqdn_connections: int
    """Number of FQDN connections."""

    ip_connections: int
    """Number of IP connections."""

    microsoft_teams_sbc_connections: int
    """Number of Microsoft Teams SBC (direct routing) connections."""

    mobile_voice_connections: int
    """Number of mobile voice (IMS) connections."""

    operator_connect_connections: int
    """Number of Microsoft Operator Connect connections."""

    texml_applications: int
    """Number of TeXML applications."""

    third_party_provider_connections: int
    """Number of third-party provider connections."""

    uac_connections: int
    """Number of UAC connections."""

    zoom_sbc_connections: int
    """Number of Zoom SBC connections."""


class DataLimitsGlobalConnectionLimit(BaseModel):
    global_limit: int
    """Maximum total number of connections allowed, when a global limit applies."""


class DataLimitsPerTypeConnectionLimits(BaseModel):
    standard_limit: int
    """Maximum number of standard connections allowed, when per-type limits apply."""

    texml_limit: int
    """Maximum number of TeXML applications allowed, when per-type limits apply."""

    uac_limit: int
    """Maximum number of UAC connections allowed, when per-type limits apply."""


DataLimits: TypeAlias = Union[DataLimitsGlobalConnectionLimit, DataLimitsPerTypeConnectionLimits]


class Data(BaseModel):
    counts: DataCounts
    """Counts of the authenticated user's connections, grouped by connection type.

    Forward-only connections are excluded.
    """

    limits: DataLimits
    """Connection limits that apply to the user.

    Contains a single global_limit when a global connection limit applies, or
    per-type limits (standard_limit, texml_limit and uac_limit) when the user has
    per-type connection count capabilities.
    """

    record_type: str
    """Identifies the type of the resource."""


class ConnectionRetrieveCountResponse(BaseModel):
    data: Data
