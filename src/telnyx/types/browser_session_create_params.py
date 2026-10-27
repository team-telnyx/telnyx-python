# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BrowserSessionCreateParams", "Policy", "Limits"]


class BrowserSessionCreateParams(TypedDict, total=False):
    policy: Required[Policy]

    idempotency_key: str
    """Scoped to the organization.

    The same key and identical normalized policy, limits, and metadata replay the
    existing session (HTTP 201); a different request returns 409
    idempotency_conflict. Replays do not restart terminal sessions.
    """

    limits: Limits

    metadata: object
    """Arbitrary key-value metadata."""


class Policy(TypedDict, total=False):
    allowed_domains: Required[SequenceNotStr[str]]
    """Domain patterns the browser can navigate to.

    Exact match (example.com) or wildcard (\\**.example.com). IP literals not allowed.
    """


class Limits(TypedDict, total=False):
    idle_timeout_s: int
    """Idle timeout in seconds. Must not exceed lifetime_s."""

    lifetime_s: int
    """Max session duration in seconds (60-1800)."""
