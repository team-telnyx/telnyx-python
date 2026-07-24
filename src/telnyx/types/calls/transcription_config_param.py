# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TranscriptionConfigParam"]


class TranscriptionConfigParam(TypedDict, total=False):
    """The settings associated with speech to text for the voice assistant.

    This is only relevant if the assistant uses a text-to-text language model. Any assistant using a model with native audio support (e.g. `fixie-ai/ultravox-v0_4`) will ignore this field.
    """

    language: str
    """The language of the audio to be transcribed.

    If not set, or if set to `auto`, supported models will automatically detect the
    language. Supported and meaningful values depend on the selected transcription
    `model`. For `deepgram/flux`, supported values are: `auto` (Telnyx language
    detection controls the language hint), `multi` (no language hint), and
    language-specific hints `en`, `es`, `fr`, `de`, `hi`, `ru`, `pt`, `ja`, `it`,
    and `nl`. For `soniox/stt-rt-v4`, `auto` omits the language hint and lets Soniox
    auto-detect; ISO 639-1 codes (e.g. `en`, `es`) bias detection toward that
    language. For `assemblyai/universal-streaming`, `auto` (or unset) enables native
    multilingual code-switching; ISO 639-1 codes (`en`, `es`, `de`, `fr`, `pt`,
    `it`, `tr`, `nl`, `sv`, `no`, `da`, `fi`, `hi`, `vi`, `ar`, `he`, `ja`, `zh`)
    bias the session to that language. For `humain/realtime`, supported values are
    `ar`, `en`, `codeswitch` (Arabic/English code-switching), and `auto` (resolves
    server-side to code-switching). Unlike other models, `humain/realtime` does not
    fall back to `auto` when `language` is omitted — omitting it applies `en`
    instead.
    """

    model: Literal[
        "deepgram/flux",
        "flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
        "speechmatics/standard",
        "speechmatics/enhanced",
        "assemblyai/universal-streaming",
        "xai/grok-stt",
        "soniox/stt-rt-v4",
        "nvidia/parakeet-v3",
        "humain/realtime",
        "azure/fast",
        "azure/realtime",
        "google/latest_long",
        "distil-whisper/distil-large-v2",
        "openai/whisper-large-v3-turbo",
    ]
    """The speech to text model to be used by the voice assistant.

    Supported models include:

    - `deepgram/flux` (or `flux`) for live streaming turn-taking.
    - `deepgram/nova-3` and `deepgram/nova-2` for live streaming transcription.
    - `speechmatics/standard` and `speechmatics/enhanced` for live streaming
      transcription.
    - `assemblyai/universal-streaming` for live streaming transcription.
    - `xai/grok-stt` for live streaming transcription.
    - `soniox/stt-rt-v4` for live streaming multilingual transcription with
      automatic language detection.
    - `nvidia/parakeet-v3` for multilingual transcription with automatic language
      detection.
    - `humain/realtime` for live streaming transcription with native Arabic and
      Arabic/English code-switching support.
    - `azure/fast` and `azure/realtime`; Azure models require `region`, and
      unsupported regions require `api_key_ref`.
    - `google/latest_long` for non-streaming multilingual transcription.
    - `distil-whisper/distil-large-v2` for lower-latency English-only non-streaming
      transcription.
    - `openai/whisper-large-v3-turbo` for multilingual non-streaming transcription
      with automatic language detection.
    """
