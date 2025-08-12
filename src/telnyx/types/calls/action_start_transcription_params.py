# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, TypeAlias, TypedDict

from .google_transcription_language import GoogleTranscriptionLanguage

__all__ = [
    "ActionStartTranscriptionParams",
    "TranscriptionEngineConfig",
    "TranscriptionEngineConfigTranscriptionEngineAConfig",
    "TranscriptionEngineConfigTranscriptionEngineAConfigSpeechContext",
    "TranscriptionEngineConfigTranscriptionEngineBConfig",
]


class ActionStartTranscriptionParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    transcription_engine: Literal["A", "B"]
    """Engine to use for speech recognition. `A` - `Google`, `B` - `Telnyx`."""

    transcription_engine_config: TranscriptionEngineConfig

    transcription_tracks: str
    """Indicates which leg of the call will be transcribed.

    Use `inbound` for the leg that requested the transcription, `outbound` for the
    other leg, and `both` for both legs of the call. Will default to `inbound`.
    """


class TranscriptionEngineConfigTranscriptionEngineAConfigSpeechContext(TypedDict, total=False):
    boost: float
    """Boost factor for the speech context."""

    phrases: List[str]


class TranscriptionEngineConfigTranscriptionEngineAConfig(TypedDict, total=False):
    enable_speaker_diarization: bool
    """Enables speaker diarization."""

    hints: List[str]
    """Hints to improve transcription accuracy."""

    interim_results: bool
    """Whether to send also interim results.

    If set to false, only final results will be sent.
    """

    language: GoogleTranscriptionLanguage
    """Language to use for speech recognition"""

    max_speaker_count: int
    """Defines maximum number of speakers in the conversation."""

    min_speaker_count: int
    """Defines minimum number of speakers in the conversation."""

    model: Literal[
        "latest_long",
        "latest_short",
        "command_and_search",
        "phone_call",
        "video",
        "default",
        "medical_conversation",
        "medical_dictation",
    ]
    """The model to use for transcription."""

    profanity_filter: bool
    """Enables profanity_filter."""

    speech_context: Iterable[TranscriptionEngineConfigTranscriptionEngineAConfigSpeechContext]
    """Speech context to improve transcription accuracy."""

    transcription_engine: Literal["A"]
    """Engine identifier for Google transcription service"""

    use_enhanced: bool
    """Enables enhanced transcription, this works for models `phone_call` and `video`."""


class TranscriptionEngineConfigTranscriptionEngineBConfig(TypedDict, total=False):
    language: Literal[
        "en",
        "zh",
        "de",
        "es",
        "ru",
        "ko",
        "fr",
        "ja",
        "pt",
        "tr",
        "pl",
        "ca",
        "nl",
        "ar",
        "sv",
        "it",
        "id",
        "hi",
        "fi",
        "vi",
        "he",
        "uk",
        "el",
        "ms",
        "cs",
        "ro",
        "da",
        "hu",
        "ta",
        "no",
        "th",
        "ur",
        "hr",
        "bg",
        "lt",
        "la",
        "mi",
        "ml",
        "cy",
        "sk",
        "te",
        "fa",
        "lv",
        "bn",
        "sr",
        "az",
        "sl",
        "kn",
        "et",
        "mk",
        "br",
        "eu",
        "is",
        "hy",
        "ne",
        "mn",
        "bs",
        "kk",
        "sq",
        "sw",
        "gl",
        "mr",
        "pa",
        "si",
        "km",
        "sn",
        "yo",
        "so",
        "af",
        "oc",
        "ka",
        "be",
        "tg",
        "sd",
        "gu",
        "am",
        "yi",
        "lo",
        "uz",
        "fo",
        "ht",
        "ps",
        "tk",
        "nn",
        "mt",
        "sa",
        "lb",
        "my",
        "bo",
        "tl",
        "mg",
        "as",
        "tt",
        "haw",
        "ln",
        "ha",
        "ba",
        "jw",
        "su",
        "auto_detect",
    ]
    """Language to use for speech recognition"""

    transcription_engine: Literal["B"]
    """Engine identifier for Telnyx transcription service"""

    transcription_model: Literal["openai/whisper-tiny", "openai/whisper-large-v3-turbo"]
    """The model to use for transcription."""


TranscriptionEngineConfig: TypeAlias = Union[
    TranscriptionEngineConfigTranscriptionEngineAConfig, TranscriptionEngineConfigTranscriptionEngineBConfig
]
