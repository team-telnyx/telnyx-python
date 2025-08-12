# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DynamicEmergencyEndpointCreateParams"]


class DynamicEmergencyEndpointCreateParams(TypedDict, total=False):
    callback_number: Required[str]

    caller_name: Required[str]

    dynamic_emergency_address_id: Required[str]
    """An id of a currently active dynamic emergency location."""
