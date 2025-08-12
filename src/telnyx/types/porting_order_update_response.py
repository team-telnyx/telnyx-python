# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .porting_order_type import PortingOrderType

__all__ = [
    "PortingOrderUpdateResponse",
    "Data",
    "DataActivationSettings",
    "DataDocuments",
    "DataEndUser",
    "DataEndUserAdmin",
    "DataEndUserLocation",
    "DataMessaging",
    "DataMisc",
    "DataPhoneNumberConfiguration",
    "DataRequirement",
    "DataStatus",
    "DataStatusDetail",
    "DataUserFeedback",
    "Meta",
]


class DataActivationSettings(BaseModel):
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

    fast_port_eligible: Optional[bool] = None
    """Indicates whether this porting order is eligible for FastPort"""

    foc_datetime_actual: Optional[datetime] = None
    """ISO 8601 formatted Date/Time of the FOC date"""

    foc_datetime_requested: Optional[datetime] = None
    """ISO 8601 formatted Date/Time requested for the FOC date"""


class DataDocuments(BaseModel):
    invoice: Optional[str] = None
    """Returned ID of the submitted Invoice via the Documents endpoint"""

    loa: Optional[str] = None
    """Returned ID of the submitted LOA via the Documents endpoint"""


class DataEndUserAdmin(BaseModel):
    account_number: Optional[str] = None
    """The authorized person's account number with the current service provider"""

    auth_person_name: Optional[str] = None
    """Name of person authorizing the porting order"""

    billing_phone_number: Optional[str] = None
    """Billing phone number associated with these phone numbers"""

    business_identifier: Optional[str] = None
    """European business identification number. Applicable only in the European Union"""

    entity_name: Optional[str] = None
    """Person Name or Company name requesting the port"""

    pin_passcode: Optional[str] = None
    """
    PIN/passcode possibly required by the old service provider for extra
    verification
    """

    tax_identifier: Optional[str] = None
    """European tax identification number. Applicable only in the European Union"""


class DataEndUserLocation(BaseModel):
    administrative_area: Optional[str] = None
    """State, province, or similar of billing address"""

    country_code: Optional[str] = None
    """ISO3166-1 alpha-2 country code of billing address"""

    extended_address: Optional[str] = None
    """Second line of billing address"""

    locality: Optional[str] = None
    """City or municipality of billing address"""

    postal_code: Optional[str] = None
    """Postal Code of billing address"""

    street_address: Optional[str] = None
    """First line of billing address"""


class DataEndUser(BaseModel):
    admin: Optional[DataEndUserAdmin] = None

    location: Optional[DataEndUserLocation] = None


class DataMessaging(BaseModel):
    enable_messaging: Optional[bool] = None
    """
    Indicates whether Telnyx will port messaging capabilities from the losing
    carrier. If false, any messaging capabilities will stay with their current
    provider.
    """

    messaging_capable: Optional[bool] = None
    """Indicates whether the porting order can also port messaging capabilities."""

    messaging_port_completed: Optional[bool] = None
    """Indicates whether the messaging porting has been completed."""

    messaging_port_status: Optional[
        Literal["not_applicable", "pending", "activating", "exception", "canceled", "partial_port_complete", "ported"]
    ] = None
    """The current status of the messaging porting."""


class DataMisc(BaseModel):
    new_billing_phone_number: Optional[str] = None
    """New billing phone number for the remaining numbers.

    Used in case the current billing phone number is being ported to Telnyx. This
    will be set on your account with your current service provider and should be one
    of the numbers remaining on that account.
    """

    remaining_numbers_action: Optional[Literal["keep", "disconnect"]] = None
    """
    Remaining numbers can be either kept with their current service provider or
    disconnected. 'new_billing_telephone_number' is required when
    'remaining_numbers_action' is 'keep'.
    """

    type: Optional[PortingOrderType] = None
    """A port can be either 'full' or 'partial'.

    When type is 'full' the other attributes should be omitted.
    """


class DataPhoneNumberConfiguration(BaseModel):
    billing_group_id: Optional[str] = None
    """identifies the billing group to set on the numbers when ported"""

    connection_id: Optional[str] = None
    """identifies the connection to set on the numbers when ported"""

    emergency_address_id: Optional[str] = None
    """identifies the emergency address to set on the numbers when ported"""

    messaging_profile_id: Optional[str] = None
    """identifies the messaging profile to set on the numbers when ported"""

    tags: Optional[List[str]] = None


class DataRequirement(BaseModel):
    field_type: Optional[Literal["document"]] = None
    """Type of value expected on field_value field"""

    field_value: Optional[str] = None
    """identifies the document that satisfies this requirement"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirement_type_id: Optional[str] = None
    """Identifies the requirement type that meets this requirement"""


class DataStatusDetail(BaseModel):
    code: Optional[
        Literal[
            "ACCOUNT_NUMBER_MISMATCH",
            "AUTH_PERSON_MISMATCH",
            "BTN_ATN_MISMATCH",
            "ENTITY_NAME_MISMATCH",
            "FOC_EXPIRED",
            "FOC_REJECTED",
            "LOCATION_MISMATCH",
            "LSR_PENDING",
            "MAIN_BTN_PORTING",
            "OSP_IRRESPONSIVE",
            "OTHER",
            "PASSCODE_PIN_INVALID",
            "PHONE_NUMBER_HAS_SPECIAL_FEATURE",
            "PHONE_NUMBER_MISMATCH",
            "PHONE_NUMBER_NOT_PORTABLE",
            "PORT_TYPE_INCORRECT",
            "PORTING_ORDER_SPLIT_REQUIRED",
            "POSTAL_CODE_MISMATCH",
            "RATE_CENTER_NOT_PORTABLE",
            "SV_CONFLICT",
            "SV_UNKNOWN_FAILURE",
        ]
    ] = None
    """Identifier of an exception type"""

    description: Optional[str] = None
    """Description of an exception type"""


class DataStatus(BaseModel):
    details: Optional[List[DataStatusDetail]] = None
    """A list of 0 or more details about this porting order's status"""

    value: Optional[
        Literal[
            "draft",
            "in-process",
            "submitted",
            "exception",
            "foc-date-confirmed",
            "ported",
            "cancelled",
            "cancel-pending",
        ]
    ] = None
    """The current status of the porting order"""


class DataUserFeedback(BaseModel):
    user_comment: Optional[str] = None
    """A comment related to the customer rating."""

    user_rating: Optional[int] = None
    """
    Once an order is ported, cancellation is requested or the request is cancelled,
    the user may rate their experience
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this porting order"""

    activation_settings: Optional[DataActivationSettings] = None

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

    documents: Optional[DataDocuments] = None
    """Can be specified directly or via the `requirement_group_id` parameter."""

    end_user: Optional[DataEndUser] = None

    messaging: Optional[DataMessaging] = None
    """Information about messaging porting process."""

    misc: Optional[DataMisc] = None

    old_service_provider_ocn: Optional[str] = None
    """Identifies the old service provider"""

    parent_support_key: Optional[str] = None
    """
    A key to reference for the porting order group when contacting Telnyx customer
    support. This information is not available for porting orders in `draft` state
    """

    phone_number_configuration: Optional[DataPhoneNumberConfiguration] = None

    phone_number_type: Optional[Literal["landline", "local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """The type of the phone number"""

    porting_phone_numbers_count: Optional[int] = None
    """Count of phone numbers associated with this porting order"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    requirements: Optional[List[DataRequirement]] = None
    """List of documentation requirements for porting numbers.

    Can be set directly or via the `requirement_group_id` parameter.
    """

    requirements_met: Optional[bool] = None
    """Is true when the required documentation is met"""

    status: Optional[DataStatus] = None
    """Porting order status"""

    support_key: Optional[str] = None
    """A key to reference this porting order when contacting Telnyx customer support.

    This information is not available in draft porting orders.
    """

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    user_feedback: Optional[DataUserFeedback] = None

    user_id: Optional[str] = None
    """Identifies the user (or organization) who requested the porting order"""

    webhook_url: Optional[str] = None


class Meta(BaseModel):
    phone_numbers_url: Optional[str] = None
    """Link to list all phone numbers"""


class PortingOrderUpdateResponse(BaseModel):
    data: Optional[Data] = None

    meta: Optional[Meta] = None
