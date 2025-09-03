# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActionMuteParams"]


class ActionMuteParams(TypedDict, total=False):
    call_control_ids: SequenceNotStr[str]
    """Array of unique identifiers and tokens for controlling the call.

    When empty all participants will be muted.
    """
