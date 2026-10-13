# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TokenGroupUpdateParams", "Guardrails", "GuardrailsDlp", "GuardrailsSecrets", "Retries"]


class TokenGroupUpdateParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    allowed_models: SequenceNotStr[str]

    blocked: bool

    budget_duration: Optional["BudgetDuration"]

    cache_ttl: Optional[int]

    fallbacks: Optional[Dict[str, SequenceNotStr[str]]]
    """Per-group model fallbacks: primary alias -> ordered list of 1..3 other aliases.

    Every key and listed alias must be in allowed_models (a PATCH removing a
    referenced alias is 400); a chain never lists its own key; wildcards are
    rejected. Chains are one level deep (a step's own chain is not expanded).
    Fallback is attempted only for managed routes, only before the first provider
    event is forwarded, and only to steps the key may use; each attempt is reserved
    and recorded. {} and null both disable fallbacks.
    """

    guardrails: Optional[Guardrails]
    """Per-group guardrail policy.

    Missing actions default to ignore. profiles may be listed with both dlp actions
    ignore (staged, inactive) but a non-ignore dlp action requires at least one
    profile. streaming defaults to buffered when any response action is block and
    passthrough otherwise; passthrough with a response block is 400. Findings are
    codes and counts only; content is never stored. The stored form is echoed back
    canonicalised (all actions explicit, profiles sorted); {} is stored as an
    all-ignore policy, null disables.
    """

    max_budget: Optional[float]
    """
    USD, decimal precision at most 6 places; parse exactly to integer micro-USD,
    never binary float accounting.
    """

    max_parallel_requests: Optional[int]
    """Optional maximum concurrent reserved/dispatched cache misses across replicas.

    Null means no concurrency cap. Cache hits do not consume slots; unknown usage
    retains its budget hold without a slot.
    """

    name: str

    provider_key_ids: SequenceNotStr[str]

    retries: Optional[Retries]
    """Per-group same-route retries.

    max_attempts counts the first try of each step (the primary and each fallback)
    and is the ceiling for the x-ltg-max-attempts request header. A step is retried
    only when its attempt definitely did no provider work (connection failure before
    dispatch, or 429/529) before the first provider event; an uncertain failure
    (timeout, 408/500/502/503/504) moves to the next fallback step instead.
    max_attempts x (1 + the longest fallback chain) must not exceed 8, else 400. The
    n-th retry waits retry_delay_ms (constant), retry_delay_ms*n (linear) or
    retry_delay_ms*2^(n-1) (exponential), at most 5 s and never past the request
    deadline, then jittered uniformly down to half that value so concurrent retries
    spread out; a provider Retry-After of at most 5 s is honoured and a longer one
    moves to the next step. request_timeout_ms applies to streaming requests only:
    it bounds each attempt's time to its first provider event and never applies
    after it. Non-stream requests keep the per-attempt hop and idle bounds (their
    headers arrive only with the finished completion). retry_delay_ms and backoff
    are floors for the request knobs. Each planned attempt is reserved (at most 8
    per request); unused reservation is released at settlement. Managed routes only.
    The stored form is echoed back with defaults filled in; null disables retries.
    """

    rpm_limit: Optional[int]

    tpm_limit: Optional[int]


class GuardrailsDlp(TypedDict, total=False):
    profiles: List[Literal["financial", "government_id", "contact"]]

    prompt: Literal["ignore", "flag", "block"]

    response: Literal["ignore", "flag", "block"]


class GuardrailsSecrets(TypedDict, total=False):
    prompt: Literal["ignore", "flag", "block"]

    response: Literal["ignore", "flag", "block"]


class Guardrails(TypedDict, total=False):
    """Per-group guardrail policy.

    Missing actions default to ignore. profiles may be listed with both dlp actions ignore (staged, inactive) but a non-ignore dlp action requires at least one profile. streaming defaults to buffered when any response action is block and passthrough otherwise; passthrough with a response block is 400. Findings are codes and counts only; content is never stored. The stored form is echoed back canonicalised (all actions explicit, profiles sorted); {} is stored as an all-ignore policy, null disables.
    """

    dlp: GuardrailsDlp

    secrets: GuardrailsSecrets

    streaming: Literal["buffered", "passthrough"]


class Retries(TypedDict, total=False):
    """Per-group same-route retries.

    max_attempts counts the first try of each step (the primary and each fallback) and is the ceiling for the x-ltg-max-attempts request header. A step is retried only when its attempt definitely did no provider work (connection failure before dispatch, or 429/529) before the first provider event; an uncertain failure (timeout, 408/500/502/503/504) moves to the next fallback step instead. max_attempts x (1 + the longest fallback chain) must not exceed 8, else 400. The n-th retry waits retry_delay_ms (constant), retry_delay_ms*n (linear) or retry_delay_ms*2^(n-1) (exponential), at most 5 s and never past the request deadline, then jittered uniformly down to half that value so concurrent retries spread out; a provider Retry-After of at most 5 s is honoured and a longer one moves to the next step. request_timeout_ms applies to streaming requests only: it bounds each attempt's time to its first provider event and never applies after it. Non-stream requests keep the per-attempt hop and idle bounds (their headers arrive only with the finished completion). retry_delay_ms and backoff are floors for the request knobs. Each planned attempt is reserved (at most 8 per request); unused reservation is released at settlement. Managed routes only. The stored form is echoed back with defaults filled in; null disables retries.
    """

    max_attempts: Required[int]

    backoff: Literal["constant", "linear", "exponential"]

    request_timeout_ms: Optional[int]

    retry_delay_ms: int


from .budget_duration import BudgetDuration
