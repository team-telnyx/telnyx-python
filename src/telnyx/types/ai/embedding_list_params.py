# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["EmbeddingListParams"]


class EmbeddingListParams(TypedDict, total=False):
    status: SequenceNotStr[str]
    """List of task statuses i.e. `status=queued&status=processing`"""
