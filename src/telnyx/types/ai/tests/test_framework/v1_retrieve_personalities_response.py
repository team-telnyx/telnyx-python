# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ....._models import BaseModel

__all__ = ["V1RetrievePersonalitiesResponse", "V1RetrievePersonalitiesResponseItem"]


class V1RetrievePersonalitiesResponseItem(BaseModel):
    id: int

    end_call_enabled: bool

    language: str
    """ISO language code the simulated caller speaks."""

    name: str
    """Display name of the personality."""

    prompt: str
    """Instructions the simulated caller follows."""

    accent: Optional[str] = None

    background_noise: Optional[str] = None

    background_sound_volume: Optional[float] = None

    effective_voice_volume: Optional[float] = None

    forked_from: Optional[int] = None
    """ID of the personality this one was forked from."""

    generation_config: Optional[object] = None

    interruption_level: Optional[str] = None
    """How aggressively the personality interrupts the assistant."""

    message_plan: Optional[object] = None
    """Idle-timeout plan for messages during a call."""

    network_simulation: Optional[object] = None

    organization: Optional[int] = None

    project: Optional[int] = None

    speed: Union[float, str, None] = None

    start_speaking_plan: Union[float, object, None] = None

    stop_speaking_plan: Optional[object] = None

    voice_volume: Optional[float] = None


V1RetrievePersonalitiesResponse: TypeAlias = List[V1RetrievePersonalitiesResponseItem]
