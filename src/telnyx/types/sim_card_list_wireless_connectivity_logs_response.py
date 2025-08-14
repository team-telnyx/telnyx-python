# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["SimCardListWirelessConnectivityLogsResponse", "Data"]


class Data(BaseModel):
    id: Optional[int] = None
    """Uniquely identifies the session."""

    apn: Optional[str] = None
    """
    The Access Point Name (APN) identifies the packet data network that a mobile
    data user wants to communicate with.
    """

    cell_id: Optional[str] = None
    """The cell ID to which the SIM connected."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the record was created."""

    imei: Optional[str] = None
    """
    The International Mobile Equipment Identity (or IMEI) is a number, usually
    unique, that identifies the device currently being used connect to the network.
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

    last_seen: Optional[str] = None
    """
    ISO 8601 formatted date-time indicating when the last heartbeat to the device
    was successfully recorded.
    """

    log_type: Optional[Literal["registration", "data"]] = None
    """
    The type of the session, 'registration' being the initial authentication session
    and 'data' the actual data transfer sessions.
    """

    mobile_country_code: Optional[str] = None
    """
    It's a three decimal digit that identifies a country.<br/><br/> This code is
    commonly seen joined with a Mobile Network Code (MNC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

    mobile_network_code: Optional[str] = None
    """
    It's a two to three decimal digits that identify a network.<br/><br/> This code
    is commonly seen joined with a Mobile Country Code (MCC) in a tuple that allows
    identifying a carrier known as PLMN (Public Land Mobile Network) code.
    """

    radio_access_technology: Optional[str] = None
    """The radio technology the SIM card used during the session."""

    record_type: Optional[str] = None

    sim_card_id: Optional[str] = None
    """The identification UUID of the related SIM card resource."""

    start_time: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the session started."""

    state: Optional[str] = None
    """The state of the SIM card after when the session happened."""

    stop_time: Optional[str] = None
    """ISO 8601 formatted date-time indicating when the session ended."""


class SimCardListWirelessConnectivityLogsResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[PaginationMeta] = None
