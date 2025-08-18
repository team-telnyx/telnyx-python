# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
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
from ....types.messaging import rc_list_bulk_capabilities_params
from ....types.messaging.rc_invite_test_number_response import RcInviteTestNumberResponse
from ....types.messaging.rc_retrieve_capabilities_response import RcRetrieveCapabilitiesResponse
from ....types.messaging.rc_list_bulk_capabilities_response import RcListBulkCapabilitiesResponse

__all__ = ["RcsResource", "AsyncRcsResource"]


class RcsResource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        return AgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RcsResourceWithStreamingResponse(self)

    def invite_test_number(
        self,
        phone_number: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcInviteTestNumberResponse:
        """
        Adds a test phone number to an RCS agent for testing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._put(
            f"/messaging/rcs/test_number_invite/{id}/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcInviteTestNumberResponse,
        )

    def list_bulk_capabilities(
        self,
        *,
        agent_id: str,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcListBulkCapabilitiesResponse:
        """
        List RCS capabilities of a given batch of phone numbers

        Args:
          agent_id: RCS Agent ID

          phone_numbers: List of phone numbers to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/messaging/rcs/bulk_capabilities",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "phone_numbers": phone_numbers,
                },
                rc_list_bulk_capabilities_params.RcListBulkCapabilitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcListBulkCapabilitiesResponse,
        )

    def retrieve_capabilities(
        self,
        phone_number: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcRetrieveCapabilitiesResponse:
        """
        List RCS capabilities of a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/messaging/rcs/capabilities/{agent_id}/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcRetrieveCapabilitiesResponse,
        )


class AsyncRcsResource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        return AsyncAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRcsResourceWithStreamingResponse(self)

    async def invite_test_number(
        self,
        phone_number: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcInviteTestNumberResponse:
        """
        Adds a test phone number to an RCS agent for testing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._put(
            f"/messaging/rcs/test_number_invite/{id}/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcInviteTestNumberResponse,
        )

    async def list_bulk_capabilities(
        self,
        *,
        agent_id: str,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcListBulkCapabilitiesResponse:
        """
        List RCS capabilities of a given batch of phone numbers

        Args:
          agent_id: RCS Agent ID

          phone_numbers: List of phone numbers to check

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/messaging/rcs/bulk_capabilities",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "phone_numbers": phone_numbers,
                },
                rc_list_bulk_capabilities_params.RcListBulkCapabilitiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcListBulkCapabilitiesResponse,
        )

    async def retrieve_capabilities(
        self,
        phone_number: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RcRetrieveCapabilitiesResponse:
        """
        List RCS capabilities of a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/messaging/rcs/capabilities/{agent_id}/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RcRetrieveCapabilitiesResponse,
        )


class RcsResourceWithRawResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.invite_test_number = to_raw_response_wrapper(
            rcs.invite_test_number,
        )
        self.list_bulk_capabilities = to_raw_response_wrapper(
            rcs.list_bulk_capabilities,
        )
        self.retrieve_capabilities = to_raw_response_wrapper(
            rcs.retrieve_capabilities,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        return AgentsResourceWithRawResponse(self._rcs.agents)


class AsyncRcsResourceWithRawResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.invite_test_number = async_to_raw_response_wrapper(
            rcs.invite_test_number,
        )
        self.list_bulk_capabilities = async_to_raw_response_wrapper(
            rcs.list_bulk_capabilities,
        )
        self.retrieve_capabilities = async_to_raw_response_wrapper(
            rcs.retrieve_capabilities,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._rcs.agents)


class RcsResourceWithStreamingResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.invite_test_number = to_streamed_response_wrapper(
            rcs.invite_test_number,
        )
        self.list_bulk_capabilities = to_streamed_response_wrapper(
            rcs.list_bulk_capabilities,
        )
        self.retrieve_capabilities = to_streamed_response_wrapper(
            rcs.retrieve_capabilities,
        )

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._rcs.agents)


class AsyncRcsResourceWithStreamingResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.invite_test_number = async_to_streamed_response_wrapper(
            rcs.invite_test_number,
        )
        self.list_bulk_capabilities = async_to_streamed_response_wrapper(
            rcs.list_bulk_capabilities,
        )
        self.retrieve_capabilities = async_to_streamed_response_wrapper(
            rcs.retrieve_capabilities,
        )

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._rcs.agents)
