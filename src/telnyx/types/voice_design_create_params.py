# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VoiceDesignCreateParams"]


class VoiceDesignCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Natural language description of the voice style, e.g.

    'Speak in a warm, friendly tone with a slight British accent'.
    """

    text: Required[str]
    """Sample text to synthesize for this voice design."""

    language: str
    """Language for synthesis.

    Supported values: Auto, Chinese, English, Japanese, Korean, German, French,
    Russian, Portuguese, Spanish, Italian. Defaults to Auto.
    """

    max_new_tokens: int
    """Maximum number of tokens to generate. Default: 2048."""

    name: str
    """Name for the voice design.

    Required when creating a new design (`voice_design_id` is not provided); ignored
    when adding a version. Cannot be a UUID.
    """

    repetition_penalty: float
    """Repetition penalty to reduce repeated patterns in generated audio.

    Default: 1.05.
    """

    temperature: float
    """Sampling temperature controlling randomness.

    Higher values produce more varied output. Default: 0.9.
    """

    top_k: int
    """Top-k sampling parameter — limits the token vocabulary considered at each step.

    Default: 50.
    """

    top_p: float
    """
    Top-p (nucleus) sampling parameter — cumulative probability cutoff for token
    selection. Default: 1.0.
    """

    voice_design_id: str
    """ID of an existing voice design to add a new version to.

    When provided, a new version is created instead of a new design.
    """
