# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PortingOrderPhoneNumberConfiguration"]


class PortingOrderPhoneNumberConfiguration(BaseModel):
    billing_group_id: Optional[str] = None
    """identifies the billing group to set on the numbers when ported"""

    connection_id: Optional[str] = None
    """identifies the connection to set on the numbers when ported"""

    emergency_address_id: Optional[str] = None
    """identifies the emergency address to set on the numbers when ported"""

    messaging_profile_id: Optional[str] = None
    """identifies the messaging profile to set on the numbers when ported"""

    tags: Optional[List[str]] = None
