# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["InexplicitNumberOrderListResponse", "Data", "DataOrderingGroup", "DataOrderingGroupOrder"]


class DataOrderingGroupOrder(BaseModel):
    number_order_id: str
    """ID of the main number order"""

    sub_number_order_ids: List[str]
    """Array of sub number order IDs"""


class DataOrderingGroup(BaseModel):
    administrative_area: Optional[str] = None
    """Filter for phone numbers in a given state / province"""

    count_allocated: Optional[int] = None
    """Quantity of phone numbers allocated"""

    count_requested: Optional[int] = None
    """Quantity of phone numbers requested"""

    country_iso: Optional[str] = None
    """Country where you would like to purchase phone numbers"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the ordering group was created"""

    error_reason: Optional[str] = None
    """Error reason if applicable"""

    national_destination_code: Optional[str] = None
    """Filter by area code"""

    orders: Optional[List[DataOrderingGroupOrder]] = None
    """Array of orders created to fulfill the inexplicit order"""

    phone_number_type: Optional[str] = None
    """Number type"""

    phone_number_contains: Optional[str] = FieldInfo(alias="phone_number[contains]", default=None)
    """Filter for phone numbers that contain the digits specified"""

    phone_number_ends_with: Optional[str] = FieldInfo(alias="phone_number[ends_with]", default=None)
    """Filter by the ending digits of the phone number"""

    phone_number_starts_with: Optional[str] = FieldInfo(alias="phone_number[starts_with]", default=None)
    """Filter by the starting digits of the phone number"""

    status: Optional[Literal["pending", "processing", "failed", "success", "partial_success"]] = None
    """Status of the ordering group"""

    strategy: Optional[Literal["always", "never"]] = None
    """Ordering strategy used"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the ordering group was updated"""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the inexplicit number order"""

    billing_group_id: Optional[str] = None
    """Billing group id to apply to phone numbers that are purchased"""

    connection_id: Optional[str] = None
    """Connection id to apply to phone numbers that are purchased"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created"""

    customer_reference: Optional[str] = None
    """Reference label for the customer"""

    messaging_profile_id: Optional[str] = None
    """Messaging profile id to apply to phone numbers that are purchased"""

    ordering_groups: Optional[List[DataOrderingGroup]] = None

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated"""


class InexplicitNumberOrderListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
