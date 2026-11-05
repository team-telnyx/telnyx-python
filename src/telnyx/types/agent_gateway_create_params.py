# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentGatewayCreateParams"]


class AgentGatewayCreateParams(TypedDict, total=False):
    wireguard_interface_id: Required[str]
    """One of the account's WireGuard Interfaces.

    The instance joins it as a peer, and the interface's other peers reach the
    instance.
    """

    name: Optional[str]
    """A label for people."""
