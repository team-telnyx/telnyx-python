# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CommentListParams", "Filter"]


class CommentListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[comment_record_type], filter[comment_record_id]
    """


class Filter(TypedDict, total=False):
    comment_record_id: str
    """ID of the record the comments relate to"""

    comment_record_type: Literal["sub_number_order", "requirement_group"]
    """Record type that the comment relates to"""
