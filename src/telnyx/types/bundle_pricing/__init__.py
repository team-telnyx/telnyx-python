# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .user_bundle_list_params import UserBundleListParams as UserBundleListParams
from .user_bundle_create_params import UserBundleCreateParams as UserBundleCreateParams
from .billing_bundle_list_params import BillingBundleListParams as BillingBundleListParams
from .user_bundle_list_unused_params import UserBundleListUnusedParams as UserBundleListUnusedParams

if TYPE_CHECKING:
    from .user_bundle import UserBundle as UserBundle
    from .pagination_response import PaginationResponse as PaginationResponse
    from .user_bundle_resource import UserBundleResource as UserBundleResource
    from .billing_bundle_summary import BillingBundleSummary as BillingBundleSummary
    from .user_bundle_create_response import UserBundleCreateResponse as UserBundleCreateResponse
    from .user_bundle_retrieve_response import UserBundleRetrieveResponse as UserBundleRetrieveResponse
    from .user_bundle_deactivate_response import UserBundleDeactivateResponse as UserBundleDeactivateResponse
    from .billing_bundle_retrieve_response import BillingBundleRetrieveResponse as BillingBundleRetrieveResponse
    from .user_bundle_list_unused_response import UserBundleListUnusedResponse as UserBundleListUnusedResponse
    from .user_bundle_list_resources_response import UserBundleListResourcesResponse as UserBundleListResourcesResponse


def __getattr__(name: str) -> Any:
    if name == "BillingBundleSummary":
        from .billing_bundle_summary import BillingBundleSummary

        return BillingBundleSummary
    if name == "PaginationResponse":
        from .pagination_response import PaginationResponse

        return PaginationResponse
    if name == "BillingBundleRetrieveResponse":
        from .billing_bundle_retrieve_response import BillingBundleRetrieveResponse

        return BillingBundleRetrieveResponse
    if name == "UserBundle":
        from .user_bundle import UserBundle

        return UserBundle
    if name == "UserBundleResource":
        from .user_bundle_resource import UserBundleResource

        return UserBundleResource
    if name == "UserBundleCreateResponse":
        from .user_bundle_create_response import UserBundleCreateResponse

        return UserBundleCreateResponse
    if name == "UserBundleRetrieveResponse":
        from .user_bundle_retrieve_response import UserBundleRetrieveResponse

        return UserBundleRetrieveResponse
    if name == "UserBundleDeactivateResponse":
        from .user_bundle_deactivate_response import UserBundleDeactivateResponse

        return UserBundleDeactivateResponse
    if name == "UserBundleListResourcesResponse":
        from .user_bundle_list_resources_response import UserBundleListResourcesResponse

        return UserBundleListResourcesResponse
    if name == "UserBundleListUnusedResponse":
        from .user_bundle_list_unused_response import UserBundleListUnusedResponse

        return UserBundleListUnusedResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
