# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActionStopParams"]


class ActionStopParams(TypedDict, total=False):
    call_control_ids: SequenceNotStr[str]
    """
    List of call control ids identifying participants the audio file should stop be
    played to. If not given, the audio will be stoped to the entire conference.
    """

    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located.

    Defaults to the region defined in user's data locality settings (Europe or US).
    """
