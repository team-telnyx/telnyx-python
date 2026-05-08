# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UacExternalSettings"]


class UacExternalSettings(BaseModel):
    """
    External SIP peer settings used by Telnyx when registering to your PBX and routing outbound calls.
    """

    auth_username: Optional[str] = None
    """The authentication username used in SIP digest authentication.

    If not set, the Username value will be used.
    """

    expiration_sec: Optional[int] = None
    """
    The registration interval, in seconds, indicating how often the system refreshes
    the SIP registration with the external SIP peer.
    """

    from_user: Optional[str] = None
    """The user portion of the SIP From header used in outbound requests.

    This controls the caller identity presented to the external SIP peer.
    """

    outbound_proxy: Optional[str] = None
    """
    An optional SIP proxy used to route outbound requests before reaching the
    external SIP peer.
    """

    password: Optional[str] = None
    """The SIP password used for digest authentication with the external SIP peer."""

    proxy: Optional[str] = None
    """
    The SIP proxy address of the external SIP peer used for registrations and
    outbound call routing.
    """

    transport: Optional[Literal["UDP", "TLS", "TCP"]] = None
    """
    The transport protocol used for SIP signaling when communicating with the
    external SIP peer. One of UDP, TLS, or TCP.
    """

    username: Optional[str] = None
    """
    The SIP username used to authenticate with the external SIP peer for
    registrations and outbound calls. Must start with a letter or number and contain
    only letters, numbers, hyphens, and underscores.
    """
