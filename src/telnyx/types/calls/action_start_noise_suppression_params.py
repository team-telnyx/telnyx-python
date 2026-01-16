# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionStartNoiseSuppressionParams", "NoiseSuppressionEngineConfig"]


class ActionStartNoiseSuppressionParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    direction: Literal["inbound", "outbound", "both"]
    """The direction of the audio stream to be noise suppressed."""

    noise_suppression_engine: Literal["Denoiser", "DeepFilterNet", "Krisp"]
    """
    The engine to use for noise suppression. For backward compatibility, engines A,
    B, and C are also supported, but are deprecated: A - Denoiser B - DeepFilterNet
    C - Krisp
    """

    noise_suppression_engine_config: NoiseSuppressionEngineConfig
    """Configuration parameters for noise suppression engines."""


class NoiseSuppressionEngineConfig(TypedDict, total=False):
    """Configuration parameters for noise suppression engines."""

    attenuation_limit: int
    """The attenuation limit for noise suppression (0-100).

    Only applicable for DeepFilterNet.
    """
