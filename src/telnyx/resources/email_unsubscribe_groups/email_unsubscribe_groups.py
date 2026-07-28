# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    email_unsubscribe_group_list_params,
    email_unsubscribe_group_create_params,
    email_unsubscribe_group_delete_params,
    email_unsubscribe_group_update_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .suppressions import (
    SuppressionsResource,
    AsyncSuppressionsResource,
    SuppressionsResourceWithRawResponse,
    AsyncSuppressionsResourceWithRawResponse,
    SuppressionsResourceWithStreamingResponse,
    AsyncSuppressionsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.unsubscribe_group import UnsubscribeGroup
from ...types.unsubscribe_group_response import UnsubscribeGroupResponse

__all__ = ["EmailUnsubscribeGroupsResource", "AsyncEmailUnsubscribeGroupsResource"]


class EmailUnsubscribeGroupsResource(SyncAPIResource):
    """Named groups and group-scoped suppressions."""

    @cached_property
    def suppressions(self) -> SuppressionsResource:
        """Named groups and group-scoped suppressions."""
        return SuppressionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailUnsubscribeGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailUnsubscribeGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailUnsubscribeGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailUnsubscribeGroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeGroupResponse:
        """
        Create an unsubscribe group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/email_unsubscribe_groups",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                email_unsubscribe_group_create_params.EmailUnsubscribeGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
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
    ) -> UnsubscribeGroupResponse:
        """
        Retrieve an unsubscribe group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeGroupResponse:
        """Partial update (only `name` / `description`).

        `PUT` is not routed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                email_unsubscribe_group_update_params.EmailUnsubscribeGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[UnsubscribeGroup]:
        """
        Offset pagination only (`page[number]` default 1, `page[size]` default 25, max
        100). No `sort`/`filter`/cursor — ordering fixed `desc created_at, desc id`.
        Uses the shared `QueryParser.parse_offset/1` — a malformed `page` (e.g. flat
        `?page=1` instead of `?page[number]=1`) returns `400` (code `10015`), consistent
        with `GET /v2/email_blocks`. `meta` includes `total_pages`.

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_unsubscribe_groups",
            page=SyncDefaultFlatPagination[UnsubscribeGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    email_unsubscribe_group_list_params.EmailUnsubscribeGroupListParams,
                ),
            ),
            model=UnsubscribeGroup,
        )

    def delete(
        self,
        id: str,
        *,
        force: Union[Literal["true", "false"], bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """If the group has 0 active suppressions, hard-deletes the row.

        With `force=true`,
        soft-deletes all active suppressions first (status → `removed`, `group_id`
        cleared, `removed` audit event per block) in a single transaction, then
        hard-deletes the group. Without `force` and active suppressions present → `409`.
        Audit trail is preserved. `force` only accepts the string `"true"` or boolean
        `true`; all other values are false.

        Args:
          force: Force-delete a group with active suppressions. Only `"true"` (string) or `true`
              (bool) are truthy; all other values are false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"force": force}, email_unsubscribe_group_delete_params.EmailUnsubscribeGroupDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class AsyncEmailUnsubscribeGroupsResource(AsyncAPIResource):
    """Named groups and group-scoped suppressions."""

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResource:
        """Named groups and group-scoped suppressions."""
        return AsyncSuppressionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailUnsubscribeGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailUnsubscribeGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailUnsubscribeGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailUnsubscribeGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeGroupResponse:
        """
        Create an unsubscribe group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/email_unsubscribe_groups",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                email_unsubscribe_group_create_params.EmailUnsubscribeGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
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
    ) -> UnsubscribeGroupResponse:
        """
        Retrieve an unsubscribe group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnsubscribeGroupResponse:
        """Partial update (only `name` / `description`).

        `PUT` is not routed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                email_unsubscribe_group_update_params.EmailUnsubscribeGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UnsubscribeGroupResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UnsubscribeGroup, AsyncDefaultFlatPagination[UnsubscribeGroup]]:
        """
        Offset pagination only (`page[number]` default 1, `page[size]` default 25, max
        100). No `sort`/`filter`/cursor — ordering fixed `desc created_at, desc id`.
        Uses the shared `QueryParser.parse_offset/1` — a malformed `page` (e.g. flat
        `?page=1` instead of `?page[number]=1`) returns `400` (code `10015`), consistent
        with `GET /v2/email_blocks`. `meta` includes `total_pages`.

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_unsubscribe_groups",
            page=AsyncDefaultFlatPagination[UnsubscribeGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    email_unsubscribe_group_list_params.EmailUnsubscribeGroupListParams,
                ),
            ),
            model=UnsubscribeGroup,
        )

    async def delete(
        self,
        id: str,
        *,
        force: Union[Literal["true", "false"], bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """If the group has 0 active suppressions, hard-deletes the row.

        With `force=true`,
        soft-deletes all active suppressions first (status → `removed`, `group_id`
        cleared, `removed` audit event per block) in a single transaction, then
        hard-deletes the group. Without `force` and active suppressions present → `409`.
        Audit trail is preserved. `force` only accepts the string `"true"` or boolean
        `true`; all other values are false.

        Args:
          force: Force-delete a group with active suppressions. Only `"true"` (string) or `true`
              (bool) are truthy; all other values are false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email_unsubscribe_groups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"force": force}, email_unsubscribe_group_delete_params.EmailUnsubscribeGroupDeleteParams
                ),
            ),
            cast_to=NoneType,
        )


class EmailUnsubscribeGroupsResourceWithRawResponse:
    def __init__(self, email_unsubscribe_groups: EmailUnsubscribeGroupsResource) -> None:
        self._email_unsubscribe_groups = email_unsubscribe_groups

        self.create = to_raw_response_wrapper(
            email_unsubscribe_groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_unsubscribe_groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email_unsubscribe_groups.update,
        )
        self.list = to_raw_response_wrapper(
            email_unsubscribe_groups.list,
        )
        self.delete = to_raw_response_wrapper(
            email_unsubscribe_groups.delete,
        )

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithRawResponse:
        """Named groups and group-scoped suppressions."""
        return SuppressionsResourceWithRawResponse(self._email_unsubscribe_groups.suppressions)


class AsyncEmailUnsubscribeGroupsResourceWithRawResponse:
    def __init__(self, email_unsubscribe_groups: AsyncEmailUnsubscribeGroupsResource) -> None:
        self._email_unsubscribe_groups = email_unsubscribe_groups

        self.create = async_to_raw_response_wrapper(
            email_unsubscribe_groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_unsubscribe_groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email_unsubscribe_groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            email_unsubscribe_groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_unsubscribe_groups.delete,
        )

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithRawResponse:
        """Named groups and group-scoped suppressions."""
        return AsyncSuppressionsResourceWithRawResponse(self._email_unsubscribe_groups.suppressions)


class EmailUnsubscribeGroupsResourceWithStreamingResponse:
    def __init__(self, email_unsubscribe_groups: EmailUnsubscribeGroupsResource) -> None:
        self._email_unsubscribe_groups = email_unsubscribe_groups

        self.create = to_streamed_response_wrapper(
            email_unsubscribe_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_unsubscribe_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email_unsubscribe_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            email_unsubscribe_groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_unsubscribe_groups.delete,
        )

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithStreamingResponse:
        """Named groups and group-scoped suppressions."""
        return SuppressionsResourceWithStreamingResponse(self._email_unsubscribe_groups.suppressions)


class AsyncEmailUnsubscribeGroupsResourceWithStreamingResponse:
    def __init__(self, email_unsubscribe_groups: AsyncEmailUnsubscribeGroupsResource) -> None:
        self._email_unsubscribe_groups = email_unsubscribe_groups

        self.create = async_to_streamed_response_wrapper(
            email_unsubscribe_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_unsubscribe_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email_unsubscribe_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            email_unsubscribe_groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_unsubscribe_groups.delete,
        )

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """Named groups and group-scoped suppressions."""
        return AsyncSuppressionsResourceWithStreamingResponse(self._email_unsubscribe_groups.suppressions)
