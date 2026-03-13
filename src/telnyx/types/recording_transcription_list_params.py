# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RecordingTranscriptionListParams", "Filter", "FilterCreatedAt"]


class RecordingTranscriptionListParams(TypedDict, total=False):
    filter: Filter
    """Filter recording transcriptions by various attributes."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterCreatedAt(TypedDict, total=False):
    gte: str
    """Returns only transcriptions created later than or at given ISO 8601 datetime."""

    lte: str
    """Returns only transcriptions created earlier than or at given ISO 8601 datetime."""


class Filter(TypedDict, total=False):
    """Filter recording transcriptions by various attributes."""

    created_at: FilterCreatedAt

    recording_id: str
    """
    If present, transcriptions will be filtered to those associated with the given
    recording.
    """
