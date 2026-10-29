# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionSettingsParam"]


class TranscriptionSettingsParam(TypedDict, total=False):
    api_key_ref: str
    """Integration secret identifier for the transcription provider API key.

    Currently used for Azure transcription regions that require a customer-provided
    API key.
    """

    challenger: Optional["TranscriptionChallengerParam"]
    """
    A second speech-to-text model that transcribes alongside `transcription.model`,
    and the rule that decides which transcript the assistant uses.
    """

    fallback_models: Optional[Iterable["TranscriptionFallbackModelParam"]]
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
    model does not auto-detect and defaults to `ar` when `language` is omitted. For
    `speechmatics/linden-1`, there is no auto-detect; set a code from Speechmatics'
    Realtime language list (67 language codes, including `es-bilingual-en` for
    Spanish and English bilingual, and the spelling and script variants `en-US`,
    `en-GB`, `en-AU`, `cmn-Hans`, and `cmn-Hant`; `en` alone uses the default
    spelling); unset defaults to `en`, while an explicit `auto`, `auto_beta`, or
    `multi` is rejected with a 400.
    """

    model: Literal[
        "deepgram/flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
        "speechmatics/standard",
        "speechmatics/linden-1",
        "azure/fast",
        "assemblyai/universal-3-6-pro",
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
    - `speechmatics/standard` is a Speechmatics model self-hosted by Telnyx; it
      supports a fixed set of language packs (including bilingual packs such as
      `ar_en`) and defaults to `en`.
    - `speechmatics/linden-1` (preview) is a vendor-hosted streaming model with no
      auto-detect; set `language` from Speechmatics' Realtime language list
      (defaults to `en`).
    - `azure/fast` is a multilingual Azure transcription model.
    - `assemblyai/universal-3-6-pro` (AssemblyAI Universal-3.6 Pro) is a
      multilingual streaming model with configurable turn detection. The legacy
      aliases `assemblyai/universal-3-5-pro` and `assemblyai/universal-streaming`
      are still accepted and run the same model.
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


from .transcription_challenger_param import TranscriptionChallengerParam
from .transcription_fallback_model_param import TranscriptionFallbackModelParam
from .transcription_settings_config_param import TranscriptionSettingsConfigParam
