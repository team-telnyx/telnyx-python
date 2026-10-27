# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_rotate_token_response import ActionRotateTokenResponse as ActionRotateTokenResponse


def __getattr__(name: str) -> Any:
    if name == "ActionRotateTokenResponse":
        from .action_rotate_token_response import ActionRotateTokenResponse

        return ActionRotateTokenResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
