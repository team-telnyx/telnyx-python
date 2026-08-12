# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .collections.source_request_param import SourceRequestParam
from .collections.retrieval_settings_wrapper_param import RetrievalSettingsWrapperParam

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable collection name."""

    description: str
    """Optional description."""

    settings: RetrievalSettingsWrapperParam
    """Optional retrieval settings."""

    slug: str
    """Optional slug (unique per organization). Derived from `name` when omitted."""

    sources: Iterable[SourceRequestParam]
    """Optional sources to attach at creation time."""
