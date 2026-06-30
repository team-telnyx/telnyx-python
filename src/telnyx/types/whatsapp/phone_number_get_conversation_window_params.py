# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberGetConversationWindowParams"]


class PhoneNumberGetConversationWindowParams(TypedDict, total=False):
    destination_number: Required[str]
    """Destination phone number in E.164 format"""
