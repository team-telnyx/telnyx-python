# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunListParams", "Page"]


class RunListParams(TypedDict, total=False):
    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    status: str
    """Filter runs by execution status (pending, running, completed, failed, timeout)"""

    test_suite_run_id: str
    """Filter runs by specific suite execution batch ID"""


class Page(TypedDict, total=False):
    number: int
    """Page number to retrieve (1-based indexing)"""

    size: int
    """Number of test runs to return per page (1-100)"""
