# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_models import BaseModel

__all__ = ["ScenarioRunScenariosResponse"]


class ScenarioRunScenariosResponse(BaseModel):
    id: int
    """ID of the created test-run batch whose results can be polled."""

    status: str
    """Initial status of the run batch."""
