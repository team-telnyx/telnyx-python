# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TextToSpeechListVoicesResponse", "Voice"]


class Voice(BaseModel):
    id: Optional[str] = None

    accent: Optional[str] = None

    age: Optional[str] = None

    gender: Optional[str] = None

    label: Optional[str] = None

    language: Optional[str] = None

    name: Optional[str] = None

    provider: Optional[str] = None


class TextToSpeechListVoicesResponse(BaseModel):
    voices: Optional[List[Voice]] = None
