# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .porting_order_type import PortingOrderType

__all__ = [
    "PortingOrderUpdateParams",
    "ActivationSettings",
    "Documents",
    "EndUser",
    "EndUserAdmin",
    "EndUserLocation",
    "Messaging",
    "Misc",
    "PhoneNumberConfiguration",
    "Requirement",
    "UserFeedback",
]


class PortingOrderUpdateParams(TypedDict, total=False):
    activation_settings: ActivationSettings

    customer_reference: str

    documents: Documents
    """Can be specified directly or via the `requirement_group_id` parameter."""

    end_user: EndUser

    messaging: Messaging

    misc: Misc

    phone_number_configuration: PhoneNumberConfiguration

    requirement_group_id: str
    """
    If present, we will read the current values from the specified Requirement Group
    into the Documents and Requirements for this Porting Order. Note that any future
    changes in the Requirement Group would have no impact on this Porting Order. We
    will return an error if a specified Requirement Group conflicts with documents
    or requirements in the same request.
    """

    requirements: Iterable[Requirement]
    """List of requirements for porting numbers."""

    user_feedback: UserFeedback

    webhook_url: str


class ActivationSettings(TypedDict, total=False):
    foc_datetime_requested: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 formatted Date/Time requested for the FOC date"""


class Documents(TypedDict, total=False):
    invoice: str
    """Returned ID of the submitted Invoice via the Documents endpoint"""

    loa: str
    """Returned ID of the submitted LOA via the Documents endpoint"""


class EndUserAdmin(TypedDict, total=False):
    account_number: str
    """The authorized person's account number with the current service provider"""

    auth_person_name: str
    """Name of person authorizing the porting order"""

    billing_phone_number: str
    """Billing phone number associated with these phone numbers"""

    business_identifier: str
    """European business identification number. Applicable only in the European Union"""

    entity_name: str
    """Person Name or Company name requesting the port"""

    pin_passcode: str
    """
    PIN/passcode possibly required by the old service provider for extra
    verification
    """

    tax_identifier: str
    """European tax identification number. Applicable only in the European Union"""


class EndUserLocation(TypedDict, total=False):
    administrative_area: str
    """State, province, or similar of billing address"""

    country_code: str
    """ISO3166-1 alpha-2 country code of billing address"""

    extended_address: str
    """Second line of billing address"""

    locality: str
    """City or municipality of billing address"""

    postal_code: str
    """Postal Code of billing address"""

    street_address: str
    """First line of billing address"""


class EndUser(TypedDict, total=False):
    admin: EndUserAdmin

    location: EndUserLocation


class Messaging(TypedDict, total=False):
    enable_messaging: bool
    """
    Indicates whether Telnyx will port messaging capabilities from the losing
    carrier. If false, any messaging capabilities will stay with their current
    provider.
    """


class Misc(TypedDict, total=False):
    new_billing_phone_number: str
    """New billing phone number for the remaining numbers.

    Used in case the current billing phone number is being ported to Telnyx. This
    will be set on your account with your current service provider and should be one
    of the numbers remaining on that account.
    """

    remaining_numbers_action: Literal["keep", "disconnect"]
    """
    Remaining numbers can be either kept with their current service provider or
    disconnected. 'new_billing_telephone_number' is required when
    'remaining_numbers_action' is 'keep'.
    """

    type: PortingOrderType
    """A port can be either 'full' or 'partial'.

    When type is 'full' the other attributes should be omitted.
    """


class PhoneNumberConfiguration(TypedDict, total=False):
    billing_group_id: str
    """identifies the billing group to set on the numbers when ported"""

    connection_id: str
    """identifies the connection to set on the numbers when ported"""

    emergency_address_id: str
    """identifies the emergency address to set on the numbers when ported"""

    messaging_profile_id: str
    """identifies the messaging profile to set on the numbers when ported"""

    tags: List[str]


class Requirement(TypedDict, total=False):
    field_value: Required[str]
    """
    identifies the document or provides the text value that satisfies this
    requirement
    """

    requirement_type_id: Required[str]
    """Identifies the requirement type that the `field_value` fulfills"""


class UserFeedback(TypedDict, total=False):
    user_comment: str
    """A comment related to the customer rating."""

    user_rating: int
    """
    Once an order is ported, cancellation is requested or the request is cancelled,
    the user may rate their experience
    """
