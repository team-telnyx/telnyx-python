# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["RemediationPerNumberResults"]


class RemediationPerNumberResults(BaseModel):
    """Per-category buckets of phone numbers, populated once results are available.

    Empty lists are kept (not omitted) so consumers can iterate without null-checking each key.
    """

    ineligible: Optional[List[str]] = None

    not_flagged: Optional[List[str]] = None

    refused: Optional[List[str]] = None

    remediated: Optional[List[str]] = None

    requires_review: Optional[List[str]] = None
