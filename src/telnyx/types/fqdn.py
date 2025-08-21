# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Fqdn"]


class Fqdn(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    connection_id: Optional[str] = None
    """ID of the FQDN connection to which this FQDN is attached."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    dns_record_type: Optional[str] = None
    """The DNS record type for the FQDN.

    For cases where a port is not set, the DNS record type must be 'srv'. For cases
    where a port is set, the DNS record type must be 'a'. If the DNS record type is
    'a' and a port is not specified, 5060 will be used.
    """

    fqdn: Optional[str] = None
    """FQDN represented by this resource."""

    port: Optional[int] = None
    """Port to use when connecting to this FQDN."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
