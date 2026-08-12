# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebSearchContentsResponse", "Data", "DataResult", "DataResultMetadata"]


class DataResultMetadata(BaseModel):
    """Page metadata (if `metadata` format requested)."""

    favicon_url: Optional[str] = None
    """Favicon URL (if available)."""

    site_name: Optional[str] = None
    """Site name. Often empty."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataResult(BaseModel):
    url: str
    """The source URL."""

    html: Optional[str] = None
    """
    Cleaned HTML content (if `html` format requested; may also be present on freshly
    crawled pages).
    """

    markdown: Optional[str] = None
    """Markdown content (if `markdown` format requested)."""

    metadata: Optional[DataResultMetadata] = None
    """Page metadata (if `metadata` format requested)."""

    title: Optional[str] = None
    """Page title (if available)."""


class Data(BaseModel):
    results: Optional[List[DataResult]] = None


class WebSearchContentsResponse(BaseModel):
    data: Optional[Data] = None
