# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionSendChatParams"]


class ActionSendChatParams(TypedDict, total=False):
    text: Required[str]
    """Message text, 1–4000 characters.

    On Google Meet and Teams, also at most 4096 UTF-8 bytes and nonblank; control
    characters other than tab and line breaks are rejected. CRLF is normalized to
    LF.
    """
