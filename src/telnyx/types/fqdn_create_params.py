# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FqdnCreateParams"]


class FqdnCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """ID of the FQDN connection to which this IP should be attached."""

    dns_record_type: Required[str]
    """The DNS record type for the FQDN.

    For cases where a port is not set, the DNS record type must be 'srv'. For cases
    where a port is set, the DNS record type must be 'a'. If the DNS record type is
    'a' and a port is not specified, 5060 will be used.
    """

    fqdn: Required[str]
    """FQDN represented by this resource."""

    port: Optional[int]
    """Port to use when connecting to this FQDN."""
