# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tunnel", "Connection"]


class Connection(BaseModel):
    """A tunnel process connected to the tunnel."""

    connected_at: Optional[datetime] = None
    """When the process connected."""

    hostname: Optional[str] = None
    """The name the host reports for itself. Preview: empty until the CLI reports it."""

    region_code: Optional[str] = None
    """The Telnyx region the process is connected to.

    Preview: empty until the CLI reports it.
    """

    version: Optional[str] = None
    """The `telnyx-edge` CLI version of the process.

    Preview: empty until the CLI reports it.
    """


class Tunnel(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    connection_count: Optional[int] = None
    """The number of tunnel processes connected with the tunnel's token."""

    connections: Optional[List[Connection]] = None
    """The tunnel processes connected with the tunnel's token."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    name: Optional[str] = None
    """A user specified name for the tunnel."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["inactive", "healthy", "degraded"]] = None
    """
    `inactive` when no tunnel process is connected, and `healthy` when one or more
    are. `degraded` (Preview, not reported yet) when a process is connected but
    fails to reach its destinations.
    """
