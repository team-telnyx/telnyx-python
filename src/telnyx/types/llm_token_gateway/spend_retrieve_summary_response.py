# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from .spend_group_by import SpendGroupBy

__all__ = ["SpendRetrieveSummaryResponse", "Data", "Meta"]


class Data(BaseModel):
    dimension_id: Optional[str] = None

    input_tokens: int

    name: Optional[str] = None

    output_tokens: int

    requests: int

    reserved_spend: float
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    spend: float
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    unknown_requests: int

    end_user_id: Optional[str] = None

    metadata_key: Optional[str] = None
    """Present only for group_by=metadata:<key>: the tag key.

    dimension_id is then the tag value in text form (booleans as true/false,
    integers in decimal), or null for requests without the key; name is null.
    """

    token_group_id: Optional[str] = None

    token_key_id: Optional[str] = None

    token_user_id: Optional[str] = None


class Meta(BaseModel):
    end_date: date

    group_by: SpendGroupBy
    """Group by one request tag key.

    Keys starting with ltg*, telnyx*, litellm* or cf* (any case) are rejected.
    """

    has_more: bool

    page_number: int

    page_size: int

    snapshot: str

    start_date: date


class SpendRetrieveSummaryResponse(BaseModel):
    data: List[Data]

    meta: Meta
