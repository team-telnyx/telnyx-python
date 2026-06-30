# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .purchase_create_params import PurchaseCreateParams as PurchaseCreateParams
from .register_create_params import RegisterCreateParams as RegisterCreateParams

if TYPE_CHECKING:
    from .purchase_create_response import PurchaseCreateResponse as PurchaseCreateResponse
    from .register_create_response import RegisterCreateResponse as RegisterCreateResponse


def __getattr__(name: str) -> Any:
    if name == "PurchaseCreateResponse":
        from .purchase_create_response import PurchaseCreateResponse

        return PurchaseCreateResponse
    if name == "RegisterCreateResponse":
        from .register_create_response import RegisterCreateResponse

        return RegisterCreateResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
