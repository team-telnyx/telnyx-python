# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscriptionSettingsParam", "Challenger", "FallbackModel"]


class Challenger(TypedDict, total=False):
    """
    A second speech-to-text model that transcribes alongside `transcription.model`, and the rule that decides which transcript the assistant uses.
    """

    model: Required[
        Literal[
            "deepgram/flux",
            "deepgram/nova-3",
            "deepgram/nova-2",
            "azure/fast",
            "assemblyai/universal-3-5-pro",
            "assemblyai/universal-streaming",
            "xai/grok-stt",
            "soniox/stt-rt-v4",
            "soniox/stt-rt-v5",
            "nvidia/parakeet-v3",
            "omi-health/omi-med-stt-v1",
            "humain/realtime",
            "reson8/turns",
            "cohere/ar-stt",
            "telnyx/basira",
            "distil-whisper/distil-large-v2",
            "openai/whisper-large-v3-turbo",
        ]
    ]
    """The language booster's model.

    It must be the same kind of model as `transcription.model`: both streaming
    (`deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`,
    `assemblyai/universal-3-5-pro` or its legacy alias
    `assemblyai/universal-streaming`, `xai/grok-stt`, `soniox/stt-rt-v4`,
    `soniox/stt-rt-v5`, `humain/realtime`, `reson8/turns`) or both non-streaming
    (`azure/fast`, `nvidia/parakeet-v3`, `omi-health/omi-med-stt-v1`,
    `cohere/ar-stt`, `distil-whisper/distil-large-v2`,
    `openai/whisper-large-v3-turbo`, `telnyx/basira`). It can be the same model as
    `transcription.model` on a different `language`.
    """

    language: Optional[str]
    """The language this model transcribes.

    Omit it or set it to `null` to use the language of `transcription.model`. The
    request is rejected when this model doesn't support the language it would run.
    It is also rejected when it would run the same model on the same language as
    `transcription.model`.
    """

    rule: Literal["best_turn", "best_engine", "merge_words"]
    """How the assistant picks the transcript it uses.

    The models are compared on how complete and confident their transcripts are, not
    on language, so the rules work best when both models understand the callers'
    language.

    - `best_turn` (default): both models transcribe the whole call. Each turn uses
      the language booster's transcript only when it scores higher than the
      transcript of `transcription.model` (clearly higher with non-streaming
      models). With streaming models, `transcription.model` also decides when each
      turn ends. Available for every pair.
    - `best_engine`: both models transcribe the first turns, then the call continues
      alone on the model whose transcripts scored higher. If neither clearly leads,
      `transcription.model` continues. Streaming models only.
    - `merge_words`: both models transcribe each utterance and their words are
      merged, keeping Arabic and English spoken in the same sentence. Available only
      for `telnyx/basira` with `cohere/ar-stt`, in either order. The pair runs on
      the language that applies to `telnyx/basira` (its own, or that of
      `transcription.model`), which must be Arabic (`ar` or an `ar-` locale),
      `multi`, or `auto`.
    """

    settings: Optional["TranscriptionSettingsConfigParam"]
    """
    Settings for the language booster, with the same fields and limits as
    `transcription.settings`. Fields that don't apply to this model's provider are
    dropped, and the provider's defaults fill in the rest. Omit it or set it to
    `null` to use the settings of `transcription.model` where they apply to this
    model.
    """


class FallbackModel(TypedDict, total=False):
    """
    A streaming speech-to-text model that takes over transcription when the model in use fails.
    """

    model: Required[
        Literal[
            "deepgram/flux",
            "deepgram/nova-3",
            "deepgram/nova-2",
            "assemblyai/universal-3-5-pro",
            "assemblyai/universal-streaming",
            "xai/grok-stt",
            "soniox/stt-rt-v4",
            "soniox/stt-rt-v5",
            "humain/realtime",
            "reson8/turns",
        ]
    ]
    """The fallback model.

    It must be a streaming model other than `transcription.model` and the other
    fallbacks: `deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`,
    `assemblyai/universal-3-5-pro` (or its legacy alias
    `assemblyai/universal-streaming`), `xai/grok-stt`, `soniox/stt-rt-v4`,
    `soniox/stt-rt-v5`, `humain/realtime`, or `reson8/turns`.
    """

    language: Optional[str]
    """The language the fallback transcribes.

    Omit it or set it to `null` to use the language of `transcription.model`. The
    request is rejected when the fallback model doesn't support the language it
    would run.
    """

    settings: Optional["TranscriptionSettingsConfigParam"]
    """
    Settings for the fallback, with the same fields and limits as
    `transcription.settings`. Fields that don't apply to this model's provider are
    dropped, and the provider's defaults fill in the rest. Omit it or set it to
    `null` to use the settings of `transcription.model` where they apply to this
    model.
    """


class TranscriptionSettingsParam(TypedDict, total=False):
    api_key_ref: str
    """Integration secret identifier for the transcription provider API key.

    Currently used for Azure transcription regions that require a customer-provided
    API key.
    """

    challenger: Optional[Challenger]
    """
    A second speech-to-text model that transcribes alongside `transcription.model`,
    and the rule that decides which transcript the assistant uses.
    """

    fallback_models: Optional[Iterable[FallbackModel]]
    """
    Up to 3 streaming models that take over transcription, in this order, when the
    model in use fails, at the start of a call or mid-call. `model` must be a
    streaming model too, and must support `language` alongside other models. On
    update, a list replaces the stored one: omit the field to keep the stored list,
    or send `null` or `[]` to remove it. When an update changes `model` or
    `language`, stored fallbacks that no longer fit are removed without an error.
    Can't be combined with `challenger`, the language booster; to replace a stored
    language booster, send `challenger: null` in the same request.
    """

    language: str
    """The language of the audio to be transcribed.

    If not set, or if set to `auto`, supported models will automatically detect the
    language. For `deepgram/flux`, supported values are: `auto` (Telnyx language
    detection controls the language hint), `multi` (no language hint), and
    language-specific hints `en`, `es`, `fr`, `de`, `hi`, `ru`, `pt`, `ja`, `it`,
    and `nl`. For `soniox/stt-rt-v4` and `soniox/stt-rt-v5`, `auto` omits the
    language hint and lets Soniox auto-detect; ISO 639-1 codes (e.g. `en`, `es`)
    bias detection toward that language; `settings.language_hints` can pin multiple
    languages at once instead. For `humain/realtime`, supported values are `ar`,
    `en`, `codeswitch` (Arabic/English code-switching), and `auto` (resolves
    server-side to code-switching). Unlike other models, `humain/realtime` does not
    fall back to `auto` when `language` is omitted — omitting it applies `en`
    instead. For `reson8/turns`, supported values are `auto` (or unset) for
    automatic language detection, and the language codes `nl`, `en`, `fr`, `fy`,
    `de`, `it`, `pl`, `pt`, `es`, and `sv` to fix the transcription language. For
    `cohere/ar-stt`, supported values are `ar` and `en`; unlike other models, this
    model does not auto-detect and defaults to `ar` when `language` is omitted.
    """

    model: Literal[
        "deepgram/flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
        "azure/fast",
        "assemblyai/universal-3-5-pro",
        "assemblyai/universal-streaming",
        "xai/grok-stt",
        "soniox/stt-rt-v4",
        "soniox/stt-rt-v5",
        "nvidia/parakeet-v3",
        "omi-health/omi-med-stt-v1",
        "humain/realtime",
        "reson8/turns",
        "cohere/ar-stt",
        "telnyx/basira",
        "distil-whisper/distil-large-v2",
        "openai/whisper-large-v3-turbo",
    ]
    """The speech to text model to be used by the voice assistant.

    All Deepgram models are run on-premise.

    - `deepgram/flux` is optimized for turn-taking with multilingual language hints.
    - `deepgram/nova-3` is multilingual with automatic language detection.
    - `deepgram/nova-2` is Deepgram's previous-generation multilingual model.
    - `azure/fast` is a multilingual Azure transcription model.
    - `assemblyai/universal-3-5-pro` is a multilingual streaming model with
      configurable turn detection. The legacy alias `assemblyai/universal-streaming`
      is still accepted and resolves to the same model.
    - `xai/grok-stt` is a multilingual Grok STT model.
    - `soniox/stt-rt-v4` and `soniox/stt-rt-v5` are multilingual streaming models
      with automatic language detection, configurable endpointing, term biasing
      (`context`), and `language_hints`.
    - `nvidia/parakeet-v3` is a multilingual transcription model with automatic
      language detection.
    - `omi-health/omi-med-stt-v1` is an English-only medical transcription model
      (Parakeet-based).
    - `humain/realtime` is a streaming model with native Arabic and Arabic/English
      code-switching support.
    - `reson8/turns` is a turn-based streaming model covering 10 European languages
      with automatic language detection.
    - `cohere/ar-stt` is a non-streaming Arabic and English transcription model.
    - `telnyx/basira` is a non-streaming Arabic transcription model.
    """

    region: str
    """
    Region on third party cloud providers (currently Azure) if using one of their
    models. Some regions require `api_key_ref`.
    """

    settings: "TranscriptionSettingsConfigParam"


from .transcription_settings_config_param import TranscriptionSettingsConfigParam
