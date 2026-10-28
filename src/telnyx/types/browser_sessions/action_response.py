# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ActionResponse", "Error", "Result", "ResultArtifact", "ResultObservation"]


class Error(BaseModel):
    """Null unless an execution failure is recorded.

    Action failures (policy_denied, stale_observation, stale_ref, navigation_blocked, timeout, execution_lost, result_too_large) are returned on the action resource with HTTP 200. An unknown action with execution_lost has retryable=false; inspect session state and reconcile possible effects before any new action. Separately, a request may return HTTP 503 with a top-level execution_lost error and retryable=true; that is not proof of safe re-execution.
    """

    code: str

    retryable: bool


class ResultArtifact(BaseModel):
    artifact_id: Optional[str] = None

    content_type: Optional[str] = None

    size_bytes: Optional[int] = None


class ResultObservation(BaseModel):
    """
    Full tree and refs are delivered only in the original successful POST response when completed within wait_seconds. GET polling and idempotent replays return metadata with an empty tree and refs plus ref_count. Submit a fresh observe action to obtain usable refs.
    """

    observation_id: Optional[str] = None

    ref_count: Optional[int] = None
    """
    Number of refs in the original observation, present on stored observation
    metadata.
    """

    refs: Optional[object] = None

    title: Optional[str] = None

    tree: Optional[str] = None

    truncated: Optional[bool] = None

    url: Optional[str] = None


class Result(BaseModel):
    artifact: Optional[ResultArtifact] = None

    observation: Optional[ResultObservation] = None
    """
    Full tree and refs are delivered only in the original successful POST response
    when completed within wait_seconds. GET polling and idempotent replays return
    metadata with an empty tree and refs plus ref_count. Submit a fresh observe
    action to obtain usable refs.
    """

    results: Optional[List[object]] = None
    """Present only for batch actions."""

    title: Optional[str] = None

    url: Optional[str] = None


class ActionResponse(BaseModel):
    id: str

    completed_at: Optional[datetime] = None

    created_at: datetime

    error: Optional[Error] = None
    """Null unless an execution failure is recorded.

    Action failures (policy_denied, stale_observation, stale_ref,
    navigation_blocked, timeout, execution_lost, result_too_large) are returned on
    the action resource with HTTP 200. An unknown action with execution_lost has
    retryable=false; inspect session state and reconcile possible effects before any
    new action. Separately, a request may return HTTP 503 with a top-level
    execution_lost error and retryable=true; that is not proof of safe re-execution.
    """

    request: object
    """
    Normalized request metadata; defaults may be materialized and fill values are
    redacted as {redacted: true, length: number}, including inside batch actions.
    """

    result: Optional[Result] = None

    seq: int

    session_id: str

    started_at: Optional[datetime] = None

    status: Literal["queued", "running", "succeeded", "failed", "unknown"]
    """POST returns 202 for queued or running actions.

    Terminal states are succeeded, failed, and unknown (the execution outcome could
    not be determined, with error.code=execution_lost). GET returns 200 for both
    nonterminal and terminal states.
    """

    type: str
