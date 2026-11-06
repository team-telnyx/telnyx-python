# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MeetingSessionLeavePolicyParam"]


class MeetingSessionLeavePolicyParam(TypedDict, total=False):
    """Automatic departure settings for Google Meet and Teams.

    Omitted fields use the default behavior. Set at creation; cannot be changed later. Zoom ignores this policy.
    """

    alone_seconds: int
    """Seconds alone after another participant has attended and left.

    Does not start just because the bot arrives first.
    """

    bot_name_keywords: Optional[SequenceNotStr[str]]
    """
    Case-insensitive names or phrases identifying other bots to exclude when
    deciding whether this bot is alone. Matching splits names on spaces, hyphens and
    underscores. Null or an empty array disables filtering.
    """

    host_wait_seconds: int
    """Seconds to wait for the host to start the meeting."""

    lobby_wait_seconds: int
    """Seconds to wait for lobby admission."""

    max_duration_seconds: Optional[int]
    """Maximum seconds after joining.

    Null means no per-join duration limit; service safety limits still apply.
    """

    silence_grace_seconds: int
    """Seconds after joining before silence detection starts a fresh inactivity timer."""

    silence_seconds: int
    """Continuous audio inactivity before departure after the silence grace period."""
