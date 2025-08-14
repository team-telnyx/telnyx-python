# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SiprecConnectorRetrieveResponse", "Data"]


class Data(BaseModel):
    app_subdomain: Optional[str] = None
    """Subdomain to route calls when using Telnyx SRS (optional)."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date/time of creation."""

    host: Optional[str] = None
    """Hostname/IPv4 address of the SIPREC SRS."""

    name: Optional[str] = None
    """Name for the SIPREC connector resource."""

    port: Optional[int] = None
    """Port for the SIPREC SRS."""

    record_type: Optional[str] = None

    updated_at: Optional[str] = None
    """ISO 8601 formatted date/time of last update."""


class SiprecConnectorRetrieveResponse(BaseModel):
    data: Data
