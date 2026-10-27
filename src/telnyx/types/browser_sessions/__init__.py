# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .fill_action_param import FillActionParam as FillActionParam
from .click_action_param import ClickActionParam as ClickActionParam
from .press_action_param import PressActionParam as PressActionParam
from .scroll_action_param import ScrollActionParam as ScrollActionParam
from .select_action_param import SelectActionParam as SelectActionParam
from .action_create_params import ActionCreateParams as ActionCreateParams
from .observe_action_param import ObserveActionParam as ObserveActionParam
from .navigate_action_param import NavigateActionParam as NavigateActionParam
from .wait_for_action_param import WaitForActionParam as WaitForActionParam
from .screenshot_action_param import ScreenshotActionParam as ScreenshotActionParam

if TYPE_CHECKING:
    from .action_response import ActionResponse as ActionResponse
    from .action_create_response import ActionCreateResponse as ActionCreateResponse
    from .action_retrieve_response import ActionRetrieveResponse as ActionRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "ActionResponse":
        from .action_response import ActionResponse

        return ActionResponse
    if name == "ActionCreateResponse":
        from .action_create_response import ActionCreateResponse

        return ActionCreateResponse
    if name == "ActionRetrieveResponse":
        from .action_retrieve_response import ActionRetrieveResponse

        return ActionRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
