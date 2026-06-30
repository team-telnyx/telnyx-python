# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_remove_response import ActionRemoveResponse as ActionRemoveResponse


def __getattr__(name: str) -> Any:
    if name == "ActionRemoveResponse":
        from .action_remove_response import ActionRemoveResponse

        return ActionRemoveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
