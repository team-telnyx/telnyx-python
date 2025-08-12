# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LedgerBillingGroupReportCreateParams"]


class LedgerBillingGroupReportCreateParams(TypedDict, total=False):
    month: int
    """Month of the ledger billing group report"""

    year: int
    """Year of the ledger billing group report"""
