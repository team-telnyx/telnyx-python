# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .settings_param import SettingsParam

__all__ = ["AuthenticationProviderCreateParams"]


class AuthenticationProviderCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name associated with the authentication provider."""

    settings: Required[SettingsParam]
    """The settings associated with the authentication provider."""

    short_name: Required[str]
    """The short name associated with the authentication provider.

    This must be unique and URL-friendly, as it's going to be part of the login URL.
    """

    active: bool
    """The active status of the authentication provider"""

    settings_url: str
    """
    The URL for the identity provider metadata file to populate the settings
    automatically. If the settings attribute is provided, that will be used instead.
    """
