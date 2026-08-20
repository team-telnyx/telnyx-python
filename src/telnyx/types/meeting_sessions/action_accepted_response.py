# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ActionAcceptedResponse", "Data"]


class Data(BaseModel):
    accepted: bool


class ActionAcceptedResponse(BaseModel):
    data: Data
