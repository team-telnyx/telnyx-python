# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ...._models import BaseModel
from .mission_run_data import MissionRunData
from ..assistants.tests.test_suites.meta import Meta

__all__ = ["MissionRunsListResponse"]


class MissionRunsListResponse(BaseModel):
    data: List[MissionRunData]

    meta: Meta
