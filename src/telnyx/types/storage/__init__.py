# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .kv_list_params import KvListParams as KvListParams
from .kv_create_params import KvCreateParams as KvCreateParams
from .migration_create_params import MigrationCreateParams as MigrationCreateParams
from .migration_source_create_params import MigrationSourceCreateParams as MigrationSourceCreateParams
from .bucket_create_presigned_url_params import BucketCreatePresignedURLParams as BucketCreatePresignedURLParams

if TYPE_CHECKING:
    from .kv_namespace import KvNamespace as KvNamespace
    from .migration_params import MigrationParams as MigrationParams
    from .migration_list_response import MigrationListResponse as MigrationListResponse
    from .migration_source_params import MigrationSourceParams as MigrationSourceParams
    from .migration_create_response import MigrationCreateResponse as MigrationCreateResponse
    from .migration_retrieve_response import MigrationRetrieveResponse as MigrationRetrieveResponse
    from .kv_namespace_response_wrapper import KvNamespaceResponseWrapper as KvNamespaceResponseWrapper
    from .migration_source_list_response import MigrationSourceListResponse as MigrationSourceListResponse
    from .migration_source_create_response import MigrationSourceCreateResponse as MigrationSourceCreateResponse
    from .migration_source_delete_response import MigrationSourceDeleteResponse as MigrationSourceDeleteResponse
    from .migration_source_retrieve_response import MigrationSourceRetrieveResponse as MigrationSourceRetrieveResponse
    from .bucket_create_presigned_url_response import (
        BucketCreatePresignedURLResponse as BucketCreatePresignedURLResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "BucketCreatePresignedURLResponse":
        from .bucket_create_presigned_url_response import BucketCreatePresignedURLResponse

        return BucketCreatePresignedURLResponse
    if name == "MigrationSourceParams":
        from .migration_source_params import MigrationSourceParams

        return MigrationSourceParams
    if name == "MigrationSourceCreateResponse":
        from .migration_source_create_response import MigrationSourceCreateResponse

        return MigrationSourceCreateResponse
    if name == "MigrationSourceRetrieveResponse":
        from .migration_source_retrieve_response import MigrationSourceRetrieveResponse

        return MigrationSourceRetrieveResponse
    if name == "MigrationSourceListResponse":
        from .migration_source_list_response import MigrationSourceListResponse

        return MigrationSourceListResponse
    if name == "MigrationSourceDeleteResponse":
        from .migration_source_delete_response import MigrationSourceDeleteResponse

        return MigrationSourceDeleteResponse
    if name == "MigrationParams":
        from .migration_params import MigrationParams

        return MigrationParams
    if name == "MigrationCreateResponse":
        from .migration_create_response import MigrationCreateResponse

        return MigrationCreateResponse
    if name == "MigrationRetrieveResponse":
        from .migration_retrieve_response import MigrationRetrieveResponse

        return MigrationRetrieveResponse
    if name == "MigrationListResponse":
        from .migration_list_response import MigrationListResponse

        return MigrationListResponse
    if name == "KvNamespace":
        from .kv_namespace import KvNamespace

        return KvNamespace
    if name == "KvNamespaceResponseWrapper":
        from .kv_namespace_response_wrapper import KvNamespaceResponseWrapper

        return KvNamespaceResponseWrapper
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
