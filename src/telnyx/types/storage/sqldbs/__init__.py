# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_query_params import ActionQueryParams as ActionQueryParams

if TYPE_CHECKING:
    from .action_query_response import ActionQueryResponse as ActionQueryResponse


def __getattr__(name: str) -> Any:
    if name == "ActionQueryResponse":
        from .action_query_response import ActionQueryResponse

        return ActionQueryResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
