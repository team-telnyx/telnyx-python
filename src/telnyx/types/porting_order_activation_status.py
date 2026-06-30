# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["PortingOrderActivationStatus"]

PortingOrderActivationStatus: TypeAlias = Literal[
    "New",
    "Pending",
    "Conflict",
    "Cancel Pending",
    "Failed",
    "Concurred",
    "Activate RDY",
    "Disconnect Pending",
    "Concurrence Sent",
    "Old",
    "Sending",
    "Active",
    "Cancelled",
]
