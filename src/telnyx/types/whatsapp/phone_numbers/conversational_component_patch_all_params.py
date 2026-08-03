# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["ConversationalComponentPatchAllParams", "Command"]


class ConversationalComponentPatchAllParams(TypedDict, total=False):
    commands: Iterable[Command]
    """List of commands"""

    ice_breakers: SequenceNotStr[str]
    """List of ice breakers"""


class Command(TypedDict, total=False):
    command: str

    description: str
