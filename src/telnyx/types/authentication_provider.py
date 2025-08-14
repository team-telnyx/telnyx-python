# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthenticationProvider", "Settings"]


class Settings(BaseModel):
    assertion_consumer_service_url: Optional[str] = None
    """The Assertion Consumer Service URL for the service provider (Telnyx)."""

    idp_cert_fingerprint: Optional[str] = None
    """The certificate fingerprint for the identity provider (IdP)"""

    idp_cert_fingerprint_algorithm: Optional[Literal["sha1", "sha256", "sha384", "sha512"]] = None
    """
    The algorithm used to generate the identity provider's (IdP) certificate
    fingerprint
    """

    idp_entity_id: Optional[str] = None
    """The Entity ID for the identity provider (IdP)."""

    idp_sso_target_url: Optional[str] = None
    """The SSO target url for the identity provider (IdP)."""

    name_identifier_format: Optional[str] = None
    """The name identifier format associated with the authentication provider.

    This must be the same for both the Identity Provider (IdP) and the service
    provider (Telnyx).
    """

    service_provider_entity_id: Optional[str] = None
    """The Entity ID for the service provider (Telnyx)."""


class AuthenticationProvider(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies the authentication provider."""

    active: Optional[bool] = None
    """The active status of the authentication provider"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    name: Optional[str] = None
    """The name associated with the authentication provider."""

    organization_id: Optional[str] = None
    """The id from the Organization the authentication provider belongs to."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    settings: Optional[Settings] = None
    """The settings associated with the authentication provider."""

    short_name: Optional[str] = None
    """The short name associated with the authentication provider.

    This must be unique and URL-friendly, as it's going to be part of the login URL.
    """

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
