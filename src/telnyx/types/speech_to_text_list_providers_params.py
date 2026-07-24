# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .stt_service_type import SttServiceType

__all__ = ["SpeechToTextListProvidersParams"]


class SpeechToTextListProvidersParams(TypedDict, total=False):
    provider: Literal[
        "deepgram",
        "speechmatics",
        "assemblyai",
        "xai",
        "soniox",
        "parakeet",
        "humain",
        "azure",
        "openai",
        "google",
        "telnyx",
    ]
    """Filter to entries for a specific STT provider.

    The enum mirrors the providers advertised across the speech-to-text spec
    (including `google` and `telnyx`, which are accepted as WebSocket transcription
    engines). A provider that has no models currently registered for any service
    type will return an empty `data` array rather than an error.
    """

    service_type: SttServiceType
    """Filter to entries that support the given service type.

    For backward compatibility with the values that briefly shipped before the
    product-aligned rename, the legacy aliases `file_transcription`,
    `in_call_transcription`, and `ai_assistant_transcription` are silently accepted
    and normalized to `file_based`, `in_call`, and `ai_assistant` respectively. The
    response always emits the canonical (post-rename) values.
    """
