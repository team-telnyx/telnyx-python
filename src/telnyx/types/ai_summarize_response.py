# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["AISummarizeResponse", "Data"]


class Data(BaseModel):
    summary: str


class AISummarizeResponse(BaseModel):
    data: Data
