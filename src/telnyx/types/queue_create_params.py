# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["QueueCreateParams"]


class QueueCreateParams(TypedDict, total=False):
    queue_name: Required[str]
    """The name of the queue. Must be between 1 and 255 characters."""

    max_size: int
    """The maximum number of calls allowed in the queue."""
