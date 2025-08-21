# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["JobUpdateEmergencySettingsBatchParams"]


class JobUpdateEmergencySettingsBatchParams(TypedDict, total=False):
    emergency_enabled: Required[bool]
    """Indicates whether to enable or disable emergency services on the numbers."""

    phone_numbers: Required[List[str]]

    emergency_address_id: Optional[str]
    """Identifies the address to be used with emergency services.

    Required if emergency_enabled is true, must be null or omitted if
    emergency_enabled is false.
    """
