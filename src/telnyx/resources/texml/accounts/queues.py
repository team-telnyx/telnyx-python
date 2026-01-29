# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultPaginationForQueues, AsyncDefaultPaginationForQueues
from ...._base_client import AsyncPaginator, make_request_options
from ....types.texml.accounts import queue_list_params, queue_create_params, queue_update_params
from ....types.texml.accounts.queue_list_response import QueueListResponse
from ....types.texml.accounts.queue_create_response import QueueCreateResponse
from ....types.texml.accounts.queue_update_response import QueueUpdateResponse
from ....types.texml.accounts.queue_retrieve_response import QueueRetrieveResponse

__all__ = ["QueuesResource", "AsyncQueuesResource"]


class QueuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return QueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return QueuesResourceWithStreamingResponse(self)

    def create(
        self,
        account_sid: str,
        *,
        friendly_name: str | Omit = omit,
        max_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueCreateResponse:
        """
        Creates a new queue resource.

        Args:
          friendly_name: A human readable name for the queue.

          max_size: The maximum size of the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Queues",
            body=maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "max_size": max_size,
                },
                queue_create_params.QueueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueCreateResponse,
        )

    def retrieve(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueRetrieveResponse:
        """
        Returns a queue resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueRetrieveResponse,
        )

    def update(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        max_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueUpdateResponse:
        """
        Updates a queue resource.

        Args:
          max_size: The maximum size of the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            body=maybe_transform({"max_size": max_size}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueUpdateResponse,
        )

    def list(
        self,
        account_sid: str,
        *,
        date_created: str | Omit = omit,
        date_updated: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultPaginationForQueues[QueueListResponse]:
        """
        Lists queue resources.

        Args:
          date_created: Filters conferences by the creation date. Expected format is YYYY-MM-DD. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          date_updated: Filters conferences by the time they were last updated. Expected format is
              YYYY-MM-DD. Also accepts inequality operators, e.g. DateUpdated>=2023-05-22.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get_api_list(
            f"/texml/Accounts/{account_sid}/Queues",
            page=SyncDefaultPaginationForQueues[QueueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "date_updated": date_updated,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    queue_list_params.QueueListParams,
                ),
            ),
            model=QueueListResponse,
        )

    def delete(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a queue resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncQueuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncQueuesResourceWithStreamingResponse(self)

    async def create(
        self,
        account_sid: str,
        *,
        friendly_name: str | Omit = omit,
        max_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueCreateResponse:
        """
        Creates a new queue resource.

        Args:
          friendly_name: A human readable name for the queue.

          max_size: The maximum size of the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Queues",
            body=await async_maybe_transform(
                {
                    "friendly_name": friendly_name,
                    "max_size": max_size,
                },
                queue_create_params.QueueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueCreateResponse,
        )

    async def retrieve(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueRetrieveResponse:
        """
        Returns a queue resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueRetrieveResponse,
        )

    async def update(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        max_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueUpdateResponse:
        """
        Updates a queue resource.

        Args:
          max_size: The maximum size of the queue.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            body=await async_maybe_transform({"max_size": max_size}, queue_update_params.QueueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueueUpdateResponse,
        )

    def list(
        self,
        account_sid: str,
        *,
        date_created: str | Omit = omit,
        date_updated: str | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        page_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[QueueListResponse, AsyncDefaultPaginationForQueues[QueueListResponse]]:
        """
        Lists queue resources.

        Args:
          date_created: Filters conferences by the creation date. Expected format is YYYY-MM-DD. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          date_updated: Filters conferences by the time they were last updated. Expected format is
              YYYY-MM-DD. Also accepts inequality operators, e.g. DateUpdated>=2023-05-22.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get_api_list(
            f"/texml/Accounts/{account_sid}/Queues",
            page=AsyncDefaultPaginationForQueues[QueueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "date_updated": date_updated,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    queue_list_params.QueueListParams,
                ),
            ),
            model=QueueListResponse,
        )

    async def delete(
        self,
        queue_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a queue resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not queue_sid:
            raise ValueError(f"Expected a non-empty value for `queue_sid` but received {queue_sid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/texml/Accounts/{account_sid}/Queues/{queue_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class QueuesResourceWithRawResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.create = to_raw_response_wrapper(
            queues.create,
        )
        self.retrieve = to_raw_response_wrapper(
            queues.retrieve,
        )
        self.update = to_raw_response_wrapper(
            queues.update,
        )
        self.list = to_raw_response_wrapper(
            queues.list,
        )
        self.delete = to_raw_response_wrapper(
            queues.delete,
        )


class AsyncQueuesResourceWithRawResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.create = async_to_raw_response_wrapper(
            queues.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            queues.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            queues.update,
        )
        self.list = async_to_raw_response_wrapper(
            queues.list,
        )
        self.delete = async_to_raw_response_wrapper(
            queues.delete,
        )


class QueuesResourceWithStreamingResponse:
    def __init__(self, queues: QueuesResource) -> None:
        self._queues = queues

        self.create = to_streamed_response_wrapper(
            queues.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            queues.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            queues.update,
        )
        self.list = to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = to_streamed_response_wrapper(
            queues.delete,
        )


class AsyncQueuesResourceWithStreamingResponse:
    def __init__(self, queues: AsyncQueuesResource) -> None:
        self._queues = queues

        self.create = async_to_streamed_response_wrapper(
            queues.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            queues.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            queues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            queues.delete,
        )
