# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SpeechToTextListProvidersResponse", "Data", "Meta"]


class Data(BaseModel):
    """A (provider, model) tuple along with its supported service types and languages."""

    languages: List[str]
    """Languages this (provider, model) accepts, in the provider's native code format.

    `auto` indicates the provider performs language detection.
    """

    model: str
    """Provider-scoped model name."""

    provider: str
    """STT provider name."""

    service_types: List[Literal["streaming", "file_transcription", "in_call_transcription"]]
    """Service surfaces this (provider, model) supports."""


class Meta(BaseModel):
    total: int
    """Total number of entries returned."""


class SpeechToTextListProvidersResponse(BaseModel):
    """List of supported STT providers and models."""

    data: List[Data]

    meta: Meta
