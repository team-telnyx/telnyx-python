# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SipRegistrationStatusRetrieveResponse", "ExternalUacSettings", "InternalUacSettings"]


class ExternalUacSettings(BaseModel):
    """Outward-facing SIP settings used for registration. Password is redacted."""

    auth_username: Optional[str] = None

    expiration_sec: Optional[int] = None

    from_user: Optional[str] = None

    outbound_proxy: Optional[str] = None

    password: Optional[str] = None
    """Always redacted."""

    proxy: Optional[str] = None

    transport: Optional[Literal["TCP", "UDP", "TLS"]] = None

    username: Optional[str] = None


class InternalUacSettings(BaseModel):
    """Internal routing target the connection delivers calls to."""

    destination_uri: Optional[str] = None


class SipRegistrationStatusRetrieveResponse(BaseModel):
    b2bua_external: Optional[Dict[str, object]] = None
    """Raw external-side registration block reported by the registrar."""

    b2bua_internal: Optional[Dict[str, object]] = None
    """Raw internal-side block reported by the registrar."""

    connection_id: Optional[str] = None
    """Identifier of the UAC connection."""

    connection_name: Optional[str] = None
    """Human-readable connection name."""

    credential_type: Optional[Literal["uac_external_credential"]] = None
    """The credential type that was looked up."""

    external_state: Optional[str] = None
    """Registration state on the external (UAC / PBX) side, e.g. REGED."""

    external_uac_settings: Optional[ExternalUacSettings] = None
    """Outward-facing SIP settings used for registration. Password is redacted."""

    internal_uac_settings: Optional[InternalUacSettings] = None
    """Internal routing target the connection delivers calls to."""

    last_registration_response: Optional[str] = None
    """SIP response from the last registration attempt."""

    pair_state: Optional[str] = None
    """Internal pairing state, e.g. ACTIVE or INACTIVE."""

    registered: Optional[bool] = None
    """True if the endpoint is currently registered."""

    user_id: Optional[str] = None
    """Owner of the connection."""

    username: Optional[str] = None
    """SIP username used for the registration."""
