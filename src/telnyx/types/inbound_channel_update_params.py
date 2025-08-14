# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InboundChannelUpdateParams"]


class InboundChannelUpdateParams(TypedDict, total=False):
    channels: Required[int]
    """The new number of concurrent channels for the account"""
