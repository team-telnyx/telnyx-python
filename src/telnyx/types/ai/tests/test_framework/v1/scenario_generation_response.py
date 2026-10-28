# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_models import BaseModel

__all__ = ["ScenarioGenerationResponse"]


class ScenarioGenerationResponse(BaseModel):
    progress_id: str
    """Identifier to poll generation progress with."""
