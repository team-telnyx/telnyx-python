# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.storage import migration_source_create_params
from ...types.storage.migration_source_list_response import MigrationSourceListResponse
from ...types.storage.migration_source_create_response import MigrationSourceCreateResponse
from ...types.storage.migration_source_delete_response import MigrationSourceDeleteResponse
from ...types.storage.migration_source_retrieve_response import MigrationSourceRetrieveResponse

__all__ = ["MigrationSourcesResource", "AsyncMigrationSourcesResource"]


class MigrationSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MigrationSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MigrationSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MigrationSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        bucket_name: str,
        provider: Literal["aws", "telnyx"],
        provider_auth: migration_source_create_params.ProviderAuth,
        source_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationSourceCreateResponse:
        """
        Create a source from which data can be migrated from.

        Args:
          bucket_name: Bucket name to migrate the data from.

          provider: Cloud provider from which to migrate data. Use 'telnyx' if you want to migrate
              data from one Telnyx bucket to another.

          source_region: For intra-Telnyx buckets migration, specify the source bucket region in this
              field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/migration_sources",
            body=maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "provider": provider,
                    "provider_auth": provider_auth,
                    "source_region": source_region,
                },
                migration_source_create_params.MigrationSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceCreateResponse,
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
    ) -> MigrationSourceRetrieveResponse:
        """
        Get a Migration Source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/storage/migration_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceRetrieveResponse,
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
    ) -> MigrationSourceListResponse:
        """List all Migration Sources"""
        return self._get(
            "/storage/migration_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationSourceDeleteResponse:
        """
        Delete a Migration Source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/storage/migration_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceDeleteResponse,
        )


class AsyncMigrationSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMigrationSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMigrationSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        bucket_name: str,
        provider: Literal["aws", "telnyx"],
        provider_auth: migration_source_create_params.ProviderAuth,
        source_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationSourceCreateResponse:
        """
        Create a source from which data can be migrated from.

        Args:
          bucket_name: Bucket name to migrate the data from.

          provider: Cloud provider from which to migrate data. Use 'telnyx' if you want to migrate
              data from one Telnyx bucket to another.

          source_region: For intra-Telnyx buckets migration, specify the source bucket region in this
              field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/migration_sources",
            body=await async_maybe_transform(
                {
                    "bucket_name": bucket_name,
                    "provider": provider,
                    "provider_auth": provider_auth,
                    "source_region": source_region,
                },
                migration_source_create_params.MigrationSourceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceCreateResponse,
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
    ) -> MigrationSourceRetrieveResponse:
        """
        Get a Migration Source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/storage/migration_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceRetrieveResponse,
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
    ) -> MigrationSourceListResponse:
        """List all Migration Sources"""
        return await self._get(
            "/storage/migration_sources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MigrationSourceDeleteResponse:
        """
        Delete a Migration Source

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/storage/migration_sources/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationSourceDeleteResponse,
        )


class MigrationSourcesResourceWithRawResponse:
    def __init__(self, migration_sources: MigrationSourcesResource) -> None:
        self._migration_sources = migration_sources

        self.create = to_raw_response_wrapper(
            migration_sources.create,
        )
        self.retrieve = to_raw_response_wrapper(
            migration_sources.retrieve,
        )
        self.list = to_raw_response_wrapper(
            migration_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            migration_sources.delete,
        )


class AsyncMigrationSourcesResourceWithRawResponse:
    def __init__(self, migration_sources: AsyncMigrationSourcesResource) -> None:
        self._migration_sources = migration_sources

        self.create = async_to_raw_response_wrapper(
            migration_sources.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            migration_sources.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            migration_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            migration_sources.delete,
        )


class MigrationSourcesResourceWithStreamingResponse:
    def __init__(self, migration_sources: MigrationSourcesResource) -> None:
        self._migration_sources = migration_sources

        self.create = to_streamed_response_wrapper(
            migration_sources.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            migration_sources.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            migration_sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            migration_sources.delete,
        )


class AsyncMigrationSourcesResourceWithStreamingResponse:
    def __init__(self, migration_sources: AsyncMigrationSourcesResource) -> None:
        self._migration_sources = migration_sources

        self.create = async_to_streamed_response_wrapper(
            migration_sources.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            migration_sources.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            migration_sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            migration_sources.delete,
        )
