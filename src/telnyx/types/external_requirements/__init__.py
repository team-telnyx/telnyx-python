# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .sub_number_order_update_params import SubNumberOrderUpdateParams as SubNumberOrderUpdateParams

if TYPE_CHECKING:
    from .sub_number_order_update_response import SubNumberOrderUpdateResponse as SubNumberOrderUpdateResponse
    from .sub_number_order_retrieve_response import SubNumberOrderRetrieveResponse as SubNumberOrderRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "SubNumberOrderRetrieveResponse":
        from .sub_number_order_retrieve_response import SubNumberOrderRetrieveResponse

        return SubNumberOrderRetrieveResponse
    if name == "SubNumberOrderUpdateResponse":
        from .sub_number_order_update_response import SubNumberOrderUpdateResponse

        return SubNumberOrderUpdateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
