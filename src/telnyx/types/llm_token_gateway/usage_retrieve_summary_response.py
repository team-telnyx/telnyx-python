# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .guardrail_finding import GuardrailFinding

__all__ = [
    "UsageRetrieveSummaryResponse",
    "Data",
    "DataByDay",
    "DataByModel",
    "DataGuardrails",
    "DataGuardrailsRecentEvent",
    "DataTotals",
    "Meta",
]


class DataByDay(BaseModel):
    cache_hits: int

    date: datetime.date

    failed_requests: int

    input_tokens: int

    output_tokens: int

    partial_requests: int

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

    succeeded_requests: int

    unknown_requests: int


class DataByModel(BaseModel):
    cache_hits: int

    failed_requests: int

    input_tokens: int

    model: str

    output_tokens: int

    partial_requests: int

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

    succeeded_requests: int

    unknown_requests: int


class DataGuardrailsRecentEvent(BaseModel):
    id: str

    created_at: datetime.datetime

    end_user_id: Optional[str] = None

    evaluation_input_tokens: Optional[int] = None

    evaluation_output_tokens: Optional[int] = None

    findings: List[GuardrailFinding]

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

    outcome: Literal["evaluated", "flagged", "blocked", "unevaluated"]

    record_type: Literal["guardrail_event"]

    request_id: str

    stage: Literal["prompt", "response"]

    token_group_id: str

    token_key_id: str

    token_user_id: Optional[str] = None


class DataGuardrails(BaseModel):
    blocked_events: int

    flagged_events: int

    recent_events: List[DataGuardrailsRecentEvent]


class DataTotals(BaseModel):
    cache_hits: int

    failed_requests: int

    input_tokens: int

    output_tokens: int

    partial_requests: int

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

    succeeded_requests: int

    unknown_requests: int


class Data(BaseModel):
    by_day: List[DataByDay]

    by_model: List[DataByModel]

    guardrails: DataGuardrails

    totals: DataTotals


class Meta(BaseModel):
    end_date: datetime.date

    metadata: Dict[str, str]
    """The metadata[<key>] filters applied to every section; {} when unfiltered."""

    start_date: datetime.date

    token_group_id: str


class UsageRetrieveSummaryResponse(BaseModel):
    data: Data

    meta: Meta
