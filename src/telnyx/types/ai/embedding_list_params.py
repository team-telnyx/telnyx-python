# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["EmbeddingListParams"]


class EmbeddingListParams(TypedDict, total=False):
    status: List[str]
    """List of task statuses i.e. `status=queued&status=processing`"""
