# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from ..calls.loopcount_param import LoopcountParam

__all__ = ["ActionPlayParams"]


class ActionPlayParams(TypedDict, total=False):
    audio_url: str
    """The URL of a file to be played back in the conference.

    media_name and audio_url cannot be used together in one request.
    """

    call_control_ids: List[str]
    """
    List of call control ids identifying participants the audio file should be
    played to. If not given, the audio file will be played to the entire conference.
    """

    loop: LoopcountParam
    """The number of times the audio file should be played.

    If supplied, the value must be an integer between 1 and 100, or the special
    string `infinity` for an endless loop.
    """

    media_name: str
    """The media_name of a file to be played back in the conference.

    The media_name must point to a file previously uploaded to
    api.telnyx.com/v2/media by the same user/organization. The file must either be a
    WAV or MP3 file.
    """
