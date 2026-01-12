# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.messaging_feature_set import MessagingFeatureSet

__all__ = ["MessagingListResponse", "Features"]


class Features(BaseModel):
    sms: Optional[MessagingFeatureSet] = None
    """The set of features available for a specific messaging use case (SMS or MMS).

    Features can vary depending on the characteristics the phone number, as well as
    its current product configuration.
    """


class MessagingListResponse(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    features: Optional[Features] = None

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

    type: Optional[Literal["longcode"]] = None
    """The type of the phone number"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
