# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_stop_response import ActionStopResponse as ActionStopResponse


def __getattr__(name: str) -> Any:
    if name == "ActionStopResponse":
        from .action_stop_response import ActionStopResponse

        return ActionStopResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
