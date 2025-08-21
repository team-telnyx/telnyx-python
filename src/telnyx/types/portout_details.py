# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortoutDetails"]


class PortoutDetails(BaseModel):
    id: Optional[str] = None

    already_ported: Optional[bool] = None
    """Is true when the number is already ported"""

    authorized_name: Optional[str] = None
    """Name of person authorizing the porting order"""

    carrier_name: Optional[str] = None
    """Carrier the number will be ported out to"""

    city: Optional[str] = None
    """City or municipality of billing address"""

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the portout was created"""

    current_carrier: Optional[str] = None
    """The current carrier"""

    end_user_name: Optional[str] = None
    """Person name or company name requesting the port"""

    foc_date: Optional[str] = None
    """ISO 8601 formatted Date/Time of the FOC date"""

    host_messaging: Optional[bool] = None
    """
    Indicates whether messaging services should be maintained with Telnyx after the
    port out completes
    """

    inserted_at: Optional[str] = None
    """ISO 8601 formatted date of when the portout was created"""

    lsr: Optional[List[str]] = None
    """The Local Service Request"""

    phone_numbers: Optional[List[str]] = None
    """Phone numbers associated with this portout"""

    pon: Optional[str] = None
    """Port order number assigned by the carrier the number will be ported out to"""

    reason: Optional[str] = None
    """The reason why the order is being rejected by the user.

    If the order is authorized, this field can be left null
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    rejection_code: Optional[int] = None
    """The rejection code for one of the valid rejections to reject a port out order"""

    requested_foc_date: Optional[str] = None
    """ISO 8601 formatted Date/Time of the user requested FOC date"""

    service_address: Optional[str] = None
    """First line of billing address (street address)"""

    spid: Optional[str] = None
    """New service provider spid"""

    state: Optional[str] = None
    """State, province, or similar of billing address"""

    status: Optional[Literal["pending", "authorized", "ported", "rejected", "rejected-pending", "canceled"]] = None
    """Status of portout request"""

    support_key: Optional[str] = None
    """
    A key to reference this port out request when contacting Telnyx customer support
    """

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the portout was last updated"""

    user_id: Optional[str] = None
    """Identifies the user (or organization) who requested the port out"""

    vendor: Optional[str] = None
    """Telnyx partner providing network coverage"""

    zip: Optional[str] = None
    """Postal Code of billing address"""
