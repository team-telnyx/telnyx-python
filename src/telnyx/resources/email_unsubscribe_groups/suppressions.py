# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_block import EmailBlock
from ...types.email_block_response import EmailBlockResponse
from ...types.email_unsubscribe_groups import suppression_list_params, suppression_create_params

__all__ = ["SuppressionsResource", "AsyncSuppressionsResource"]


class SuppressionsResource(SyncAPIResource):
    """Named groups and group-scoped suppressions."""

    @cached_property
    def with_raw_response(self) -> SuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SuppressionsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """
        Creates a suppression with `reason: unsubscribe`, `source: manual`,
        `group_id: <this group>`. All other body fields are ignored; only `to` is read.
        Idempotent (same dedupe key → `200`, no new event).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email_unsubscribe_groups/{id}/suppressions", id=id),
            body=maybe_transform({"to": to}, suppression_create_params.SuppressionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def list(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EmailBlock]:
        """Account + group scoped.

        Offset pagination only (`page[number]` default 1,
        `page[size]` default 25, max 100). No `sort`/`filter`/ cursor — ordering fixed
        `desc created_at, desc id`. Uses the shared `QueryParser.parse_offset/1` — a
        malformed `page` returns `400` (code `10015`), consistent with
        `GET /v2/email_blocks`. `meta` includes `total_pages`. Rows reuse the standard
        suppression shape (`group_id` set to this group).

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/email_unsubscribe_groups/{id}/suppressions", id=id),
            page=SyncDefaultFlatPagination[EmailBlock],
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
                    suppression_list_params.SuppressionListParams,
                ),
            ),
            model=EmailBlock,
        )

    def delete(
        self,
        email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-deletes all active blocks for (account, group, normalized email) — one
        `removed` audit event per block (`actor: manual`). The `email` path segment is
        normalized (trim + lower-case) before matching. Idempotent on already-removed
        rows (returns `404` since they're no longer `active`).

        Two distinct `404` cases: a missing/cross-account **group** returns
        `10001 "The requested unsubscribe group was not found"`; a group that exists but
        has **no active suppression** for that email returns
        `10001 "The requested group suppression was not found"`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not email:
            raise ValueError(f"Expected a non-empty value for `email` but received {email!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/email_unsubscribe_groups/{id}/suppressions/{email}", id=id, email=email),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSuppressionsResource(AsyncAPIResource):
    """Named groups and group-scoped suppressions."""

    @cached_property
    def with_raw_response(self) -> AsyncSuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSuppressionsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        to: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailBlockResponse:
        """
        Creates a suppression with `reason: unsubscribe`, `source: manual`,
        `group_id: <this group>`. All other body fields are ignored; only `to` is read.
        Idempotent (same dedupe key → `200`, no new event).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email_unsubscribe_groups/{id}/suppressions", id=id),
            body=await async_maybe_transform({"to": to}, suppression_create_params.SuppressionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailBlockResponse,
        )

    def list(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailBlock, AsyncDefaultFlatPagination[EmailBlock]]:
        """Account + group scoped.

        Offset pagination only (`page[number]` default 1,
        `page[size]` default 25, max 100). No `sort`/`filter`/ cursor — ordering fixed
        `desc created_at, desc id`. Uses the shared `QueryParser.parse_offset/1` — a
        malformed `page` returns `400` (code `10015`), consistent with
        `GET /v2/email_blocks`. `meta` includes `total_pages`. Rows reuse the standard
        suppression shape (`group_id` set to this group).

        Args:
          page_number: Offset page number (≥1, default 1).

          page_size: Page size (1–100, default 25).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/email_unsubscribe_groups/{id}/suppressions", id=id),
            page=AsyncDefaultFlatPagination[EmailBlock],
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
                    suppression_list_params.SuppressionListParams,
                ),
            ),
            model=EmailBlock,
        )

    async def delete(
        self,
        email: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-deletes all active blocks for (account, group, normalized email) — one
        `removed` audit event per block (`actor: manual`). The `email` path segment is
        normalized (trim + lower-case) before matching. Idempotent on already-removed
        rows (returns `404` since they're no longer `active`).

        Two distinct `404` cases: a missing/cross-account **group** returns
        `10001 "The requested unsubscribe group was not found"`; a group that exists but
        has **no active suppression** for that email returns
        `10001 "The requested group suppression was not found"`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not email:
            raise ValueError(f"Expected a non-empty value for `email` but received {email!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/email_unsubscribe_groups/{id}/suppressions/{email}", id=id, email=email),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_raw_response_wrapper(
            suppressions.create,
        )
        self.list = to_raw_response_wrapper(
            suppressions.list,
        )
        self.delete = to_raw_response_wrapper(
            suppressions.delete,
        )


class AsyncSuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_raw_response_wrapper(
            suppressions.create,
        )
        self.list = async_to_raw_response_wrapper(
            suppressions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            suppressions.delete,
        )


class SuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_streamed_response_wrapper(
            suppressions.create,
        )
        self.list = to_streamed_response_wrapper(
            suppressions.list,
        )
        self.delete = to_streamed_response_wrapper(
            suppressions.delete,
        )


class AsyncSuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_streamed_response_wrapper(
            suppressions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            suppressions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            suppressions.delete,
        )
