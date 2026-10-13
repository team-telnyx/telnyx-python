# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SpendRetrieveEventsResponse", "Data", "Meta"]


class Data(BaseModel):
    id: str

    attempts: int
    """Provider attempts begun for the request (fallbacks included); 0 for a cache hit.

    Token and cost totals sum every attempt.
    """

    biller: Literal["telnyx", "provider", "none"]

    cache_hit: bool

    configuration_version: int

    cost: Optional[float] = None
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    created_at: datetime

    end_user_id: Optional[str] = None

    input_tokens: Optional[int] = None

    metadata: Dict[str, Union[str, int, bool]]
    """Customer request tags from the x-ltg-metadata header: up to 5 entries.

    Keys are case-sensitive; keys starting with ltg*, telnyx*, litellm* or cf* (any
    case) are reserved. Values are strings (1-256 characters, no control or format
    characters), integers within +/-9007199254740991, or booleans; floats, null,
    objects and arrays are rejected. Values that look like credentials are rejected.
    Tags are attribution only: never forwarded upstream, never part of the response
    cache key, never used for budgets or routing. An untagged request reports {}.
    """

    model: str
    """
    Public alias that served (the last attempt); rate_version, biller and
    provider_key_id follow it.
    """

    output_tokens: Optional[int] = None

    provider_key_id: Optional[str] = None

    rate_version: str

    request_id: str

    requested_model: str
    """
    Public alias the caller requested; differs from model only when a group fallback
    served.
    """

    reservation_micro_usd: int

    status: Literal["succeeded", "failed", "partial", "unknown"]

    token_group_id: str

    token_key_id: str

    token_user_id: Optional[str] = None

    usage_status: Literal["known", "unknown", "reconciled"]


class Meta(BaseModel):
    has_more: bool

    page_number: int

    page_size: int

    snapshot: str


class SpendRetrieveEventsResponse(BaseModel):
    data: List[Data]

    meta: Meta
