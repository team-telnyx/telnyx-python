# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QueueCreateParams"]


class QueueCreateParams(TypedDict, total=False):
    friendly_name: Annotated[str, PropertyInfo(alias="FriendlyName")]
    """A human readable name for the queue."""

    max_size: Annotated[int, PropertyInfo(alias="MaxSize")]
    """The maximum size of the queue."""
