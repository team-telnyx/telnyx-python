# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ParticipantUpdateParams"]


class ParticipantUpdateParams(TypedDict, total=False):
    account_sid: Required[str]

    conference_sid: Required[str]

    announce_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="AnnounceMethod")]
    """The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`."""

    announce_url: Annotated[str, PropertyInfo(alias="AnnounceUrl")]
    """The URL to call to announce something to the participant.

    The URL may return an MP3 fileo a WAV file, or a TwiML document that contains
    `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.
    """

    beep_on_exit: Annotated[bool, PropertyInfo(alias="BeepOnExit")]
    """
    Whether to play a notification beep to the conference when the participant
    exits.
    """

    call_sid_to_coach: Annotated[str, PropertyInfo(alias="CallSidToCoach")]
    """The SID of the participant who is being coached.

    The participant being coached is the only participant who can hear the
    participant who is coaching.
    """

    coaching: Annotated[bool, PropertyInfo(alias="Coaching")]
    """Whether the participant is coaching another call.

    When `true`, `CallSidToCoach` has to be given.
    """

    end_conference_on_exit: Annotated[bool, PropertyInfo(alias="EndConferenceOnExit")]
    """Whether to end the conference when the participant leaves."""

    hold: Annotated[bool, PropertyInfo(alias="Hold")]
    """Whether the participant should be on hold."""

    hold_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="HoldMethod")]
    """The HTTP method to use when calling the `HoldUrl`."""

    hold_url: Annotated[str, PropertyInfo(alias="HoldUrl")]
    """
    The URL to be called using the `HoldMethod` for music that plays when the
    participant is on hold. The URL may return an MP3 file, a WAV file, or a TwiML
    document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.
    """

    muted: Annotated[bool, PropertyInfo(alias="Muted")]
    """Whether the participant should be muted."""

    wait_url: Annotated[str, PropertyInfo(alias="WaitUrl")]
    """
    The URL to call for an audio file to play while the participant is waiting for
    the conference to start.
    """
