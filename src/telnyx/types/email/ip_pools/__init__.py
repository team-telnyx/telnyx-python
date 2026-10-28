# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .ip_create_params import IPCreateParams as IPCreateParams
from .ip_delete_params import IPDeleteParams as IPDeleteParams

if TYPE_CHECKING:
    from .ip_create_response import IPCreateResponse as IPCreateResponse


def __getattr__(name: str) -> Any:
    if name == "IPCreateResponse":
        from .ip_create_response import IPCreateResponse

        return IPCreateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
