# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["ActionHoldParams"]


class ActionHoldParams(TypedDict, total=False):
    audio_url: str
    """The URL of a file to be played to the participants when they are put on hold.

    media_name and audio_url cannot be used together in one request.
    """

    call_control_ids: List[str]
    """List of unique identifiers and tokens for controlling the call.

    When empty all participants will be placed on hold.
    """

    media_name: str
    """
    The media_name of a file to be played to the participants when they are put on
    hold. The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """
