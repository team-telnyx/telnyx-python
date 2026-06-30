# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .action_extend_response import ActionExtendResponse as ActionExtendResponse


def __getattr__(name: str) -> Any:
    if name == "ActionExtendResponse":
        from .action_extend_response import ActionExtendResponse

        return ActionExtendResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
