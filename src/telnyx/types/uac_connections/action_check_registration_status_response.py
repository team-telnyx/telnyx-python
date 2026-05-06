# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionCheckRegistrationStatusResponse", "Data"]


class Data(BaseModel):
    ip_address: Optional[str] = None
    """The ip used during the SIP connection"""

    last_registration: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was last updated."""

    port: Optional[int] = None
    """The port of the SIP connection"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    sip_username: Optional[str] = None
    """The user name of the SIP connection"""

    status: Optional[Literal["Not Applicable", "Not Registered", "Failed", "Expired", "Registered", "Unregistered"]] = (
        None
    )
    """The current registration status of your SIP connection"""

    transport: Optional[str] = None
    """The protocol of the SIP connection"""

    user_agent: Optional[str] = None
    """The user agent of the SIP connection"""


class ActionCheckRegistrationStatusResponse(BaseModel):
    data: Optional[Data] = None
