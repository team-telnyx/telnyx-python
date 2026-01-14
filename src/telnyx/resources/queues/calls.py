# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.queues import call_list_params, call_update_params
from ...types.queues.call_list_response import CallListResponse
from ...types.queues.call_retrieve_response import CallRetrieveResponse

__all__ = ["CallsResource", "AsyncCallsResource"]


class CallsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Retrieve an existing call from an existing queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return self._get(
            f"/queues/{queue_name}/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def update(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        keep_after_hangup: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update queued call's keep_after_hangup flag

        Args:
          keep_after_hangup: Whether the call should remain in queue after hangup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/queues/{queue_name}/calls/{call_control_id}",
            body=maybe_transform({"keep_after_hangup": keep_after_hangup}, call_update_params.CallUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        queue_name: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[CallListResponse]:
        """
        Retrieve the list of calls in an existing queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._get_api_list(
            f"/queues/{queue_name}/calls",
            page=SyncDefaultFlatPagination[CallListResponse],
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
                    call_list_params.CallListParams,
                ),
            ),
            model=CallListResponse,
        )

    def remove(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes an inactive call from a queue.

        If the call is no longer active, use this
        command to remove it from the queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/queues/{queue_name}/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCallsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallRetrieveResponse:
        """
        Retrieve an existing call from an existing queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        return await self._get(
            f"/queues/{queue_name}/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    async def update(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        keep_after_hangup: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update queued call's keep_after_hangup flag

        Args:
          keep_after_hangup: Whether the call should remain in queue after hangup.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/queues/{queue_name}/calls/{call_control_id}",
            body=await async_maybe_transform(
                {"keep_after_hangup": keep_after_hangup}, call_update_params.CallUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        queue_name: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CallListResponse, AsyncDefaultFlatPagination[CallListResponse]]:
        """
        Retrieve the list of calls in an existing queue

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._get_api_list(
            f"/queues/{queue_name}/calls",
            page=AsyncDefaultFlatPagination[CallListResponse],
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
                    call_list_params.CallListParams,
                ),
            ),
            model=CallListResponse,
        )

    async def remove(
        self,
        call_control_id: str,
        *,
        queue_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes an inactive call from a queue.

        If the call is no longer active, use this
        command to remove it from the queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        if not call_control_id:
            raise ValueError(f"Expected a non-empty value for `call_control_id` but received {call_control_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/queues/{queue_name}/calls/{call_control_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CallsResourceWithRawResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.update = to_raw_response_wrapper(
            calls.update,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )
        self.remove = to_raw_response_wrapper(
            calls.remove,
        )


class AsyncCallsResourceWithRawResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            calls.update,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )
        self.remove = async_to_raw_response_wrapper(
            calls.remove,
        )


class CallsResourceWithStreamingResponse:
    def __init__(self, calls: CallsResource) -> None:
        self._calls = calls

        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            calls.update,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )
        self.remove = to_streamed_response_wrapper(
            calls.remove,
        )


class AsyncCallsResourceWithStreamingResponse:
    def __init__(self, calls: AsyncCallsResource) -> None:
        self._calls = calls

        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            calls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            calls.remove,
        )
