# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TtsIntegrationRetrieveVoicesResponse", "Voice"]


class Voice(BaseModel):
    voice_id: str
    """Unique in the list; no dots.

    A caller selects the voice as `<engine name>.<voice_id>`.
    """

    gender: Optional[str] = None
    """A display string, for example `male`, `female` or `neutral`."""

    language: Optional[str] = None
    """A BCP-47 tag, at most 35 characters."""

    name: Optional[str] = None
    """A display name."""

    provider: Optional[str] = None
    """A display string."""


class TtsIntegrationRetrieveVoicesResponse(BaseModel):
    voices: List[Voice]
