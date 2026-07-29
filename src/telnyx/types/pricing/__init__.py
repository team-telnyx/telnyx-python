# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .product_list_params import ProductListParams as ProductListParams
from .product_retrieve_params import ProductRetrieveParams as ProductRetrieveParams

if TYPE_CHECKING:
    from .pricing_tier import PricingTier as PricingTier
    from .product_list_response import ProductListResponse as ProductListResponse
    from .pricing_pagination_meta import PricingPaginationMeta as PricingPaginationMeta
    from .product_retrieve_response import ProductRetrieveResponse as ProductRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "PricingPaginationMeta":
        from .pricing_pagination_meta import PricingPaginationMeta

        return PricingPaginationMeta
    if name == "PricingTier":
        from .pricing_tier import PricingTier

        return PricingTier
    if name == "ProductRetrieveResponse":
        from .product_retrieve_response import ProductRetrieveResponse

        return ProductRetrieveResponse
    if name == "ProductListResponse":
        from .product_list_response import ProductListResponse

        return ProductListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
