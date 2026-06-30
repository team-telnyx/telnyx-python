# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .external_vetting_order_params import ExternalVettingOrderParams as ExternalVettingOrderParams
from .external_vetting_list_response import ExternalVettingListResponse as ExternalVettingListResponse
from .external_vetting_imports_params import ExternalVettingImportsParams as ExternalVettingImportsParams

if TYPE_CHECKING:
    from .external_vetting import ExternalVetting as ExternalVetting


def __getattr__(name: str) -> Any:
    if name == "ExternalVetting":
        from .external_vetting import ExternalVetting

        return ExternalVetting
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
