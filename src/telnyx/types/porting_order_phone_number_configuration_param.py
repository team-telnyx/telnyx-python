# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["PortingOrderPhoneNumberConfigurationParam"]


class PortingOrderPhoneNumberConfigurationParam(TypedDict, total=False):
    billing_group_id: str
    """identifies the billing group to set on the numbers when ported"""

    connection_id: str
    """identifies the connection to set on the numbers when ported"""

    emergency_address_id: str
    """identifies the emergency address to set on the numbers when ported"""

    messaging_profile_id: str
    """identifies the messaging profile to set on the numbers when ported"""

    tags: List[str]
