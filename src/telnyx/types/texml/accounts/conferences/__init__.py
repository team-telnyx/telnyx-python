# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .participant_update_params import ParticipantUpdateParams as ParticipantUpdateParams
from .participant_participants_params import ParticipantParticipantsParams as ParticipantParticipantsParams

if TYPE_CHECKING:
    from .participant_resource import ParticipantResource as ParticipantResource
    from .participant_participants_response import ParticipantParticipantsResponse as ParticipantParticipantsResponse
    from .participant_retrieve_participants_response import (
        ParticipantRetrieveParticipantsResponse as ParticipantRetrieveParticipantsResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "ParticipantResource":
        from .participant_resource import ParticipantResource

        return ParticipantResource
    if name == "ParticipantParticipantsResponse":
        from .participant_participants_response import ParticipantParticipantsResponse

        return ParticipantParticipantsResponse
    if name == "ParticipantRetrieveParticipantsResponse":
        from .participant_retrieve_participants_response import ParticipantRetrieveParticipantsResponse

        return ParticipantRetrieveParticipantsResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
