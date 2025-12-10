# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DetailRecordListParams", "Filter"]


class DetailRecordListParams(TypedDict, total=False):
    filter: Filter
    """Filter records on a given record attribute and value.

    <br/>Example: filter[status]=delivered. <br/>Required: filter[record_type] must
    be specified.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: SequenceNotStr[str]
    """Specifies the sort order for results. <br/>Example: sort=-created_at"""


class FilterTyped(TypedDict, total=False):
    """Filter records on a given record attribute and value.

    <br/>Example: filter[status]=delivered. <br/>Required: filter[record_type] must be specified.
    """

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
