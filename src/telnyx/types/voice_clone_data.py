# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VoiceCloneData"]


class VoiceCloneData(BaseModel):
    """A voice clone object."""

    id: Optional[str] = None
    """Unique identifier for the voice clone."""

    created_at: Optional[datetime] = None
    """Timestamp when the voice clone was created."""

    gender: Optional[Literal["male", "female", "neutral"]] = None
    """Gender of the voice clone."""

    label: Optional[str] = None
    """Voice style description.

    If not explicitly set on upload, falls back to the source design's prompt text.
    """

    language: Optional[str] = None
    """ISO 639-1 language code of the voice clone."""

    api_model_id: Optional[Literal["Qwen3TTS", "Ultra", "speech-2.8-turbo"]] = FieldInfo(alias="model_id", default=None)
    """TTS model identifier for the voice clone."""

    name: Optional[str] = None
    """Name of the voice clone."""

    provider: Optional[Literal["telnyx", "minimax"]] = None
    """Voice synthesis provider used for this clone."""

    provider_supported_models: Optional[List[str]] = None
    """List of TTS model identifiers supported by this clone's provider."""

    provider_voice_id: Optional[str] = None
    """Provider-specific voice identifier used for TTS synthesis.

    May differ from the clone UUID depending on the provider and model.
    """

    record_type: Optional[Literal["voice_clone"]] = None
    """Identifies the resource type."""

    source_voice_design_id: Optional[str] = None
    """UUID of the source voice design. `null` for upload-based clones."""

    source_voice_design_version: Optional[int] = None
    """Version of the source voice design used. `null` for upload-based clones."""

    status: Optional[Literal["active", "pending", "failed", "expired"]] = None
    """Clone status.

    pending for Ultra clones while on-prem import is in progress, active once ready,
    failed if verification timed out, expired if not kept alive.
    """

    updated_at: Optional[datetime] = None
    """Timestamp when the voice clone was last updated."""
