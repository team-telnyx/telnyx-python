# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["PortingPhoneNumberListResponse", "Data"]


class Data(BaseModel):
    activation_status: Optional[
        Literal[
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
    ] = None
    """Activation status"""

    phone_number: Optional[str] = None
    """E164 formatted phone number"""

    phone_number_type: Optional[Literal["landline", "local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """The type of the phone number"""

    portability_status: Optional[Literal["pending", "confirmed", "provisional"]] = None
    """
    Specifies whether Telnyx is able to confirm portability this number in the
    United States & Canada. International phone numbers are provisional by default.
    """

    porting_order_id: Optional[str] = None
    """Identifies the associated port request"""

    porting_order_status: Optional[
        Literal[
            "draft",
            "in-process",
            "submitted",
            "exception",
            "foc-date-confirmed",
            "cancel-pending",
            "ported",
            "cancelled",
        ]
    ] = None
    """The current status of the porting order"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirements_status: Optional[
        Literal["requirement-info-pending", "requirement-info-under-review", "requirement-info-exception", "approved"]
    ] = None
    """The current status of the requirements in a INTL porting order"""

    support_key: Optional[str] = None
    """A key to reference this porting order when contacting Telnyx customer support"""


class PortingPhoneNumberListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
