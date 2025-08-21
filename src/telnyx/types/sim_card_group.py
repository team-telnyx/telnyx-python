# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .consumed_data import ConsumedData

__all__ = ["SimCardGroup", "DataLimit"]


class DataLimit(BaseModel):
    amount: Optional[str] = None

    unit: Optional[str] = None


class SimCardGroup(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    consumed_data: Optional[ConsumedData] = None
    """Represents the amount of data consumed."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    data_limit: Optional[DataLimit] = None
    """Upper limit on the amount of data the SIM cards, within the group, can use."""

    default: Optional[bool] = None
    """
    Indicates whether the SIM card group is the users default group.<br/>The default
    group is created for the user and can not be removed.
    """

    name: Optional[str] = None
    """A user friendly name for the SIM card group."""

    private_wireless_gateway_id: Optional[str] = None
    """The identification of the related Private Wireless Gateway resource."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""

    wireless_blocklist_id: Optional[str] = None
    """The identification of the related Wireless Blocklist resource."""
