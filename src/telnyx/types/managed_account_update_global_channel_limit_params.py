# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ManagedAccountUpdateGlobalChannelLimitParams"]


class ManagedAccountUpdateGlobalChannelLimitParams(TypedDict, total=False):
    channel_limit: int
    """
    Integer value that indicates the number of allocatable global outbound channels
    that should be allocated to the managed account. Must be 0 or more. If the value
    is 0 then the account will have no usable channels and will not be able to
    perform outbound calling.
    """
