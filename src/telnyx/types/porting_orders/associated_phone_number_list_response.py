# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..pagination_meta import PaginationMeta

__all__ = ["AssociatedPhoneNumberListResponse", "Data", "DataPhoneNumberRange"]


class DataPhoneNumberRange(BaseModel):
    end_at: Optional[str] = None
    """Specifies the end of the phone number range for this associated phone number."""

    start_at: Optional[str] = None
    """Specifies the start of the phone number range for this associated phone number."""


class Data(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this associated phone number."""

    action: Optional[Literal["keep", "disconnect"]] = None
    """Specifies the action to take with this phone number during partial porting."""

    country_code: Optional[str] = None
    """Specifies the country code for this associated phone number.

    It is a two-letter ISO 3166-1 alpha-2 country code.
    """

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    phone_number_range: Optional[DataPhoneNumberRange] = None
    """Specifies the phone number range for this associated phone number."""

    phone_number_type: Optional[Literal["landline", "local", "mobile", "national", "shared_cost", "toll_free"]] = None
    """Specifies the phone number type for this associated phone number."""

    porting_order_id: Optional[str] = None
    """Identifies the porting order associated with this phone number."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was last updated."""


class AssociatedPhoneNumberListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
