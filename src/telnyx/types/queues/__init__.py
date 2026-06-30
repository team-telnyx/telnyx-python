# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .call_list_params import CallListParams as CallListParams
from .call_update_params import CallUpdateParams as CallUpdateParams

if TYPE_CHECKING:
    from .queue_call import QueueCall as QueueCall
    from .call_retrieve_response import CallRetrieveResponse as CallRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "QueueCall":
        from .queue_call import QueueCall

        return QueueCall
    if name == "CallRetrieveResponse":
        from .call_retrieve_response import CallRetrieveResponse

        return CallRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
