# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["PortabilityCheckRunParams"]


class PortabilityCheckRunParams(TypedDict, total=False):
    phone_numbers: List[str]
    """The list of +E.164 formatted phone numbers to check for portability"""
