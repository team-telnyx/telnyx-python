# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SpeechToTextListProvidersParams"]


class SpeechToTextListProvidersParams(TypedDict, total=False):
    provider: Literal["deepgram", "speechmatics", "assemblyai", "xai", "soniox", "azure", "openai", "google", "telnyx"]
    """Filter to entries for a specific STT provider.

    The enum mirrors the providers advertised across the speech-to-text spec
    (including `google` and `telnyx`, which are accepted as WebSocket transcription
    engines). A provider that has no models currently registered for any service
    type will return an empty `data` array rather than an error.
    """

    service_type: Literal["streaming", "file_transcription", "in_call_transcription"]
    """Filter to entries that support the given service type."""
