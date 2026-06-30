# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_validate_params import ActionValidateParams as ActionValidateParams
from .action_accept_suggestions_params import ActionAcceptSuggestionsParams as ActionAcceptSuggestionsParams

if TYPE_CHECKING:
    from .action_validate_response import ActionValidateResponse as ActionValidateResponse
    from .action_accept_suggestions_response import ActionAcceptSuggestionsResponse as ActionAcceptSuggestionsResponse


def __getattr__(name: str) -> Any:
    if name == "ActionAcceptSuggestionsResponse":
        from .action_accept_suggestions_response import ActionAcceptSuggestionsResponse

        return ActionAcceptSuggestionsResponse
    if name == "ActionValidateResponse":
        from .action_validate_response import ActionValidateResponse

        return ActionValidateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
