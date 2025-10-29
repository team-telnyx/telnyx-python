# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConferenceRetrieveParams"]


class ConferenceRetrieveParams(TypedDict, total=False):
    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located"""
