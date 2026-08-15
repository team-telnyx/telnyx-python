# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionAcceptedResponse", "Data"]


class Data(BaseModel):
    accepted: Literal[True]


class ActionAcceptedResponse(BaseModel):
    data: Data
