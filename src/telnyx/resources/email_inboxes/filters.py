# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_inboxes import filter_add_params, filter_replace_params, filter_delete_all_params
from ...types.email_inboxes.filter_add_response import FilterAddResponse
from ...types.email_inboxes.filter_list_response import FilterListResponse
from ...types.email_inboxes.filter_replace_response import FilterReplaceResponse
from ...types.email_inboxes.filter_delete_all_response import FilterDeleteAllResponse

__all__ = ["FiltersResource", "AsyncFiltersResource"]


class FiltersResource(SyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> FiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FiltersResourceWithStreamingResponse(self)

    def list(
        self,
        inbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterListResponse:
        """Returns the inbox's sender allowlist and blocklist.

        Entries are normalized to
        lowercase. A blocklist match takes precedence over an allowlist match; when both
        lists are empty, all senders are accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._get(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterListResponse,
        )

    def add(
        self,
        inbox_id: str,
        *,
        entries: SequenceNotStr[str],
        type: Literal["allowlist", "blocklist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterAddResponse:
        """Adds entries to either the allowlist or blocklist.

        The operation is an
        idempotent set union: entries already present remain unchanged.

        Args:
          type: The list to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._post(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=maybe_transform(
                {
                    "entries": entries,
                    "type": type,
                },
                filter_add_params.FilterAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterAddResponse,
        )

    def delete_all(
        self,
        inbox_id: str,
        *,
        entries: SequenceNotStr[str],
        type: Literal["allowlist", "blocklist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterDeleteAllResponse:
        """Removes entries from either the allowlist or blocklist.

        The operation is
        idempotent: removing an entry that is not present still returns the current
        filter lists.

        Args:
          type: The list to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._delete(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=maybe_transform(
                {
                    "entries": entries,
                    "type": type,
                },
                filter_delete_all_params.FilterDeleteAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterDeleteAllResponse,
        )

    def replace(
        self,
        inbox_id: str,
        *,
        allowlist: SequenceNotStr[str] | Omit = omit,
        blocklist: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterReplaceResponse:
        """Replaces both sender filter lists atomically.

        Omitting either list clears that
        list. Use `POST` or `DELETE` for incremental changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return self._put(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=maybe_transform(
                {
                    "allowlist": allowlist,
                    "blocklist": blocklist,
                },
                filter_replace_params.FilterReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterReplaceResponse,
        )


class AsyncFiltersResource(AsyncAPIResource):
    """
    Create and manage agent inboxes, retrieve inbound messages and threads, and reply to or forward messages.
    """

    @cached_property
    def with_raw_response(self) -> AsyncFiltersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFiltersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFiltersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFiltersResourceWithStreamingResponse(self)

    async def list(
        self,
        inbox_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterListResponse:
        """Returns the inbox's sender allowlist and blocklist.

        Entries are normalized to
        lowercase. A blocklist match takes precedence over an allowlist match; when both
        lists are empty, all senders are accepted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._get(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterListResponse,
        )

    async def add(
        self,
        inbox_id: str,
        *,
        entries: SequenceNotStr[str],
        type: Literal["allowlist", "blocklist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterAddResponse:
        """Adds entries to either the allowlist or blocklist.

        The operation is an
        idempotent set union: entries already present remain unchanged.

        Args:
          type: The list to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._post(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=await async_maybe_transform(
                {
                    "entries": entries,
                    "type": type,
                },
                filter_add_params.FilterAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterAddResponse,
        )

    async def delete_all(
        self,
        inbox_id: str,
        *,
        entries: SequenceNotStr[str],
        type: Literal["allowlist", "blocklist"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterDeleteAllResponse:
        """Removes entries from either the allowlist or blocklist.

        The operation is
        idempotent: removing an entry that is not present still returns the current
        filter lists.

        Args:
          type: The list to change.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._delete(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=await async_maybe_transform(
                {
                    "entries": entries,
                    "type": type,
                },
                filter_delete_all_params.FilterDeleteAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterDeleteAllResponse,
        )

    async def replace(
        self,
        inbox_id: str,
        *,
        allowlist: SequenceNotStr[str] | Omit = omit,
        blocklist: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilterReplaceResponse:
        """Replaces both sender filter lists atomically.

        Omitting either list clears that
        list. Use `POST` or `DELETE` for incremental changes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not inbox_id:
            raise ValueError(f"Expected a non-empty value for `inbox_id` but received {inbox_id!r}")
        return await self._put(
            path_template("/email_inboxes/{inbox_id}/filters", inbox_id=inbox_id),
            body=await async_maybe_transform(
                {
                    "allowlist": allowlist,
                    "blocklist": blocklist,
                },
                filter_replace_params.FilterReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilterReplaceResponse,
        )


class FiltersResourceWithRawResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.list = to_raw_response_wrapper(
            filters.list,
        )
        self.add = to_raw_response_wrapper(
            filters.add,
        )
        self.delete_all = to_raw_response_wrapper(
            filters.delete_all,
        )
        self.replace = to_raw_response_wrapper(
            filters.replace,
        )


class AsyncFiltersResourceWithRawResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.list = async_to_raw_response_wrapper(
            filters.list,
        )
        self.add = async_to_raw_response_wrapper(
            filters.add,
        )
        self.delete_all = async_to_raw_response_wrapper(
            filters.delete_all,
        )
        self.replace = async_to_raw_response_wrapper(
            filters.replace,
        )


class FiltersResourceWithStreamingResponse:
    def __init__(self, filters: FiltersResource) -> None:
        self._filters = filters

        self.list = to_streamed_response_wrapper(
            filters.list,
        )
        self.add = to_streamed_response_wrapper(
            filters.add,
        )
        self.delete_all = to_streamed_response_wrapper(
            filters.delete_all,
        )
        self.replace = to_streamed_response_wrapper(
            filters.replace,
        )


class AsyncFiltersResourceWithStreamingResponse:
    def __init__(self, filters: AsyncFiltersResource) -> None:
        self._filters = filters

        self.list = async_to_streamed_response_wrapper(
            filters.list,
        )
        self.add = async_to_streamed_response_wrapper(
            filters.add,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            filters.delete_all,
        )
        self.replace = async_to_streamed_response_wrapper(
            filters.replace,
        )
