# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_speak_params import ActionSpeakParams as ActionSpeakParams
from .artifact_create_params import ArtifactCreateParams as ArtifactCreateParams
from .action_send_chat_params import ActionSendChatParams as ActionSendChatParams

if TYPE_CHECKING:
    from .artifact_list_response import ArtifactListResponse as ArtifactListResponse
    from .action_accepted_response import ActionAcceptedResponse as ActionAcceptedResponse
    from .meeting_session_artifact import MeetingSessionArtifact as MeetingSessionArtifact
    from .meeting_session_artifact_response import MeetingSessionArtifactResponse as MeetingSessionArtifactResponse


def __getattr__(name: str) -> Any:
    if name == "ActionAcceptedResponse":
        from .action_accepted_response import ActionAcceptedResponse

        return ActionAcceptedResponse
    if name == "MeetingSessionArtifact":
        from .meeting_session_artifact import MeetingSessionArtifact

        return MeetingSessionArtifact
    if name == "MeetingSessionArtifactResponse":
        from .meeting_session_artifact_response import MeetingSessionArtifactResponse

        return MeetingSessionArtifactResponse
    if name == "ArtifactListResponse":
        from .artifact_list_response import ArtifactListResponse

        return ArtifactListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
