# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .usage_get_api_usage_params import UsageGetAPIUsageParams as UsageGetAPIUsageParams
from .ssl_certificate_create_params import SslCertificateCreateParams as SslCertificateCreateParams

if TYPE_CHECKING:
    from .ssl_certificate import SslCertificate as SslCertificate
    from .pagination_meta_simple import PaginationMetaSimple as PaginationMetaSimple
    from .usage_get_api_usage_response import UsageGetAPIUsageResponse as UsageGetAPIUsageResponse
    from .ssl_certificate_create_response import SslCertificateCreateResponse as SslCertificateCreateResponse
    from .ssl_certificate_delete_response import SslCertificateDeleteResponse as SslCertificateDeleteResponse
    from .usage_get_bucket_usage_response import UsageGetBucketUsageResponse as UsageGetBucketUsageResponse
    from .ssl_certificate_retrieve_response import SslCertificateRetrieveResponse as SslCertificateRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "SslCertificate":
        from .ssl_certificate import SslCertificate

        return SslCertificate
    if name == "SslCertificateCreateResponse":
        from .ssl_certificate_create_response import SslCertificateCreateResponse

        return SslCertificateCreateResponse
    if name == "SslCertificateRetrieveResponse":
        from .ssl_certificate_retrieve_response import SslCertificateRetrieveResponse

        return SslCertificateRetrieveResponse
    if name == "SslCertificateDeleteResponse":
        from .ssl_certificate_delete_response import SslCertificateDeleteResponse

        return SslCertificateDeleteResponse
    if name == "PaginationMetaSimple":
        from .pagination_meta_simple import PaginationMetaSimple

        return PaginationMetaSimple
    if name == "UsageGetAPIUsageResponse":
        from .usage_get_api_usage_response import UsageGetAPIUsageResponse

        return UsageGetAPIUsageResponse
    if name == "UsageGetBucketUsageResponse":
        from .usage_get_bucket_usage_response import UsageGetBucketUsageResponse

        return UsageGetBucketUsageResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
