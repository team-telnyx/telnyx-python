# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoiceSDKCallReportListParams"]


class VoiceSDKCallReportListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    sort: Literal["asc", "desc", "created_at", "-created_at"]
    """Set the order of the results by creation date.

    `asc` and `created_at` sort oldest reports first; `desc` and `-created_at` sort
    newest reports first. If not given, results are sorted by creation date in
    descending order.
    """
