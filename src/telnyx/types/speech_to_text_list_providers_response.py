# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .stt_service_type import SttServiceType

__all__ = ["SpeechToTextListProvidersResponse", "Data", "DataServiceType", "Meta"]


class DataServiceType(BaseModel):
    """
    A supported service surface for a given (provider, model), along with the language codes accepted on that surface. Language support can differ per surface — for example, a model may accept a narrower language set for streaming than for file transcription.
    """

    languages: List[str]
    """Languages accepted on this service surface, in the provider's native code
    format.

    `auto` indicates the provider performs language detection.
    """

    type: SttServiceType
    """Service surface a model is available on.

    `ai_assistant` is the STT surface configured via Call Control voice-assistant
    transcription; it covers both live-streaming and non-streaming/batch models
    (matching the `TranscriptionConfig.model` enum on `call-control` voice
    assistants).
    """


class Data(BaseModel):
    """A (provider, model) tuple along with the service surfaces it supports.

    Each entry in `service_types` describes one surface and the languages accepted on it.
    """

    model: str
    """Provider-scoped model name."""

    provider: str
    """STT provider name."""

    service_types: List[DataServiceType]
    """Service surfaces this (provider, model) supports.

    When the request filters by `service_type`, only the matching nested entry is
    returned for each matching model.
    """


class Meta(BaseModel):
    total: int
    """Total number of entries returned."""


class SpeechToTextListProvidersResponse(BaseModel):
    """List of supported STT providers and models."""

    data: List[Data]

    meta: Meta
