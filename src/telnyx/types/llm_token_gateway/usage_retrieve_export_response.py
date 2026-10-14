# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .guardrail_finding import GuardrailFinding

__all__ = [
    "UsageRetrieveExportResponse",
    "Data",
    "DataUsageExportInferenceRequest",
    "DataUsageExportInferenceRequestTimings",
    "DataUsageExportGuardrailEvaluation",
    "Meta",
]


class DataUsageExportInferenceRequestTimings(BaseModel):
    admitted_at: datetime

    completed_at: Optional[datetime] = None

    first_attempt_at: Optional[datetime] = None

    gateway_duration_ms: Optional[int] = None
    """completed_at - admitted_at as recorded by the ledger; not time to first token."""

    settled_at: datetime


class DataUsageExportInferenceRequest(BaseModel):
    id: str
    """Deterministic: req\\__{request_id}\\__r{revision}. Deduplicate on id."""

    attempts: int

    biller: Literal["telnyx", "provider", "none"]

    cache_hit: bool

    configuration_version: int

    cost: Optional[str] = None
    """
    USD decimal string with exactly 6 places, 0 to 1000000000.000000 (the Money
    bound); enforcement basis, not invoice truth.
    """

    end_user_id: Optional[str] = None

    input_tokens: Optional[int] = None

    metadata: Dict[str, Union[str, int, bool]]
    """Customer request tags captured at admission; {} when untagged."""

    model: str

    output_tokens: Optional[int] = None

    protocol: Literal["openai", "anthropic"]

    provider: str

    provider_key_id: Optional[str] = None

    provider_model: str

    rate_version: str

    request_id: str

    revision: int

    route_mode: Literal["managed", "byok", "cache"]

    schema_version: Literal[1]

    status: Literal["succeeded", "failed", "partial", "unknown"]

    stream: bool

    supersedes: Optional[str] = None
    """Previous revision id; keep the highest revision per request_id."""

    timings: DataUsageExportInferenceRequestTimings

    token_group_id: str

    token_key_id: str

    token_user_id: Optional[str] = None

    type: Literal["inference.request"]

    usage_source: Optional[Literal["provider", "gateway_tokenizer", "operator"]] = None

    usage_status: Literal["known", "unknown", "reconciled"]


class DataUsageExportGuardrailEvaluation(BaseModel):
    id: str

    created_at: datetime

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

    request_id: str

    schema_version: Literal[1]

    stage: Literal["prompt", "response"]

    token_group_id: str

    token_key_id: str

    token_user_id: Optional[str] = None

    type: Literal["guardrail.evaluation"]


Data: TypeAlias = Annotated[
    Union[DataUsageExportInferenceRequest, DataUsageExportGuardrailEvaluation], PropertyInfo(discriminator="type")
]


class Meta(BaseModel):
    has_more: bool

    horizon_lag_seconds: int

    next_cursor: str


class UsageRetrieveExportResponse(BaseModel):
    data: List[Data]

    meta: Meta
