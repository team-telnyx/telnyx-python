# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UacExternalSettingsParam"]


class UacExternalSettingsParam(TypedDict, total=False):
    """
    External SIP peer settings used by Telnyx when registering to your PBX and routing outbound calls.
    """

    auth_username: Optional[str]
    """The authentication username used in SIP digest authentication.

    If not set, the Username value will be used.
    """

    expiration_sec: Optional[int]
    """
    The registration interval, in seconds, indicating how often the system refreshes
    the SIP registration with the external SIP peer.
    """

    from_user: Optional[str]
    """The user portion of the SIP From header used in outbound requests.

    This controls the caller identity presented to the external SIP peer.
    """

    outbound_proxy: Optional[str]
    """
    An optional SIP proxy used to route outbound requests before reaching the
    external SIP peer.
    """

    password: str
    """The SIP password used for digest authentication with the external SIP peer."""

    proxy: str
    """
    The SIP proxy address of the external SIP peer used for registrations and
    outbound call routing.
    """

    transport: Optional[Literal["UDP", "TLS", "TCP"]]
    """
    The transport protocol used for SIP signaling when communicating with the
    external SIP peer. One of UDP, TLS, or TCP.
    """

    username: str
    """
    The SIP username used to authenticate with the external SIP peer for
    registrations and outbound calls. Must start with a letter or number and contain
    only letters, numbers, hyphens, and underscores.
    """
