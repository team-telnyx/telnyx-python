# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .comment_type import CommentType

__all__ = ["CommentListParams"]


class CommentListParams(TypedDict, total=False):
    comment_type: CommentType
    """Restrict to comments of this category.

    Customer-visible categories only: internal-only comments are filtered out
    regardless of this filter.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page. Maximum 250; values above are clamped to 250."""
