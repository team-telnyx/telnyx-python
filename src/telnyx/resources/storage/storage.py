# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .buckets.buckets import (
    BucketsResource,
    AsyncBucketsResource,
    BucketsResourceWithRawResponse,
    AsyncBucketsResourceWithRawResponse,
    BucketsResourceWithStreamingResponse,
    AsyncBucketsResourceWithStreamingResponse,
)
from .migration_sources import (
    MigrationSourcesResource,
    AsyncMigrationSourcesResource,
    MigrationSourcesResourceWithRawResponse,
    AsyncMigrationSourcesResourceWithRawResponse,
    MigrationSourcesResourceWithStreamingResponse,
    AsyncMigrationSourcesResourceWithStreamingResponse,
)
from .migrations.migrations import (
    MigrationsResource,
    AsyncMigrationsResource,
    MigrationsResourceWithRawResponse,
    AsyncMigrationsResourceWithRawResponse,
    MigrationsResourceWithStreamingResponse,
    AsyncMigrationsResourceWithStreamingResponse,
)
from ...types.storage_list_migration_source_coverage_response import StorageListMigrationSourceCoverageResponse

__all__ = ["StorageResource", "AsyncStorageResource"]


class StorageResource(SyncAPIResource):
    @cached_property
    def buckets(self) -> BucketsResource:
        return BucketsResource(self._client)

    @cached_property
    def migration_sources(self) -> MigrationSourcesResource:
        return MigrationSourcesResource(self._client)

    @cached_property
    def migrations(self) -> MigrationsResource:
        return MigrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return StorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return StorageResourceWithStreamingResponse(self)

    def list_migration_source_coverage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StorageListMigrationSourceCoverageResponse:
        """List Migration Source coverage"""
        return self._get(
            "/storage/migration_source_coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageListMigrationSourceCoverageResponse,
        )


class AsyncStorageResource(AsyncAPIResource):
    @cached_property
    def buckets(self) -> AsyncBucketsResource:
        return AsyncBucketsResource(self._client)

    @cached_property
    def migration_sources(self) -> AsyncMigrationSourcesResource:
        return AsyncMigrationSourcesResource(self._client)

    @cached_property
    def migrations(self) -> AsyncMigrationsResource:
        return AsyncMigrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStorageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStorageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStorageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncStorageResourceWithStreamingResponse(self)

    async def list_migration_source_coverage(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StorageListMigrationSourceCoverageResponse:
        """List Migration Source coverage"""
        return await self._get(
            "/storage/migration_source_coverage",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StorageListMigrationSourceCoverageResponse,
        )


class StorageResourceWithRawResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.list_migration_source_coverage = to_raw_response_wrapper(
            storage.list_migration_source_coverage,
        )

    @cached_property
    def buckets(self) -> BucketsResourceWithRawResponse:
        return BucketsResourceWithRawResponse(self._storage.buckets)

    @cached_property
    def migration_sources(self) -> MigrationSourcesResourceWithRawResponse:
        return MigrationSourcesResourceWithRawResponse(self._storage.migration_sources)

    @cached_property
    def migrations(self) -> MigrationsResourceWithRawResponse:
        return MigrationsResourceWithRawResponse(self._storage.migrations)


class AsyncStorageResourceWithRawResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.list_migration_source_coverage = async_to_raw_response_wrapper(
            storage.list_migration_source_coverage,
        )

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithRawResponse:
        return AsyncBucketsResourceWithRawResponse(self._storage.buckets)

    @cached_property
    def migration_sources(self) -> AsyncMigrationSourcesResourceWithRawResponse:
        return AsyncMigrationSourcesResourceWithRawResponse(self._storage.migration_sources)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithRawResponse:
        return AsyncMigrationsResourceWithRawResponse(self._storage.migrations)


class StorageResourceWithStreamingResponse:
    def __init__(self, storage: StorageResource) -> None:
        self._storage = storage

        self.list_migration_source_coverage = to_streamed_response_wrapper(
            storage.list_migration_source_coverage,
        )

    @cached_property
    def buckets(self) -> BucketsResourceWithStreamingResponse:
        return BucketsResourceWithStreamingResponse(self._storage.buckets)

    @cached_property
    def migration_sources(self) -> MigrationSourcesResourceWithStreamingResponse:
        return MigrationSourcesResourceWithStreamingResponse(self._storage.migration_sources)

    @cached_property
    def migrations(self) -> MigrationsResourceWithStreamingResponse:
        return MigrationsResourceWithStreamingResponse(self._storage.migrations)


class AsyncStorageResourceWithStreamingResponse:
    def __init__(self, storage: AsyncStorageResource) -> None:
        self._storage = storage

        self.list_migration_source_coverage = async_to_streamed_response_wrapper(
            storage.list_migration_source_coverage,
        )

    @cached_property
    def buckets(self) -> AsyncBucketsResourceWithStreamingResponse:
        return AsyncBucketsResourceWithStreamingResponse(self._storage.buckets)

    @cached_property
    def migration_sources(self) -> AsyncMigrationSourcesResourceWithStreamingResponse:
        return AsyncMigrationSourcesResourceWithStreamingResponse(self._storage.migration_sources)

    @cached_property
    def migrations(self) -> AsyncMigrationsResourceWithStreamingResponse:
        return AsyncMigrationsResourceWithStreamingResponse(self._storage.migrations)
