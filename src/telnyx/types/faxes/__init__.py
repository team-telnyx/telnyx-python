# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_cancel_response import ActionCancelResponse as ActionCancelResponse
    from .action_refresh_response import ActionRefreshResponse as ActionRefreshResponse


def __getattr__(name: str) -> Any:
    if name == "ActionCancelResponse":
        from .action_cancel_response import ActionCancelResponse

        return ActionCancelResponse
    if name == "ActionRefreshResponse":
        from .action_refresh_response import ActionRefreshResponse

        return ActionRefreshResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
