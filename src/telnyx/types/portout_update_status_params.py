# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PortoutUpdateStatusParams"]


class PortoutUpdateStatusParams(TypedDict, total=False):
    id: Required[str]

    reason: Required[str]
    """Provide a reason if rejecting the port out request"""

    host_messaging: bool
    """
    Indicates whether messaging services should be maintained with Telnyx after the
    port out completes
    """
