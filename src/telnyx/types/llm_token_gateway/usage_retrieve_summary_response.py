# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "UsageRetrieveSummaryResponse",
    "Data",
    "DataByDay",
    "DataByModel",
    "DataGuardrails",
    "DataGuardrailsRecentEvent",
    "DataGuardrailsRecentEventFinding",
    "DataTotals",
    "Meta",
]


class DataByDay(BaseModel):
    cache_hits: int
    """Requests served from the gateway cache."""

    date: datetime.date
    """UTC day."""

    failed_requests: int
    """Requests classified as failed."""

    input_tokens: int
    """Independently known input tokens across attempts, including corrected usage."""

    output_tokens: int
    """Independently known output tokens across attempts, including corrected usage."""

    partial_requests: int
    """Requests classified as partial after streaming began."""

    requests: int
    """Number of matching requests."""

    reserved_spend: float
    """Unresolved budget reservations in USD."""

    spend: float
    """Sum of known reference/enforcement cost in USD."""

    succeeded_requests: int
    """Requests classified as succeeded."""

    unknown_requests: int
    """Requests whose cost remains unresolved; unknown cost is excluded from spend."""


class DataByModel(BaseModel):
    cache_hits: int
    """Requests served from the gateway cache."""

    failed_requests: int
    """Requests classified as failed."""

    input_tokens: int
    """Independently known input tokens across attempts, including corrected usage."""

    model: str
    """Model identifier."""

    output_tokens: int
    """Independently known output tokens across attempts, including corrected usage."""

    partial_requests: int
    """Requests classified as partial after streaming began."""

    requests: int
    """Number of matching requests."""

    reserved_spend: float
    """Unresolved budget reservations in USD."""

    spend: float
    """Sum of known reference/enforcement cost in USD."""

    succeeded_requests: int
    """Requests classified as succeeded."""

    unknown_requests: int
    """Requests whose cost remains unresolved; unknown cost is excluded from spend."""


class DataGuardrailsRecentEventFinding(BaseModel):
    action: Literal["flag", "block"]

    code: str

    count: int

    detector: Literal["secrets", "dlp", "safety"]


class DataGuardrailsRecentEvent(BaseModel):
    id: str

    created_at: datetime.datetime

    end_user_id: Optional[str] = None

    evaluation_input_tokens: Optional[int] = None

    evaluation_output_tokens: Optional[int] = None

    findings: List[DataGuardrailsRecentEventFinding]

    model: str
    """Model identifier."""

    outcome: Literal["evaluated", "flagged", "blocked", "unevaluated"]

    record_type: Literal["guardrail_event"]

    request_id: str

    stage: Literal["prompt", "response"]

    token_group_id: str

    token_key_id: str

    token_user_id: Optional[str] = None


class DataGuardrails(BaseModel):
    """
    Complete guardrail event counts and bounded recent findings for the same group and range.
    """

    blocked_events: int
    """Total blocked guardrail events, not distinct requests."""

    flagged_events: int
    """Total flagged guardrail events, not distinct requests."""

    recent_events: List[DataGuardrailsRecentEvent]
    """
    Up to 20 newest privacy-safe guardrail events, ordered by creation time
    descending and event ID.
    """


class DataTotals(BaseModel):
    """Metrics for all matching requests."""

    cache_hits: int
    """Requests served from the gateway cache."""

    failed_requests: int
    """Requests classified as failed."""

    input_tokens: int
    """Independently known input tokens across attempts, including corrected usage."""

    output_tokens: int
    """Independently known output tokens across attempts, including corrected usage."""

    partial_requests: int
    """Requests classified as partial after streaming began."""

    requests: int
    """Number of matching requests."""

    reserved_spend: float
    """Unresolved budget reservations in USD."""

    spend: float
    """Sum of known reference/enforcement cost in USD."""

    succeeded_requests: int
    """Requests classified as succeeded."""

    unknown_requests: int
    """Requests whose cost remains unresolved; unknown cost is excluded from spend."""


class Data(BaseModel):
    by_day: List[DataByDay]
    """One row per UTC day, including zero-activity days."""

    by_model: List[DataByModel]
    """One row per model, ordered by request count descending then model name."""

    guardrails: DataGuardrails
    """
    Complete guardrail event counts and bounded recent findings for the same group
    and range.
    """

    totals: DataTotals
    """Metrics for all matching requests."""


class Meta(BaseModel):
    end_date: datetime.date

    start_date: datetime.date

    token_group_id: str


class UsageRetrieveSummaryResponse(BaseModel):
    data: Data

    meta: Meta
