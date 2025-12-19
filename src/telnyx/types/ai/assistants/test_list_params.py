# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TestListParams"]


class TestListParams(TypedDict, total=False):
    destination: str
    """Filter tests by destination (phone number, webhook URL, etc.)"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    telnyx_conversation_channel: str
    """Filter tests by communication channel (e.g., 'web_chat', 'sms')"""

    test_suite: str
    """Filter tests by test suite name"""
