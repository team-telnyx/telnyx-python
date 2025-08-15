# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .messaging_feature_set import MessagingFeatureSet
from .number_health_metrics import NumberHealthMetrics

__all__ = ["PhoneNumberWithMessagingSettings", "Features"]


class Features(BaseModel):
    mms: Optional[MessagingFeatureSet] = None
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features can vary depending on the characteristics the phone number, as well as
    its current product configuration.
    """

    sms: Optional[MessagingFeatureSet] = None
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features can vary depending on the characteristics the phone number, as well as
    its current product configuration.
    """


class PhoneNumberWithMessagingSettings(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    eligible_messaging_products: Optional[List[str]] = None
    """The messaging products that this number can be registered to use"""

    features: Optional[Features] = None

    health: Optional[NumberHealthMetrics] = None
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
