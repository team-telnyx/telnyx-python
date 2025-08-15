# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sim_card_status import SimCardStatus

__all__ = ["SimpleSimCard", "CurrentBillingPeriodConsumedData", "DataLimit"]


class CurrentBillingPeriodConsumedData(BaseModel):
    amount: Optional[str] = None

    unit: Optional[str] = None


class DataLimit(BaseModel):
    amount: Optional[str] = None

    unit: Optional[Literal["MB", "GB"]] = None


class SimpleSimCard(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    actions_in_progress: Optional[bool] = None
    """Indicate whether the SIM card has any pending (in-progress) actions."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    current_billing_period_consumed_data: Optional[CurrentBillingPeriodConsumedData] = None
    """The SIM card consumption so far in the current billing cycle."""

    data_limit: Optional[DataLimit] = None
    """The SIM card individual data limit configuration."""

    iccid: Optional[str] = None
    """The ICCID is the identifier of the specific SIM card/chip.

    Each SIM is internationally identified by its integrated circuit card identifier
    (ICCID). ICCIDs are stored in the SIM card's memory and are also engraved or
    printed on the SIM card body during a process called personalization.
    """

    imsi: Optional[str] = None
    """
    SIM cards are identified on their individual network operators by a unique
    International Mobile Subscriber Identity (IMSI). <br/> Mobile network operators
    connect mobile phone calls and communicate with their market SIM cards using
    their IMSIs. The IMSI is stored in the Subscriber Identity Module (SIM) inside
    the device and is sent by the device to the appropriate network. It is used to
    acquire the details of the device in the Home Location Register (HLR) or the
    Visitor Location Register (VLR).
    """

    msisdn: Optional[str] = None
    """
    Mobile Station International Subscriber Directory Number (MSISDN) is a number
    used to identify a mobile phone number internationally. <br/> MSISDN is defined
    by the E.164 numbering plan. It includes a country code and a National
    Destination Code which identifies the subscriber's operator.
    """

    record_type: Optional[str] = None

    sim_card_group_id: Optional[str] = None
    """The group SIMCardGroup identification.

    This attribute can be <code>null</code> when it's present in an associated
    resource.
    """

    status: Optional[SimCardStatus] = None

    tags: Optional[List[str]] = None
    """Searchable tags associated with the SIM card"""

    type: Optional[Literal["physical", "esim"]] = None
    """The type of SIM card"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was updated."""
