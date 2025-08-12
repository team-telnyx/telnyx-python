# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TestListParams", "Page"]


class TestListParams(TypedDict, total=False):
    destination: str
    """Filter tests by destination (phone number, webhook URL, etc.)"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """

    telnyx_conversation_channel: str
    """Filter tests by communication channel (e.g., 'web_chat', 'sms')"""

    test_suite: str
    """Filter tests by test suite name"""


class Page(TypedDict, total=False):
    number: int
    """Page number to retrieve (1-based indexing)"""

    size: int
    """Number of tests to return per page (1-100)"""
