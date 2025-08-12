# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SiprecConnectorUpdateParams"]


class SiprecConnectorUpdateParams(TypedDict, total=False):
    host: Required[str]
    """Hostname/IPv4 address of the SIPREC SRS."""

    name: Required[str]
    """Name for the SIPREC connector resource."""

    port: Required[int]
    """Port for the SIPREC SRS."""

    app_subdomain: str
    """
    Subdomain to route the call when using Telnyx SRS (optional for non-Telnyx SRS).
    """
