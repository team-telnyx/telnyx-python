# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .usecase_get_cost_params import UsecaseGetCostParams as UsecaseGetCostParams
from .osr_get_attributes_response import OsrGetAttributesResponse as OsrGetAttributesResponse

if TYPE_CHECKING:
    from .usecase_get_cost_response import UsecaseGetCostResponse as UsecaseGetCostResponse


def __getattr__(name: str) -> Any:
    if name == "UsecaseGetCostResponse":
        from .usecase_get_cost_response import UsecaseGetCostResponse

        return UsecaseGetCostResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
