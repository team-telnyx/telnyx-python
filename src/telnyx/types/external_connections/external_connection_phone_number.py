# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExternalConnectionPhoneNumber"]


class ExternalConnectionPhoneNumber(BaseModel):
    acquired_capabilities: Optional[
        List[Literal["FirstPartyAppAssignment", "InboundCalling", "Office365", "OutboundCalling", "UserAssignment"]]
    ] = None

    civic_address_id: Optional[str] = None
    """Identifies the civic address assigned to the phone number."""

    displayed_country_code: Optional[str] = None
    """
    The iso country code that will be displayed to the user when they receive a call
    from this phone number.
    """

    location_id: Optional[str] = None
    """Identifies the location assigned to the phone number."""

    number_id: Optional[str] = None
    """Phone number ID from the Telnyx API."""

    telephone_number: Optional[str] = None
    """Phone number in E164 format."""

    ticket_id: Optional[str] = None
    """Uniquely identifies the resource."""
