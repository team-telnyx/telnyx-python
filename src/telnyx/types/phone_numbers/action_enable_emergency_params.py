# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionEnableEmergencyParams"]


class ActionEnableEmergencyParams(TypedDict, total=False):
    emergency_address_id: Required[str]
    """Identifies the address to be used with emergency services."""

    emergency_enabled: Required[bool]
    """Indicates whether to enable emergency services on this number."""
