# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PublicInternetGatewayCreateParams"]


class PublicInternetGatewayCreateParams(TypedDict, total=False):
    name: str
    """A user specified name for the interface."""

    network_id: str
    """The id of the network associated with the interface."""

    region_code: str
    """The region the interface should be deployed to."""
