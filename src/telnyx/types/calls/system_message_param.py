# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SystemMessageParam"]


class SystemMessageParam(TypedDict, total=False):
    """
    Developer-provided instructions that the model should follow, regardless of messages sent by the user.
    """

    content: Required[str]
    """The contents of the system message."""

    role: Required[Literal["system"]]
    """The role of the messages author, in this case `system`."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""
