# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .transcription import Transcription

__all__ = ["TranscriptionWebhookEvent"]


class TranscriptionWebhookEvent(BaseModel):
    data: Optional[Transcription] = None
