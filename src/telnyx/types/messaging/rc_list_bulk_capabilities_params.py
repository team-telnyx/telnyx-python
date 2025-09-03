# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RcListBulkCapabilitiesParams"]


class RcListBulkCapabilitiesParams(TypedDict, total=False):
    agent_id: Required[str]
    """RCS Agent ID"""

    phone_numbers: Required[SequenceNotStr[str]]
    """List of phone numbers to check"""
