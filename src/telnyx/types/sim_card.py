# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.sim_card_status import SimCardStatus

__all__ = ["SimCard", "CurrentBillingPeriodConsumedData", "CurrentDeviceLocation", "DataLimit", "PinPukCodes"]


class CurrentBillingPeriodConsumedData(BaseModel):
    amount: Optional[str] = None

    unit: Optional[str] = None


class CurrentDeviceLocation(BaseModel):
    accuracy: Optional[int] = None

    accuracy_unit: Optional[str] = None

    latitude: Optional[str] = None

    longitude: Optional[str] = None


class DataLimit(BaseModel):
    amount: Optional[str] = None

    unit: Optional[Literal["MB", "GB"]] = None


class PinPukCodes(BaseModel):
    pin1: Optional[str] = None
    """The primary Personal Identification Number (PIN) for the SIM card.

    This is a 4-digit code used to protect the SIM card from unauthorized use.
    """

    pin2: Optional[str] = None
    """The secondary Personal Identification Number (PIN2) for the SIM card.

    This is a 4-digit code used for additional security features.
    """

    puk1: Optional[str] = None
    """The primary Personal Unblocking Key (PUK1) for the SIM card.

    This is an 8-digit code used to unlock the SIM card if PIN1 is entered
    incorrectly multiple times.
    """

    puk2: Optional[str] = None
    """The secondary Personal Unblocking Key (PUK2) for the SIM card.

    This is an 8-digit code used to unlock the SIM card if PIN2 is entered
    incorrectly multiple times.
    """


class SimCard(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    actions_in_progress: Optional[bool] = None
    """Indicate whether the SIM card has any pending (in-progress) actions."""

    authorized_imeis: Optional[List[str]] = None
    """List of IMEIs authorized to use a given SIM card."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the resource was created."""

    current_billing_period_consumed_data: Optional[CurrentBillingPeriodConsumedData] = None
    """The SIM card consumption so far in the current billing cycle."""

    current_device_location: Optional[CurrentDeviceLocation] = None
    """Current physical location data of a given SIM card.

    Accuracy is given in meters.
    """

    current_imei: Optional[str] = None
    """IMEI of the device where a given SIM card is currently being used."""

    current_mcc: Optional[str] = None
    """Mobile Country Code of the current network to which the SIM card is connected.

    It's a three decimal digit that identifies a country.<br/><br/> This code is
    commonly seen joined with a Mobile Network Code (MNC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

    current_mnc: Optional[str] = None
    """Mobile Network Code of the current network to which the SIM card is connected.

    It's a two to three decimal digits that identify a network.<br/><br/> This code
    is commonly seen joined with a Mobile Country Code (MCC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

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

    ipv4: Optional[str] = None
    """The SIM's address in the currently connected network.

    This IPv4 address is usually obtained dynamically, so it may vary according to
    the location or new connections.
    """

    ipv6: Optional[str] = None
    """The SIM's address in the currently connected network.

    This IPv6 address is usually obtained dynamically, so it may vary according to
    the location or new connections.
    """

    live_data_session: Optional[Literal["connected", "disconnected", "unknown"]] = None
    """
    Indicates whether the device is actively connected to a network and able to run
    data.
    """

    msisdn: Optional[str] = None
    """
    Mobile Station International Subscriber Directory Number (MSISDN) is a number
    used to identify a mobile phone number internationally. <br/> MSISDN is defined
    by the E.164 numbering plan. It includes a country code and a National
    Destination Code which identifies the subscriber's operator.
    """

    pin_puk_codes: Optional[PinPukCodes] = None
    """PIN and PUK codes for the SIM card.

    Only available when include_pin_puk_codes=true is set in the request.
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
