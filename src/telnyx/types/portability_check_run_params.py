# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PortabilityCheckRunParams"]


class PortabilityCheckRunParams(TypedDict, total=False):
    phone_numbers: SequenceNotStr[str]
    """The list of +E.164 formatted phone numbers to check for portability"""
