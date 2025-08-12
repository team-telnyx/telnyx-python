# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionStartSiprecParams"]


class ActionStartSiprecParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    connector_name: str
    """Name of configured SIPREC connector to be used."""

    include_metadata_custom_headers: Literal[True, False]
    """
    When set, custom parameters will be added as metadata
    (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
    headers.
    """

    secure: Literal[True, False]
    """Controls whether to encrypt media sent to your SRS using SRTP and TLS.

    When set you need to configure SRS port in your connector to 5061.
    """

    session_timeout_secs: int
    """Sets `Session-Expires` header to the INVITE.

    A reinvite is sent every half the value set. Usefull for session keep alive.
    Minimum value is 90, set to 0 to disable.
    """

    sip_transport: Literal["udp", "tcp", "tls"]
    """Specifies SIP transport protocol."""

    siprec_track: Literal["inbound_track", "outbound_track", "both_tracks"]
    """Specifies which track should be sent on siprec session."""
