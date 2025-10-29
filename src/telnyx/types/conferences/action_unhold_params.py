# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActionUnholdParams"]


class ActionUnholdParams(TypedDict, total=False):
    call_control_ids: Required[SequenceNotStr[str]]
    """List of unique identifiers and tokens for controlling the call.

    Enter each call control ID to be unheld.
    """

    region: Literal["Australia", "Europe", "Middle East", "US"]
    """Region where the conference data is located.

    Defaults to the region defined in user's data locality settings (Europe or US).
    """
