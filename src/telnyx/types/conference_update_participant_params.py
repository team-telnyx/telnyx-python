# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConferenceUpdateParticipantParams"]


class ConferenceUpdateParticipantParams(TypedDict, total=False):
    id: Required[str]

    beep_enabled: Literal["always", "never", "on_enter", "on_exit"]
    """Whether entry/exit beeps are enabled for this participant."""

    end_conference_on_exit: bool
    """Whether the conference should end when this participant exits."""

    soft_end_conference_on_exit: bool
    """Whether the conference should soft-end when this participant exits.

    A soft end will stop new participants from joining but allow existing
    participants to remain.
    """
