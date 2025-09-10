# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ActionUnmuteParams"]


class ActionUnmuteParams(TypedDict, total=False):
    exclude: SequenceNotStr[str]
    """List of participant id to exclude from the action."""

    participants: Union[Literal["all"], SequenceNotStr[str]]
    """
    Either a list of participant id to perform the action on, or the keyword "all"
    to perform the action on all participant.
    """
