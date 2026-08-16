# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .web_search_result import WebSearchResult

__all__ = ["WebSearchCreateResponse", "Data", "DataResults"]


class DataResults(BaseModel):
    web: List[WebSearchResult]
    """Web search results."""

    news: Optional[List[WebSearchResult]] = None
    """News search results. Present only when the query surfaces news results."""


class Data(BaseModel):
    results: Optional[DataResults] = None


class WebSearchCreateResponse(BaseModel):
    data: Optional[Data] = None
