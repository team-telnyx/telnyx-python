# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["TrafficPolicyProfileUpdateParams"]


class TrafficPolicyProfileUpdateParams(TypedDict, total=False):
    domains: SequenceNotStr[str]
    """Array of domain names."""

    ip_ranges: SequenceNotStr[str]
    """Array of IP ranges in CIDR notation."""

    limit_bw_kbps: Optional[Literal[512, 1024]]
    """Bandwidth limit in kbps. Must be 512 or 1024, or null to remove."""

    services: SequenceNotStr[str]
    """Array of PCEF service IDs to include in the profile."""

    type: Literal["whitelist", "blacklist", "throttling"]
    """The type of the traffic policy profile."""
