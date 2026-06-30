# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_kick_params import ActionKickParams as ActionKickParams
from .action_mute_params import ActionMuteParams as ActionMuteParams
from .action_unmute_params import ActionUnmuteParams as ActionUnmuteParams

if TYPE_CHECKING:
    from .action_end_response import ActionEndResponse as ActionEndResponse
    from .action_kick_response import ActionKickResponse as ActionKickResponse
    from .action_mute_response import ActionMuteResponse as ActionMuteResponse
    from .action_unmute_response import ActionUnmuteResponse as ActionUnmuteResponse


def __getattr__(name: str) -> Any:
    if name == "ActionEndResponse":
        from .action_end_response import ActionEndResponse

        return ActionEndResponse
    if name == "ActionKickResponse":
        from .action_kick_response import ActionKickResponse

        return ActionKickResponse
    if name == "ActionMuteResponse":
        from .action_mute_response import ActionMuteResponse

        return ActionMuteResponse
    if name == "ActionUnmuteResponse":
        from .action_unmute_response import ActionUnmuteResponse

        return ActionUnmuteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
