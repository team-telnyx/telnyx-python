# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebSearchCreateParams"]


class WebSearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """The search query text."""

    count: int
    """Number of results to return (1-100)."""

    country: str
    """Two-letter country code (ISO 3166-1 alpha-2) to bias results."""

    exclude_domains: SequenceNotStr[str]
    """Exclude results from these domains (bare hostnames, e.g. `pinterest.com`)."""

    freshness: str
    """Time-based filter for results. Common values: `day`, `week`, `month`, `year`."""

    include_domains: SequenceNotStr[str]
    """Restrict results to these domains (bare hostnames, e.g. `arxiv.org`)."""

    livecrawl: bool
    """When true, the provider crawls pages in real-time for fresh content.

    The boolean is translated to the provider's internal enum internally; callers
    always pass `true` or `false`.
    """

    safesearch: Literal["off", "moderate", "strict"]
    """Safe search filter level."""
