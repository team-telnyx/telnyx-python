# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .v1_systemone_params import V1SystemoneParams as V1SystemoneParams

if TYPE_CHECKING:
    from .v1_systemone_response import V1SystemoneResponse as V1SystemoneResponse


def __getattr__(name: str) -> Any:
    if name == "V1SystemoneResponse":
        from .v1_systemone_response import V1SystemoneResponse

        return V1SystemoneResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
