# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_delete_params import ActionDeleteParams as ActionDeleteParams

if TYPE_CHECKING:
    from .action_delete_response import ActionDeleteResponse as ActionDeleteResponse


def __getattr__(name: str) -> Any:
    if name == "ActionDeleteResponse":
        from .action_delete_response import ActionDeleteResponse

        return ActionDeleteResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
