# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .inbox_filters import InboxFilters

__all__ = ["FilterReplaceResponse"]


class FilterReplaceResponse(BaseModel):
    data: InboxFilters
