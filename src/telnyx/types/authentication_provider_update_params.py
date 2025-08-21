# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .settings_param import SettingsParam

__all__ = ["AuthenticationProviderUpdateParams"]


class AuthenticationProviderUpdateParams(TypedDict, total=False):
    active: bool
    """The active status of the authentication provider"""

    name: str
    """The name associated with the authentication provider."""

    settings: SettingsParam
    """The settings associated with the authentication provider."""

    settings_url: str
    """
    The URL for the identity provider metadata file to populate the settings
    automatically. If the settings attribute is provided, that will be used instead.
    """

    short_name: str
    """The short name associated with the authentication provider.

    This must be unique and URL-friendly, as it's going to be part of the login URL.
    """
