# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["NoiseSuppressionEngineListResponse", "Data"]


class Data(BaseModel):
    """A noise suppression engine available to the authenticated user."""

    default_attenuation_level: int
    """Default attenuation level of the engine (0-100, in multiples of ten)."""

    label: str
    """Human-readable name of the engine."""

    value: str
    """
    Machine-readable identifier of the engine, used when configuring noise
    suppression.
    """


class NoiseSuppressionEngineListResponse(BaseModel):
    data: List[Data]
