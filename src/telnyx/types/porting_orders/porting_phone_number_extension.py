# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PortingPhoneNumberExtension", "ActivationRange", "ExtensionRange"]


class ActivationRange(BaseModel):
    end_at: Optional[int] = None
    """Specifies the end of the activation range.

    It must be no more than the end of the extension range.
    """

    start_at: Optional[int] = None
    """Specifies the start of the activation range.

    Must be greater or equal the start of the extension range.
    """


class ExtensionRange(BaseModel):
    end_at: Optional[int] = None
    """
    Specifies the end of the extension range for this porting phone number
    extension.
    """

    start_at: Optional[int] = None
    """
    Specifies the start of the extension range for this porting phone number
    extension.
    """


class PortingPhoneNumberExtension(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this porting phone number extension."""

    activation_ranges: Optional[List[ActivationRange]] = None
    """Specifies the activation ranges for this porting phone number extension.

    The activation range must be within the extension range and should not overlap
    with other activation ranges.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    extension_range: Optional[ExtensionRange] = None
    """Specifies the extension range for this porting phone number extension."""

    porting_phone_number_id: Optional[str] = None
    """
    Identifies the porting phone number associated with this porting phone number
    extension.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was last updated."""
