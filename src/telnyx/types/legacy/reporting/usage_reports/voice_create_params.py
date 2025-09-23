# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["VoiceCreateParams"]


class VoiceCreateParams(TypedDict, total=False):
    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End time in ISO format"""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Start time in ISO format"""

    aggregation_type: int
    """
    Aggregation type: All = 0, By Connections = 1, By Tags = 2, By Billing Group = 3
    """

    connections: Iterable[int]
    """List of connections to filter by"""

    managed_accounts: SequenceNotStr[str]
    """List of managed accounts to include"""

    product_breakdown: int
    """
    Product breakdown type: No breakdown = 0, DID vs Toll-free = 1, Country = 2, DID
    vs Toll-free per Country = 3
    """

    select_all_managed_accounts: bool
    """Whether to select all managed accounts"""
