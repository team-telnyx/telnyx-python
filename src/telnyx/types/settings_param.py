# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SettingsParam"]


class SettingsParam(TypedDict, total=False):
    idp_cert_fingerprint: Required[str]
    """The certificate fingerprint for the identity provider (IdP)"""

    idp_entity_id: Required[str]
    """The Entity ID for the identity provider (IdP)."""

    idp_sso_target_url: Required[str]
    """The SSO target url for the identity provider (IdP)."""

    idp_cert_fingerprint_algorithm: Literal["sha1", "sha256", "sha384", "sha512"]
    """
    The algorithm used to generate the identity provider's (IdP) certificate
    fingerprint
    """
