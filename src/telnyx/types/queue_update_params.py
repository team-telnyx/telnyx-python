# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueueUpdateParams"]


class QueueUpdateParams(TypedDict, total=False):
    max_size: Required[int]
    """The maximum number of calls allowed in the queue."""
