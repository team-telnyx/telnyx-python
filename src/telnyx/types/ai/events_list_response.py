# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel
from .missions.runs.event_data import EventData
from .assistants.tests.test_suites.meta import Meta

__all__ = ["EventsListResponse"]


class EventsListResponse(BaseModel):
    data: List[EventData]

    meta: Meta
