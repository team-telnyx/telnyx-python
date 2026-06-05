# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    content: Required[str]
    """Comment body. 1–5000 characters."""

    parent_comment_id: str
    """Optional parent comment id to thread this reply under."""
