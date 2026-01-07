# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TelephonySettingsParam", "NoiseSuppressionConfig"]


class NoiseSuppressionConfig(TypedDict, total=False):
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    attenuation_limit: int
    """Attenuation limit for noise suppression. Range: 0-100."""

    mode: Literal["advanced"]
    """Mode for noise suppression configuration."""


class TelephonySettingsParam(TypedDict, total=False):
    default_texml_app_id: str
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    noise_suppression: Literal["deepfilternet", "disabled"]
    """The noise suppression engine to use.

    Use 'disabled' to turn off noise suppression.
    """

    noise_suppression_config: NoiseSuppressionConfig
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    supports_unauthenticated_web_calls: bool
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """

    time_limit_secs: int
    """Maximum duration in seconds for the AI assistant to participate on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """
