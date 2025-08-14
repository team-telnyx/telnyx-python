# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = [
    "MessagingProfileListPhoneNumbersResponse",
    "Data",
    "DataFeatures",
    "DataFeaturesMms",
    "DataFeaturesSMS",
    "DataHealth",
]


class DataFeaturesMms(BaseModel):
    domestic_two_way: bool
    """Send messages to and receive messages from numbers in the same country."""

    international_inbound: bool
    """Receive messages from numbers in other countries."""

    international_outbound: bool
    """Send messages to numbers in other countries."""


class DataFeaturesSMS(BaseModel):
    domestic_two_way: bool
    """Send messages to and receive messages from numbers in the same country."""

    international_inbound: bool
    """Receive messages from numbers in other countries."""

    international_outbound: bool
    """Send messages to numbers in other countries."""


class DataFeatures(BaseModel):
    mms: Optional[DataFeaturesMms] = None
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features can vary depending on the characteristics the phone number, as well as
    its current product configuration.
    """

    sms: Optional[DataFeaturesSMS] = None
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features can vary depending on the characteristics the phone number, as well as
    its current product configuration.
    """


class DataHealth(BaseModel):
    inbound_outbound_ratio: float
    """The ratio of messages received to the number of messages sent."""

    message_count: int
    """The number of messages analyzed for the health metrics."""

    spam_ratio: float
    """The ratio of messages blocked for spam to the number of messages attempted."""

    success_ratio: float
    """
    The ratio of messages sucessfully delivered to the number of messages attempted.
    """


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    eligible_messaging_products: Optional[List[str]] = None
    """The messaging products that this number can be registered to use"""

    features: Optional[DataFeatures] = None

    health: Optional[DataHealth] = None
    """High level health metrics about the number and it's messaging sending patterns."""

    messaging_product: Optional[str] = None
    """The messaging product that the number is registered to use"""

    messaging_profile_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    phone_number: Optional[str] = None
    """+E.164 formatted phone number."""

    record_type: Optional[Literal["messaging_phone_number", "messaging_settings"]] = None
    """Identifies the type of the resource."""

    traffic_type: Optional[str] = None
    """The messaging traffic or use case for which the number is currently configured."""

    type: Optional[Literal["long-code", "toll-free", "short-code", "longcode", "tollfree", "shortcode"]] = None
    """The type of the phone number"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""


class MessagingProfileListPhoneNumbersResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
