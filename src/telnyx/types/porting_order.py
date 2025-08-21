# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .porting_order_misc import PortingOrderMisc
from .porting_order_end_user import PortingOrderEndUser
from .porting_order_documents import PortingOrderDocuments
from .porting_order_messaging import PortingOrderMessaging
from .porting_order_requirement import PortingOrderRequirement
from .porting_order_user_feedback import PortingOrderUserFeedback
from .shared.porting_order_status import PortingOrderStatus
from .porting_order_activation_settings import PortingOrderActivationSettings
from .porting_order_phone_number_configuration import PortingOrderPhoneNumberConfiguration

__all__ = ["PortingOrder"]


class PortingOrder(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this porting order"""

    activation_settings: Optional[PortingOrderActivationSettings] = None

    additional_steps: Optional[List[Literal["associated_phone_numbers", "phone_number_verification_codes"]]] = None
    """
    For specific porting orders, we may require additional steps to be taken before
    submitting the porting order.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    customer_reference: Optional[str] = None
    """A customer-specified reference number for customer bookkeeping purposes"""

    description: Optional[str] = None
    """A description of the porting order"""

    documents: Optional[PortingOrderDocuments] = None
    """Can be specified directly or via the `requirement_group_id` parameter."""

    end_user: Optional[PortingOrderEndUser] = None

    messaging: Optional[PortingOrderMessaging] = None
    """Information about messaging porting process."""

    misc: Optional[PortingOrderMisc] = None

    old_service_provider_ocn: Optional[str] = None
    """Identifies the old service provider"""

    parent_support_key: Optional[str] = None
    """
    A key to reference for the porting order group when contacting Telnyx customer
    support. This information is not available for porting orders in `draft` state
    """

    phone_number_configuration: Optional[PortingOrderPhoneNumberConfiguration] = None

    phone_number_type: Optional[Literal["landline", "local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """The type of the phone number"""

    porting_phone_numbers_count: Optional[int] = None
    """Count of phone numbers associated with this porting order"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirements: Optional[List[PortingOrderRequirement]] = None
    """List of documentation requirements for porting numbers.

    Can be set directly or via the `requirement_group_id` parameter.
    """

    requirements_met: Optional[bool] = None
    """Is true when the required documentation is met"""

    status: Optional[PortingOrderStatus] = None
    """Porting order status"""

    support_key: Optional[str] = None
    """A key to reference this porting order when contacting Telnyx customer support.

    This information is not available in draft porting orders.
    """

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    user_feedback: Optional[PortingOrderUserFeedback] = None

    user_id: Optional[str] = None
    """Identifies the user (or organization) who requested the porting order"""

    webhook_url: Optional[str] = None
