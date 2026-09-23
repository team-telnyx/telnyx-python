# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["DetailRecordListParams", "Filter"]


class DetailRecordListParams(TypedDict, total=False):
    filter: Filter
    """Filter records on a given record attribute and value.

    <br/>Example: filter[status]=delivered. <br/>Required: filter[record_type] must
    be specified. <br/>The valid filter fields depend on the record_type: filtering
    by a field that does not exist for the selected record_type is rejected with a
    400 error. Call-control and sip-trunking records use started_at, finished_at and
    answered_at (they have no created_at); messaging records use created_at. To list
    the fields available for a record_type, use the /v2/detail_records/options
    endpoint.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: SequenceNotStr[str]
    """Specifies the sort order for results.

    <br/>Example: sort=-created_at <br/>The valid sort fields depend on the
    record_type: sort by a field that does not exist for the selected record_type is
    rejected with a 400 error. Call-control and sip-trunking records use started_at,
    finished_at and answered_at (they have no created_at); messaging records use
    created_at. To list the fields available for a record_type, use the
    /v2/detail_records/options endpoint.
    """


class Filter(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Filter records on a given record attribute and value.

    <br/>Example: filter[status]=delivered. <br/>Required: filter[record_type] must be specified. <br/>The valid filter fields depend on the record_type: filtering by a field that does not exist for the selected record_type is rejected with a 400 error. Call-control and sip-trunking records use started_at, finished_at and answered_at (they have no created_at); messaging records use created_at. To list the fields available for a record_type, use the /v2/detail_records/options endpoint.
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
