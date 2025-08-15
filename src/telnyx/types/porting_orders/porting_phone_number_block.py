# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingPhoneNumberBlock", "ActivationRange", "PhoneNumberRange"]


class ActivationRange(BaseModel):
    end_at: Optional[str] = None
    """Specifies the end of the activation range.

    It must be no more than the end of the phone number range.
    """

    start_at: Optional[str] = None
    """Specifies the start of the activation range.

    Must be greater or equal the start of the phone number range.
    """


class PhoneNumberRange(BaseModel):
    end_at: Optional[str] = None
    """
    Specifies the end of the phone number range for this porting phone number block.
    """

    start_at: Optional[str] = None
    """
    Specifies the start of the phone number range for this porting phone number
    block.
    """


class PortingPhoneNumberBlock(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this porting phone number block."""

    activation_ranges: Optional[List[ActivationRange]] = None
    """Specifies the activation ranges for this porting phone number block.

    The activation range must be within the phone number range and should not
    overlap with other activation ranges.
    """

    country_code: Optional[str] = None
    """Specifies the country code for this porting phone number block.

    It is a two-letter ISO 3166-1 alpha-2 country code.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    phone_number_range: Optional[PhoneNumberRange] = None
    """Specifies the phone number range for this porting phone number block."""

    phone_number_type: Optional[Literal["landline", "local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """Specifies the phone number type for this porting phone number block."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was last updated."""
