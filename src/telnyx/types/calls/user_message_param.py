# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserMessageParam"]


class UserMessageParam(TypedDict, total=False):
    """Messages sent by an end user"""

    content: Required[str]
    """The contents of the user message."""

    role: Required[Literal["user"]]
    """The role of the messages author, in this case `user`."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""
