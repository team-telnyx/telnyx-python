# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TelephonySettingsParam"]


class TelephonySettingsParam(TypedDict, total=False):
    default_texml_app_id: str
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    supports_unauthenticated_web_calls: bool
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """
