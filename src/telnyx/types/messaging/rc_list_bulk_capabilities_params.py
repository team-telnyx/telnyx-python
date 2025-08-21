# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RcListBulkCapabilitiesParams"]


class RcListBulkCapabilitiesParams(TypedDict, total=False):
    agent_id: Required[str]
    """RCS Agent ID"""

    phone_numbers: Required[List[str]]
    """List of phone numbers to check"""
