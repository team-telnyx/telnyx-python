# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BrowserSessionListParams"]


class BrowserSessionListParams(TypedDict, total=False):
    status: Literal["provisioning", "ready", "closing", "closed", "failed", "expired"]
