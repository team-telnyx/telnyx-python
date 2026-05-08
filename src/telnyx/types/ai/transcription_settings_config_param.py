# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscriptionSettingsConfigParam"]


class TranscriptionSettingsConfigParam(TypedDict, total=False):
    eager_eot_threshold: float
    """Available only for deepgram/flux.

    Confidence threshold for eager end of turn detection. Must be lower than or
    equal to eot_threshold. Setting this equal to eot_threshold effectively disables
    eager end of turn.
    """

    end_of_turn_confidence_threshold: float
    """Available only for assemblyai/universal-streaming.

    Confidence level required to trigger an end of turn. Higher values require more
    certainty before ending a turn.
    """

    eot_threshold: float
    """Available only for deepgram/flux.

    Confidence required to trigger an end of turn. Higher values = more reliable
    turn detection but slightly increased latency.
    """

    eot_timeout_ms: int
    """Available only for deepgram/flux.

    Maximum milliseconds of silence before forcing an end of turn, regardless of
    confidence.
    """

    keyterm: str
    """Available only for deepgram/nova-3 and deepgram/flux.

    A comma-separated list of key terms to boost for recognition during
    transcription. Helps improve accuracy for domain-specific terminology, proper
    nouns, or uncommon words. This field may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    using mustache syntax (e.g. `Telnyx,{{customer_name}},VoIP`). Variables are
    resolved at call time before the value is sent to the speech-to-text engine.
    """

    max_turn_silence: int
    """Available only for assemblyai/universal-streaming.

    Maximum duration of silence in milliseconds before forcing an end of turn.
    """

    min_turn_silence: int
    """Available only for assemblyai/universal-streaming.

    Minimum duration of silence in milliseconds before a turn can end. Must be less
    than or equal to max_turn_silence.
    """

    numerals: bool

    smart_format: bool
