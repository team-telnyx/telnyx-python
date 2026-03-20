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

    noise_suppression_engine: Literal["Denoiser", "DeepFilterNet", "Krisp", "AiCoustics"]
    """
    The engine to use for noise suppression. For backward compatibility, engines A,
    B, C, and D are also supported, but are deprecated: A - Denoiser B -
    DeepFilterNet C - Krisp D - AiCoustics
    """

    noise_suppression_engine_config: NoiseSuppressionEngineConfig
    """Configuration parameters for noise suppression engines.

    Different engines support different parameters.
    """


class NoiseSuppressionEngineConfig(TypedDict, total=False):
    """Configuration parameters for noise suppression engines.

    Different engines support different parameters.
    """

    attenuation_limit: int
    """The attenuation limit for noise suppression (0-100).

    Only applicable for DeepFilterNet.
    """

    enhancement_level: float
    """Enhancement intensity (0.0-1.0). Only applicable for AiCoustics."""

    family: Literal["sparrow", "quail"]
    """AiCoustics model family.

    'sparrow' optimized for human-to-human calls, 'quail' optimized for Voice
    AI/STT. Only applicable for AiCoustics.
    """

    mode: Literal["standard", "advanced"]
    """Processing mode. Only applicable for DeepFilterNet."""

    model: Literal[
        "krisp-viva-tel-v2.kef", "krisp-viva-tel-lite-v1.kef", "krisp-viva-pro-v1.kef", "krisp-viva-ss-v1.kef"
    ]
    """The Krisp model to use. Only applicable for Krisp."""

    size: Literal["s", "l", "xs", "xxs", "vf_l", "vf_1_1_l"]
    """AiCoustics model size.

    's' and 'l' work with both families. 'xs' and 'xxs' are sparrow-only. 'vf_l' and
    'vf_1_1_l' are quail-only. Only applicable for AiCoustics.
    """

    suppression_level: float
    """Suppression level (0.0-100.0). Only applicable for Krisp."""

    voice_gain: float
    """Voice gain multiplier (0.1-4.0). Only applicable for AiCoustics."""
