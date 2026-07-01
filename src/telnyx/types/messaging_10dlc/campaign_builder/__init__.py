# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .brand_qualify_by_usecase_response import BrandQualifyByUsecaseResponse as BrandQualifyByUsecaseResponse


def __getattr__(name: str) -> Any:
    if name == "BrandQualifyByUsecaseResponse":
        from .brand_qualify_by_usecase_response import BrandQualifyByUsecaseResponse

        return BrandQualifyByUsecaseResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
