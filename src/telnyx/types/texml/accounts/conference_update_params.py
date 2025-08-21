# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ConferenceUpdateParams"]


class ConferenceUpdateParams(TypedDict, total=False):
    account_sid: Required[str]

    announce_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="AnnounceMethod")]
    """The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`."""

    announce_url: Annotated[str, PropertyInfo(alias="AnnounceUrl")]
    """The URL we should call to announce something into the conference.

    The URL may return an MP3 file, a WAV file, or a TwiML document that contains
    `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.
    """

    status: Annotated[str, PropertyInfo(alias="Status")]
    """The new status of the resource.

    Specifying `completed` will end the conference and hang up all participants.
    """
