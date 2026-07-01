# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_enable_params import ActionEnableParams as ActionEnableParams

if TYPE_CHECKING:
    from .action_enable_response import ActionEnableResponse as ActionEnableResponse
    from .action_disable_response import ActionDisableResponse as ActionDisableResponse


def __getattr__(name: str) -> Any:
    if name == "ActionDisableResponse":
        from .action_disable_response import ActionDisableResponse

        return ActionDisableResponse
    if name == "ActionEnableResponse":
        from .action_enable_response import ActionEnableResponse

        return ActionEnableResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
