# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .calendar_connection import CalendarConnection

__all__ = ["CalendarConnectionResponse"]


class CalendarConnectionResponse(BaseModel):
    data: CalendarConnection
