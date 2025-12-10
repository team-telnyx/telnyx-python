# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .record import Record
from .._models import BaseModel
from .wireguard_peer_patch import WireguardPeerPatch

__all__ = ["WireguardPeerCreateResponse", "Data"]


class Data(Record, WireguardPeerPatch):
    last_seen: Optional[str] = None
    """ISO 8601 formatted date-time indicating when peer sent traffic last time."""

    private_key: Optional[str] = None
    """
    Your WireGuard `Interface.PrivateKey`.<br /><br />This attribute is only ever
    utlised if, on POST, you do NOT provide your own `public_key`. In which case, a
    new Public and Private key pair will be generated for you. When your
    `private_key` is returned, you must save this immediately as we do not save it
    within Telnyx. If you lose your Private Key, it can not be recovered.
    """

    record_type: Optional[str] = None  # type: ignore
    """Identifies the type of the resource."""

    wireguard_interface_id: Optional[str] = None
    """The id of the wireguard interface associated with the peer."""


class WireguardPeerCreateResponse(BaseModel):
    data: Optional[Data] = None
