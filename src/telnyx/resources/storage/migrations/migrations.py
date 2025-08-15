# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage import migration_create_params
from ....types.storage.migration_list_response import MigrationListResponse
from ....types.storage.migration_create_response import MigrationCreateResponse
from ....types.storage.migration_retrieve_response import MigrationRetrieveResponse

__all__ = ["MigrationsResource", "AsyncMigrationsResource"]


class MigrationsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MigrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_id: str,
        target_bucket_name: str,
        target_region: str,
        refresh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationCreateResponse:
        """Initiate a migration of data from an external provider into Telnyx Cloud
        Storage.

        Currently, only S3 is supported.

        Args:
          source_id: ID of the Migration Source from which to migrate data.

          target_bucket_name: Bucket name to migrate the data into. Will default to the same name as the
              `source_bucket_name`.

          target_region: Telnyx Cloud Storage region to migrate the data to.

          refresh: If true, will continue to poll the source bucket to ensure new data is
              continually migrated over.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/migrations",
            body=maybe_transform(
                {
                    "source_id": source_id,
                    "target_bucket_name": target_bucket_name,
                    "target_region": target_region,
                    "refresh": refresh,
                },
                migration_create_params.MigrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationRetrieveResponse:
        """
        Get a Migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/storage/migrations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationListResponse:
        """List all Migrations"""
        return self._get(
            "/storage/migrations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationListResponse,
        )


class AsyncMigrationsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMigrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMigrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_id: str,
        target_bucket_name: str,
        target_region: str,
        refresh: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationCreateResponse:
        """Initiate a migration of data from an external provider into Telnyx Cloud
        Storage.

        Currently, only S3 is supported.

        Args:
          source_id: ID of the Migration Source from which to migrate data.

          target_bucket_name: Bucket name to migrate the data into. Will default to the same name as the
              `source_bucket_name`.

          target_region: Telnyx Cloud Storage region to migrate the data to.

          refresh: If true, will continue to poll the source bucket to ensure new data is
              continually migrated over.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/migrations",
            body=await async_maybe_transform(
                {
                    "source_id": source_id,
                    "target_bucket_name": target_bucket_name,
                    "target_region": target_region,
                    "refresh": refresh,
                },
                migration_create_params.MigrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationRetrieveResponse:
        """
        Get a Migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/storage/migrations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationListResponse:
        """List all Migrations"""
        return await self._get(
            "/storage/migrations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationListResponse,
        )


class MigrationsResourceWithRawResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

        self.create = to_raw_response_wrapper(
            migrations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            migrations.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._migrations.actions)


class AsyncMigrationsResourceWithRawResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

        self.create = async_to_raw_response_wrapper(
            migrations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            migrations.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._migrations.actions)


class MigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: MigrationsResource) -> None:
        self._migrations = migrations

        self.create = to_streamed_response_wrapper(
            migrations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            migrations.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._migrations.actions)


class AsyncMigrationsResourceWithStreamingResponse:
    def __init__(self, migrations: AsyncMigrationsResource) -> None:
        self._migrations = migrations

        self.create = async_to_streamed_response_wrapper(
            migrations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            migrations.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._migrations.actions)
