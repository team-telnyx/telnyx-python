# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeveloperMessageParam"]


class DeveloperMessageParam(TypedDict, total=False):
    """
    Developer-provided instructions that the model should follow, regardless of messages sent by the user.
    """

    content: Required[str]
    """The contents of the developer message."""

    role: Required[Literal["developer"]]
    """The role of the messages author, in this case developer."""

    metadata: Dict[str, object]
    """Metadata to add to the message"""
