# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    body: str
    """Comment to post on this portout request"""
