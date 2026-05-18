# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TranscriptionSettingsConfig"]


class TranscriptionSettingsConfig(BaseModel):
    eager_eot_threshold: Optional[float] = None
    """Available only for deepgram/flux.

    Confidence threshold for eager end of turn detection. Must be lower than or
    equal to eot_threshold. Setting this equal to eot_threshold effectively disables
    eager end of turn.
    """

    enable_endpoint_detection: Optional[bool] = None
    """Available only for soniox/stt-rt-v4.

    When true, Soniox emits end-of-utterance events at the cadence configured by
    `max_endpoint_delay_ms`.
    """

    end_of_turn_confidence_threshold: Optional[float] = None
    """Available only for assemblyai/universal-streaming.

    Confidence level required to trigger an end of turn. Higher values require more
    certainty before ending a turn.
    """

    eot_threshold: Optional[float] = None
    """Available only for deepgram/flux.

    Confidence required to trigger an end of turn. Higher values = more reliable
    turn detection but slightly increased latency.
    """

    eot_timeout_ms: Optional[int] = None
    """Available only for deepgram/flux.

    Maximum milliseconds of silence before forcing an end of turn, regardless of
    confidence.
    """

    interim_results: Optional[bool] = None
    """Available only for soniox/stt-rt-v4.

    When true, Soniox streams interim (non-final) results in addition to finalized
    transcripts.
    """

    keyterm: Optional[str] = None
    """Available only for deepgram/nova-3 and deepgram/flux.

    A comma-separated list of key terms to boost for recognition during
    transcription. Helps improve accuracy for domain-specific terminology, proper
    nouns, or uncommon words. This field may be templated with
    [dynamic variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables)
    using mustache syntax (e.g. `Telnyx,{{customer_name}},VoIP`). Variables are
    resolved at call time before the value is sent to the speech-to-text engine.
    """

    max_endpoint_delay_ms: Optional[int] = None
    """Available only for soniox/stt-rt-v4.

    Maximum silence (in milliseconds) before Soniox emits an end-of-utterance event.
    Only honored when `enable_endpoint_detection` is true.
    """

    max_turn_silence: Optional[int] = None
    """Available only for assemblyai/universal-streaming.

    Maximum duration of silence in milliseconds before forcing an end of turn.
    """

    min_turn_silence: Optional[int] = None
    """Available only for assemblyai/universal-streaming.

    Minimum duration of silence in milliseconds before a turn can end. Must be less
    than or equal to max_turn_silence.
    """

    numerals: Optional[bool] = None

    smart_format: Optional[bool] = None
