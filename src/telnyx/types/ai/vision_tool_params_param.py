# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VisionToolParamsParam"]


class VisionToolParamsParam(TypedDict, total=False):
    max_frame_age_secs: int
    """
    Frames received longer ago than this many seconds are not shown to the
    assistant, so it never describes a frozen or disconnected camera as live.
    """
