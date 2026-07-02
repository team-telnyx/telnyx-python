# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .key_list_params import KeyListParams as KeyListParams
from .key_update_params import KeyUpdateParams as KeyUpdateParams

if TYPE_CHECKING:
    from .key_list_response import KeyListResponse as KeyListResponse


def __getattr__(name: str) -> Any:
    if name == "KeyListResponse":
        from .key_list_response import KeyListResponse

        return KeyListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
