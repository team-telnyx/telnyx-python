# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["NumberCreateParams"]


class NumberCreateParams(TypedDict, total=False):
    phone_numbers: Required[SequenceNotStr[str]]
    """List of phone numbers to associate for reputation monitoring (max 100)"""
