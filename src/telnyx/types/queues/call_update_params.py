# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CallUpdateParams"]


class CallUpdateParams(TypedDict, total=False):
    queue_name: Required[str]

    keep_after_hangup: bool
    """Whether the call should remain in queue after hangup."""
