# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RcGenerateDeeplinkParams"]


class RcGenerateDeeplinkParams(TypedDict, total=False):
    body: str
    """Pre-filled message body (URL encoded)"""

    phone_number: str
    """Phone number in E164 format (URL encoded)"""
