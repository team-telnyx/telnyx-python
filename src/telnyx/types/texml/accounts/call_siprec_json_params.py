# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallSiprecJsonParams"]


class CallSiprecJsonParams(TypedDict, total=False):
    account_sid: Required[str]

    connector_name: Annotated[str, PropertyInfo(alias="ConnectorName")]
    """The name of the connector to use for the SIPREC session."""

    include_metadata_custom_headers: Annotated[Literal[True, False], PropertyInfo(alias="IncludeMetadataCustomHeaders")]
    """
    When set, custom parameters will be added as metadata
    (recording.session.ExtensionParameters). Otherwise, they’ll be added to sip
    headers.
    """

    name: Annotated[str, PropertyInfo(alias="Name")]
    """Name of the SIPREC session.

    May be used to stop the SIPREC session from TeXML instruction.
    """

    secure: Annotated[Literal[True, False], PropertyInfo(alias="Secure")]
    """Controls whether to encrypt media sent to your SRS using SRTP and TLS.

    When set you need to configure SRS port in your connector to 5061.
    """

    session_timeout_secs: Annotated[int, PropertyInfo(alias="SessionTimeoutSecs")]
    """Sets `Session-Expires` header to the INVITE.

    A reinvite is sent every half the value set. Usefull for session keep alive.
    Minimum value is 90, set to 0 to disable.
    """

    sip_transport: Annotated[Literal["udp", "tcp", "tls"], PropertyInfo(alias="SipTransport")]
    """Specifies SIP transport protocol."""

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """
    URL destination for Telnyx to send status callback events to for the siprec
    session.
    """

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP request type used for `StatusCallback`."""

    track: Annotated[Literal["both_tracks", "inbound_track", "outbound_track"], PropertyInfo(alias="Track")]
    """The track to be used for siprec session.

    Can be `both_tracks`, `inbound_track` or `outbound_track`. Defaults to
    `both_tracks`.
    """
