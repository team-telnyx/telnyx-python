# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActionUnmuteParams"]


class ActionUnmuteParams(TypedDict, total=False):
    call_control_ids: SequenceNotStr[str]
    """List of unique identifiers and tokens for controlling the call.

    Enter each call control ID to be unmuted. When empty all participants will be
    unmuted.
    """
