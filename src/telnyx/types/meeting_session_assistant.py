# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MeetingSessionAssistant"]


class MeetingSessionAssistant(BaseModel):
    id: str
    """Identifier of the assistant."""

    audio_gate: Literal["half_duplex", "full_duplex"]
    """Audio gating strategy in force for the assistant call leg."""

    leave_on_end: bool
    """Whether the bot leaves when the Assistant's conversation ends or fails."""

    dynamic_variables: Optional[Dict[str, str]] = None
    """Dynamic variables in individual-session responses; null when none were supplied.

    Omitted from session list items.
    """
