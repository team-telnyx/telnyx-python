# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TrafficPolicyProfileCreateParams"]


class TrafficPolicyProfileCreateParams(TypedDict, total=False):
    type: Required[Literal["whitelist", "blacklist"]]
    """The type of the traffic policy profile."""

    domains: SequenceNotStr[str]
    """Array of domain names."""

    ip_ranges: SequenceNotStr[str]
    """Array of IP ranges in CIDR notation."""

    limit_bw_kbps: Literal[512, 1024]
    """Bandwidth limit in kbps. Must be 512 or 1024."""

    services: SequenceNotStr[str]
    """Array of PCEF service IDs to include in the profile."""
