# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

__all__ = ["ActionMuteParams"]


class ActionMuteParams(TypedDict, total=False):
    exclude: List[str]
    """List of participant id to exclude from the action."""

    participants: Union[Literal["all"], List[str]]
    """
    Either a list of participant id to perform the action on, or the keyword "all"
    to perform the action on all participant.
    """
