# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebSearchContentsParams"]


class WebSearchContentsParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]
    """List of URLs to retrieve content from (max 20 for public API)."""

    crawl_timeout: int
    """Timeout for crawling each URL, in seconds (1-60)."""

    formats: List[Literal["html", "markdown", "metadata"]]
    """Content formats to return.

    If omitted, `html` and `metadata` are returned by default. Retrieval is
    best-effort per URL: a format field appears only when that content could be
    produced, and a freshly crawled page may also include `html` even when not
    requested.
    """

    max_age: Optional[int]
    """Maximum age of cached content in seconds. `null` means no limit."""
