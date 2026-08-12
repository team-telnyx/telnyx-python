# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SipRegistrationStatusRetrieveResponse", "SipRegistrationDetails"]


class SipRegistrationDetails(BaseModel):
    """Detailed registration information reported by the registrar.

    The populated fields depend on `credential_type`: UAC external credentials report `auth_retries`, `uptime`, `next_action_at`, `failures`, and `sip_uri_user_host`; telephony credentials and SIP credential connections report `ua_ip`, `ua_port`, `transport`, and `last_modified`. All types report `expires`.
    """

    auth_retries: Optional[int] = None
    """Number of authentication retries on the last attempt (uac_external_credential)."""

    expires: Optional[int] = None
    """Unix timestamp when the current registration expires."""

    failures: Optional[int] = None
    """Count of consecutive registration failures (uac_external_credential)."""

    last_modified: Optional[str] = None
    """
    Timestamp when the registration was last modified (telephony_credential and
    sip_credential_connection).
    """

    next_action_at: Optional[int] = None
    """
    Unix timestamp of the next scheduled registration action
    (uac_external_credential).
    """

    sip_uri_user_host: Optional[str] = None
    """SIP URI user@host of the registered contact (uac_external_credential)."""

    transport: Optional[str] = None
    """Transport used for the registration, e.g.

    UDP/TCP/TLS (telephony_credential and sip_credential_connection).
    """

    ua_ip: Optional[str] = None
    """
    IP address of the registered user agent (telephony_credential and
    sip_credential_connection).
    """

    ua_port: Optional[int] = None
    """
    Port of the registered user agent (telephony_credential and
    sip_credential_connection).
    """

    uptime: Optional[int] = None
    """Registration uptime reported by the registrar (uac_external_credential)."""


class SipRegistrationStatusRetrieveResponse(BaseModel):
    connection_id: Optional[str] = None
    """Identifier of the connection associated with the credential."""

    connection_name: Optional[str] = None
    """Human-readable connection name."""

    credential_type: Optional[
        Literal["uac_external_credential", "telephony_credential", "sip_credential_connection"]
    ] = None
    """The credential type that was looked up."""

    credential_username: Optional[str] = None
    """SIP username used for the registration."""

    last_registration_response: Optional[str] = None
    """SIP response from the last registration attempt."""

    registered: Optional[bool] = None
    """True if the endpoint is currently registered."""

    sip_registration_details: Optional[SipRegistrationDetails] = None
    """Detailed registration information reported by the registrar.

    The populated fields depend on `credential_type`: UAC external credentials
    report `auth_retries`, `uptime`, `next_action_at`, `failures`, and
    `sip_uri_user_host`; telephony credentials and SIP credential connections report
    `ua_ip`, `ua_port`, `transport`, and `last_modified`. All types report
    `expires`.
    """

    sip_registration_status: Optional[
        Literal["unregistering", "connection_disabled", "standby", "failed", "trying", "registered", "unknown"]
    ] = None
    """Human-readable registration status derived from the registrar state."""
