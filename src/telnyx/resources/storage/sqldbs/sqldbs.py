# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.storage import sqldb_list_params, sqldb_create_params, sqldb_delete_params
from ....types.storage.sql_database import SqlDatabase
from ....types.storage.sql_database_response_wrapper import SqlDatabaseResponseWrapper

__all__ = ["SqldbsResource", "AsyncSqldbsResource"]


class SqldbsResource(SyncAPIResource):
    """Manage SQL databases and run SQL against them"""

    @cached_property
    def actions(self) -> ActionsResource:
        """Manage SQL databases and run SQL against them"""
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SqldbsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SqldbsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SqldbsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SqldbsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SqlDatabaseResponseWrapper:
        """Creates a new SQL database.

        Provisioning is asynchronous: the database is
        returned with status `pending` and becomes usable once it reaches
        `provision_ok`.

        Args:
          name: Database name. Lowercase letters, numbers, and hyphens only; must start and end
              with a letter or number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/sqldbs",
            body=maybe_transform({"name": name}, sqldb_create_params.SqldbCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlDatabaseResponseWrapper,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SqlDatabaseResponseWrapper:
        """
        Retrieves a SQL database by its ID, including its provisioning status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/storage/sqldbs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlDatabaseResponseWrapper,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_status: Literal["pending", "provision_ok", "provision_failed", "deleting", "delete_failed"]
        | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[SqlDatabase]:
        """Lists the SQL databases for the authenticated user's organization.

        Results use
        page-based pagination (`page[number]`/`page[size]`) and can be filtered and
        sorted.

        Args:
          filter_name: Filter by exact name match.

          filter_status: Filter by provisioning status.

          page_number: The page number to load.

          page_size: The size of the page. Values above 250 are treated as 250.

          sort: Sort field; prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/sqldbs",
            page=SyncDefaultFlatPagination[SqlDatabase],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    sqldb_list_params.SqldbListParams,
                ),
            ),
            model=SqlDatabase,
        )

    def delete(
        self,
        id: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a SQL database and all of the data it holds.

        Deletion is asynchronous
        and returns `202` with an empty body — the record is not removed synchronously.
        Poll `GET /storage/sqldbs/{id}`, which returns `404` once the database has been
        purged; there is no durable `deleted` state. A database still bound by a
        function is refused with `409` unless `force=true`.

        Args:
          force: Delete the database even when functions still bind it. Their bindings stop
              resolving.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storage/sqldbs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, sqldb_delete_params.SqldbDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncSqldbsResource(AsyncAPIResource):
    """Manage SQL databases and run SQL against them"""

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """Manage SQL databases and run SQL against them"""
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSqldbsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSqldbsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSqldbsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSqldbsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SqlDatabaseResponseWrapper:
        """Creates a new SQL database.

        Provisioning is asynchronous: the database is
        returned with status `pending` and becomes usable once it reaches
        `provision_ok`.

        Args:
          name: Database name. Lowercase letters, numbers, and hyphens only; must start and end
              with a letter or number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/sqldbs",
            body=await async_maybe_transform({"name": name}, sqldb_create_params.SqldbCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlDatabaseResponseWrapper,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SqlDatabaseResponseWrapper:
        """
        Retrieves a SQL database by its ID, including its provisioning status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/storage/sqldbs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SqlDatabaseResponseWrapper,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_status: Literal["pending", "provision_ok", "provision_failed", "deleting", "delete_failed"]
        | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SqlDatabase, AsyncDefaultFlatPagination[SqlDatabase]]:
        """Lists the SQL databases for the authenticated user's organization.

        Results use
        page-based pagination (`page[number]`/`page[size]`) and can be filtered and
        sorted.

        Args:
          filter_name: Filter by exact name match.

          filter_status: Filter by provisioning status.

          page_number: The page number to load.

          page_size: The size of the page. Values above 250 are treated as 250.

          sort: Sort field; prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/sqldbs",
            page=AsyncDefaultFlatPagination[SqlDatabase],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    sqldb_list_params.SqldbListParams,
                ),
            ),
            model=SqlDatabase,
        )

    async def delete(
        self,
        id: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a SQL database and all of the data it holds.

        Deletion is asynchronous
        and returns `202` with an empty body — the record is not removed synchronously.
        Poll `GET /storage/sqldbs/{id}`, which returns `404` once the database has been
        purged; there is no durable `deleted` state. A database still bound by a
        function is refused with `409` unless `force=true`.

        Args:
          force: Delete the database even when functions still bind it. Their bindings stop
              resolving.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storage/sqldbs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, sqldb_delete_params.SqldbDeleteParams),
            ),
            cast_to=NoneType,
        )


class SqldbsResourceWithRawResponse:
    def __init__(self, sqldbs: SqldbsResource) -> None:
        self._sqldbs = sqldbs

        self.create = to_raw_response_wrapper(
            sqldbs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sqldbs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            sqldbs.list,
        )
        self.delete = to_raw_response_wrapper(
            sqldbs.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """Manage SQL databases and run SQL against them"""
        return ActionsResourceWithRawResponse(self._sqldbs.actions)


class AsyncSqldbsResourceWithRawResponse:
    def __init__(self, sqldbs: AsyncSqldbsResource) -> None:
        self._sqldbs = sqldbs

        self.create = async_to_raw_response_wrapper(
            sqldbs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sqldbs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            sqldbs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sqldbs.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """Manage SQL databases and run SQL against them"""
        return AsyncActionsResourceWithRawResponse(self._sqldbs.actions)


class SqldbsResourceWithStreamingResponse:
    def __init__(self, sqldbs: SqldbsResource) -> None:
        self._sqldbs = sqldbs

        self.create = to_streamed_response_wrapper(
            sqldbs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sqldbs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            sqldbs.list,
        )
        self.delete = to_streamed_response_wrapper(
            sqldbs.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """Manage SQL databases and run SQL against them"""
        return ActionsResourceWithStreamingResponse(self._sqldbs.actions)


class AsyncSqldbsResourceWithStreamingResponse:
    def __init__(self, sqldbs: AsyncSqldbsResource) -> None:
        self._sqldbs = sqldbs

        self.create = async_to_streamed_response_wrapper(
            sqldbs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sqldbs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            sqldbs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sqldbs.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """Manage SQL databases and run SQL against them"""
        return AsyncActionsResourceWithStreamingResponse(self._sqldbs.actions)
