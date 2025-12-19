# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QueueUpdateParams"]


class QueueUpdateParams(TypedDict, total=False):
    account_sid: Required[str]

    max_size: Annotated[int, PropertyInfo(alias="MaxSize")]
    """The maximum size of the queue."""
