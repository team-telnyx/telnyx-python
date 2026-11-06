# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transcription_settings_config import TranscriptionSettingsConfig

__all__ = ["TranscriptionChallenger"]


class TranscriptionChallenger(BaseModel):
    """
    A second speech-to-text model that transcribes alongside `transcription.model`, and the rule that decides which transcript the assistant uses.
    """

    model: Literal[
        "deepgram/flux",
        "deepgram/nova-3",
        "deepgram/nova-2",
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
    """The language booster's model.

    It must be the same kind of model as `transcription.model`: both streaming
    (`deepgram/flux`, `deepgram/nova-3`, `deepgram/nova-2`,
    `assemblyai/universal-3-6-pro` or its legacy aliases
    `assemblyai/universal-3-5-pro` and `assemblyai/universal-streaming`,
    `xai/grok-stt`, `soniox/stt-rt-v4`, `soniox/stt-rt-v5`, `humain/realtime`,
    `reson8/turns`) or both non-streaming (`azure/fast`, `nvidia/parakeet-v3`,
    `omi-health/omi-med-stt-v1`, `cohere/ar-stt`, `distil-whisper/distil-large-v2`,
    `openai/whisper-large-v3-turbo`, `telnyx/basira`). It can be the same model as
    `transcription.model` on a different `language`.
    """

    language: Optional[str] = None
    """The language this model transcribes.

    Omit it or set it to `null` to use the language of `transcription.model`. The
    request is rejected when this model doesn't support the language it would run.
    It is also rejected when it would run the same model on the same language as
    `transcription.model`.
    """

    rule: Optional[Literal["best_turn", "best_engine", "merge_words"]] = None
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

    settings: Optional[TranscriptionSettingsConfig] = None
    """
    Settings for the language booster, with the same fields and limits as
    `transcription.settings`. Fields that don't apply to this model's provider are
    dropped, and the provider's defaults fill in the rest. Omit it or set it to
    `null` to use the settings of `transcription.model` where they apply to this
    model.
    """
