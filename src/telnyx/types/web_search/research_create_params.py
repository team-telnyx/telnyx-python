# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResearchCreateParams"]


class ResearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """The research question or topic."""

    background: bool
    """When `true`, the research runs asynchronously.

    The response returns a `task_id` immediately instead of waiting for the result.
    Poll `GET /web_search/research/{task_id}` to check status.
    """

    max_sources: int
    """Maximum number of sources to use."""

    research_effort: Literal["lite", "standard", "deep"]
    """Research depth level. `lite` is fastest, `deep` is most thorough."""
