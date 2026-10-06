# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.whatsapp.phone_numbers import calling_routing_patch_all_params
from ....types.whatsapp.phone_numbers.calling_routing_list_response import CallingRoutingListResponse
from ....types.whatsapp.phone_numbers.calling_routing_patch_all_response import CallingRoutingPatchAllResponse

__all__ = ["CallingRoutingResource", "AsyncCallingRoutingResource"]


class CallingRoutingResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> CallingRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallingRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallingRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallingRoutingResourceWithStreamingResponse(self)

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingRoutingListResponse:
        """
        Retrieve the routing connection currently stored for a BYON (Bring Your Own
        Number) phone number: the connection that inbound WhatsApp calls to the number
        are delivered to.

        Use it to check the result of
        `PATCH /whatsapp/phone_numbers/{id}/calling_routing`. A read made immediately
        after an update can still return the previous value.

        Sub-users need read permission on connections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/whatsapp/phone_numbers/{id}/calling_routing", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingRoutingListResponse,
        )

    def patch_all(
        self,
        id: str,
        *,
        connection_id: Union[str, int, None],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingRoutingPatchAllResponse:
        """
        Set or clear the connection that inbound WhatsApp calls to a BYON (Bring Your
        Own Number) phone number are delivered to.

        The update is processed asynchronously. A `202` response means the request was
        accepted, not that the routing changed. Check the result with
        `GET /whatsapp/phone_numbers/{id}/calling_routing`, which can return the
        previous value immediately after an update. An update for a number that is not a
        WhatsApp Calling number in the account returns 404.

        The connection must belong to the same account and must not be a WhatsApp
        connection. Send `connection_id: null` to clear the routing; omitting
        `connection_id` is rejected. Numbers active on Telnyx are rejected, because they
        route through their own connection assignment.

        Sub-users need update permission on connections, and read permission to check
        the result with `GET`.

        Args:
          connection_id: ID of the connection to deliver inbound WhatsApp calls to: a positive integer up
              to 9223372036854775807, sent as a decimal string or an integer. Send a string to
              keep large IDs exact. Non-null values are returned as strings. `null` clears the
              routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/whatsapp/phone_numbers/{id}/calling_routing", id=id),
            body=maybe_transform(
                {"connection_id": connection_id}, calling_routing_patch_all_params.CallingRoutingPatchAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingRoutingPatchAllResponse,
        )


class AsyncCallingRoutingResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> AsyncCallingRoutingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallingRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallingRoutingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallingRoutingResourceWithStreamingResponse(self)

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingRoutingListResponse:
        """
        Retrieve the routing connection currently stored for a BYON (Bring Your Own
        Number) phone number: the connection that inbound WhatsApp calls to the number
        are delivered to.

        Use it to check the result of
        `PATCH /whatsapp/phone_numbers/{id}/calling_routing`. A read made immediately
        after an update can still return the previous value.

        Sub-users need read permission on connections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/whatsapp/phone_numbers/{id}/calling_routing", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingRoutingListResponse,
        )

    async def patch_all(
        self,
        id: str,
        *,
        connection_id: Union[str, int, None],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingRoutingPatchAllResponse:
        """
        Set or clear the connection that inbound WhatsApp calls to a BYON (Bring Your
        Own Number) phone number are delivered to.

        The update is processed asynchronously. A `202` response means the request was
        accepted, not that the routing changed. Check the result with
        `GET /whatsapp/phone_numbers/{id}/calling_routing`, which can return the
        previous value immediately after an update. An update for a number that is not a
        WhatsApp Calling number in the account returns 404.

        The connection must belong to the same account and must not be a WhatsApp
        connection. Send `connection_id: null` to clear the routing; omitting
        `connection_id` is rejected. Numbers active on Telnyx are rejected, because they
        route through their own connection assignment.

        Sub-users need update permission on connections, and read permission to check
        the result with `GET`.

        Args:
          connection_id: ID of the connection to deliver inbound WhatsApp calls to: a positive integer up
              to 9223372036854775807, sent as a decimal string or an integer. Send a string to
              keep large IDs exact. Non-null values are returned as strings. `null` clears the
              routing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/whatsapp/phone_numbers/{id}/calling_routing", id=id),
            body=await async_maybe_transform(
                {"connection_id": connection_id}, calling_routing_patch_all_params.CallingRoutingPatchAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingRoutingPatchAllResponse,
        )


class CallingRoutingResourceWithRawResponse:
    def __init__(self, calling_routing: CallingRoutingResource) -> None:
        self._calling_routing = calling_routing

        self.list = to_raw_response_wrapper(
            calling_routing.list,
        )
        self.patch_all = to_raw_response_wrapper(
            calling_routing.patch_all,
        )


class AsyncCallingRoutingResourceWithRawResponse:
    def __init__(self, calling_routing: AsyncCallingRoutingResource) -> None:
        self._calling_routing = calling_routing

        self.list = async_to_raw_response_wrapper(
            calling_routing.list,
        )
        self.patch_all = async_to_raw_response_wrapper(
            calling_routing.patch_all,
        )


class CallingRoutingResourceWithStreamingResponse:
    def __init__(self, calling_routing: CallingRoutingResource) -> None:
        self._calling_routing = calling_routing

        self.list = to_streamed_response_wrapper(
            calling_routing.list,
        )
        self.patch_all = to_streamed_response_wrapper(
            calling_routing.patch_all,
        )


class AsyncCallingRoutingResourceWithStreamingResponse:
    def __init__(self, calling_routing: AsyncCallingRoutingResource) -> None:
        self._calling_routing = calling_routing

        self.list = async_to_streamed_response_wrapper(
            calling_routing.list,
        )
        self.patch_all = async_to_streamed_response_wrapper(
            calling_routing.patch_all,
        )
