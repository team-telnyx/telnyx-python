# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DetailRecordListParams", "Filter", "Page"]


class DetailRecordListParams(TypedDict, total=False):
    filter: Filter
    """Filter records on a given record attribute and value.

    <br/>Example: filter[status]=delivered. <br/>Required: filter[record_type] must
    be specified.
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[number], page[size]
    """

    sort: List[str]
    """Specifies the sort order for results. <br/>Example: sort=-created_at"""


class FilterTyped(TypedDict, total=False):
    record_type: Required[
        Literal[
            "ai-voice-assistant",
            "amd",
            "call-control",
            "conference",
            "conference-participant",
            "embedding",
            "fax",
            "inference",
            "inference-speech-to-text",
            "media_storage",
            "media-streaming",
            "messaging",
            "noise-suppression",
            "recording",
            "sip-trunking",
            "siprec-client",
            "stt",
            "tts",
            "verify",
            "webrtc",
            "wireless",
        ]
    ]
    """Filter by the given record type."""

    date_range: Literal[
        "yesterday",
        "today",
        "tomorrow",
        "last_week",
        "this_week",
        "next_week",
        "last_month",
        "this_month",
        "next_month",
    ]
    """Filter by the given user-friendly date range.

    You can specify one of the following enum values, or a dynamic one using this
    format: last_N_days.
    """


Filter: TypeAlias = Union[FilterTyped, Dict[str, object]]


class Page(TypedDict, total=False):
    number: int
    """Page number"""

    size: int
    """Page size"""
