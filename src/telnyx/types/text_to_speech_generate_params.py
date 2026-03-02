# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["TextToSpeechGenerateParams", "Aws", "Azure", "Elevenlabs", "Minimax", "Resemble", "Rime", "Telnyx"]


class TextToSpeechGenerateParams(TypedDict, total=False):
    aws: Aws
    """AWS Polly provider-specific parameters."""

    azure: Azure
    """Azure Cognitive Services provider-specific parameters."""

    disable_cache: bool
    """When `true`, bypass the audio cache and generate fresh audio."""

    elevenlabs: Elevenlabs
    """ElevenLabs provider-specific parameters."""

    language: str
    """Language code (e.g. `en-US`). Usage varies by provider."""

    minimax: Minimax
    """Minimax provider-specific parameters."""

    output_type: Literal["binary_output", "base64_output"]
    """Determines the response format.

    `binary_output` returns raw audio bytes, `base64_output` returns base64-encoded
    audio in JSON.
    """

    provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble"]
    """TTS provider. Required unless `voice` is provided."""

    resemble: Resemble
    """Resemble AI provider-specific parameters."""

    rime: Rime
    """Rime provider-specific parameters."""

    telnyx: Telnyx
    """Telnyx provider-specific parameters."""

    text: str
    """The text to convert to speech."""

    text_type: Literal["text", "ssml"]
    """Text type. Use `ssml` for SSML-formatted input (supported by AWS and Azure)."""

    voice: str
    """
    Voice identifier in the format `provider.model_id.voice_id` or
    `provider.voice_id`. Examples: `telnyx.NaturalHD.Alloy`,
    `azure.en-US-AvaMultilingualNeural`, `aws.Polly.Generative.Lucia`. When
    provided, `provider`, `model_id`, and `voice_id` are extracted automatically and
    take precedence over individual parameters.
    """

    voice_settings: Dict[str, object]
    """Provider-specific voice settings.

    Contents vary by provider — see provider-specific parameter objects below.
    """


class Aws(TypedDict, total=False):
    """AWS Polly provider-specific parameters."""

    language_code: str
    """Language code (e.g. `en-US`, `es-ES`)."""

    lexicon_names: SequenceNotStr[str]
    """List of lexicon names to apply."""

    output_format: str
    """Audio output format."""

    sample_rate: str
    """Audio sample rate."""

    text_type: Literal["text", "ssml"]
    """Input text type."""


class Azure(TypedDict, total=False):
    """Azure Cognitive Services provider-specific parameters."""

    api_key: str
    """Custom Azure API key. If not provided, the default Telnyx key is used."""

    deployment_id: str
    """Custom Azure deployment ID."""

    effect: str
    """Azure audio effect to apply."""

    gender: str
    """Voice gender preference."""

    language_code: str
    """Language code (e.g. `en-US`)."""

    output_format: str
    """Azure audio output format."""

    region: str
    """Azure region (e.g. `eastus`, `westeurope`)."""

    text_type: Literal["text", "ssml"]
    """Input text type. Use `ssml` for SSML-formatted input."""


class Elevenlabs(TypedDict, total=False):
    """ElevenLabs provider-specific parameters."""

    api_key: str
    """Custom ElevenLabs API key. If not provided, the default Telnyx key is used."""

    language_code: str
    """Language code."""

    voice_settings: Dict[str, object]
    """ElevenLabs voice settings (stability, similarity_boost, etc.)."""


class Minimax(TypedDict, total=False):
    """Minimax provider-specific parameters."""

    language_boost: str
    """Language code to boost pronunciation for."""

    pitch: int
    """Pitch adjustment."""

    response_format: str
    """Audio output format."""

    speed: float
    """Speech speed multiplier."""

    vol: float
    """Volume level."""


class Resemble(TypedDict, total=False):
    """Resemble AI provider-specific parameters."""

    api_key: str
    """Custom Resemble API key."""

    format: str
    """Audio output format."""

    precision: str
    """Synthesis precision."""

    sample_rate: str
    """Audio sample rate."""


class Rime(TypedDict, total=False):
    """Rime provider-specific parameters."""

    response_format: str
    """Audio output format."""

    sampling_rate: int
    """Audio sampling rate in Hz."""

    voice_speed: float
    """Voice speed multiplier."""


class Telnyx(TypedDict, total=False):
    """Telnyx provider-specific parameters."""

    response_format: str
    """Audio response format."""

    sampling_rate: int
    """Audio sampling rate in Hz."""

    temperature: float
    """Sampling temperature."""

    voice_speed: float
    """Voice speed multiplier."""
