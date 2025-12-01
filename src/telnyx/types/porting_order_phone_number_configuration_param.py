# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PortingOrderPhoneNumberConfigurationParam"]


class PortingOrderPhoneNumberConfigurationParam(TypedDict, total=False):
    billing_group_id: Optional[str]
    """identifies the billing group to set on the numbers when ported"""

    connection_id: Optional[str]
    """identifies the connection to set on the numbers when ported"""

    emergency_address_id: Optional[str]
    """identifies the emergency address to set on the numbers when ported"""

    messaging_profile_id: Optional[str]
    """identifies the messaging profile to set on the numbers when ported"""

    tags: SequenceNotStr[str]
