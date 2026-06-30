# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .session_list_0_params import SessionList0Params as SessionList0Params
from .session_list_1_params import SessionList1Params as SessionList1Params
from .session_retrieve_params import SessionRetrieveParams as SessionRetrieveParams
from .action_refresh_client_token_params import ActionRefreshClientTokenParams as ActionRefreshClientTokenParams
from .session_retrieve_participants_params import SessionRetrieveParticipantsParams as SessionRetrieveParticipantsParams
from .action_generate_join_client_token_params import (
    ActionGenerateJoinClientTokenParams as ActionGenerateJoinClientTokenParams,
)

if TYPE_CHECKING:
    from .session_retrieve_response import SessionRetrieveResponse as SessionRetrieveResponse
    from .action_refresh_client_token_response import (
        ActionRefreshClientTokenResponse as ActionRefreshClientTokenResponse,
    )
    from .action_generate_join_client_token_response import (
        ActionGenerateJoinClientTokenResponse as ActionGenerateJoinClientTokenResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "ActionGenerateJoinClientTokenResponse":
        from .action_generate_join_client_token_response import ActionGenerateJoinClientTokenResponse

        return ActionGenerateJoinClientTokenResponse
    if name == "ActionRefreshClientTokenResponse":
        from .action_refresh_client_token_response import ActionRefreshClientTokenResponse

        return ActionRefreshClientTokenResponse
    if name == "SessionRetrieveResponse":
        from .session_retrieve_response import SessionRetrieveResponse

        return SessionRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
