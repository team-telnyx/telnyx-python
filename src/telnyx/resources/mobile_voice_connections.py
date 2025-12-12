# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    mobile_voice_connection_list_params,
    mobile_voice_connection_create_params,
    mobile_voice_connection_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.mobile_voice_connection import MobileVoiceConnection
from ..types.mobile_voice_connection_create_response import MobileVoiceConnectionCreateResponse
from ..types.mobile_voice_connection_delete_response import MobileVoiceConnectionDeleteResponse
from ..types.mobile_voice_connection_update_response import MobileVoiceConnectionUpdateResponse
from ..types.mobile_voice_connection_retrieve_response import MobileVoiceConnectionRetrieveResponse

__all__ = ["MobileVoiceConnectionsResource", "AsyncMobileVoiceConnectionsResource"]


class MobileVoiceConnectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MobileVoiceConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MobileVoiceConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobileVoiceConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MobileVoiceConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        active: bool | Omit = omit,
        connection_name: str | Omit = omit,
        inbound: mobile_voice_connection_create_params.Inbound | Omit = omit,
        outbound: mobile_voice_connection_create_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionCreateResponse:
        """
        Create a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/mobile_voice_connections",
            body=maybe_transform(
                {
                    "active": active,
                    "connection_name": connection_name,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                mobile_voice_connection_create_params.MobileVoiceConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionCreateResponse,
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
    ) -> MobileVoiceConnectionRetrieveResponse:
        """
        Retrieve a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/mobile_voice_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        connection_name: str | Omit = omit,
        inbound: mobile_voice_connection_update_params.Inbound | Omit = omit,
        outbound: mobile_voice_connection_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionUpdateResponse:
        """
        Update a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/mobile_voice_connections/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "connection_name": connection_name,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                mobile_voice_connection_update_params.MobileVoiceConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter_connection_name_contains: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[MobileVoiceConnection]:
        """
        List Mobile Voice Connections

        Args:
          filter_connection_name_contains: Filter by connection name containing the given string

          page_number: The page number to load

          page_size: The size of the page

          sort: Sort by field (e.g., created_at, connection_name, active). Prefix with - for
              descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/mobile_voice_connections",
            page=SyncDefaultFlatPagination[MobileVoiceConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_connection_name_contains": filter_connection_name_contains,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    mobile_voice_connection_list_params.MobileVoiceConnectionListParams,
                ),
            ),
            model=MobileVoiceConnection,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionDeleteResponse:
        """
        Delete a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v2/mobile_voice_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionDeleteResponse,
        )


class AsyncMobileVoiceConnectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMobileVoiceConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMobileVoiceConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobileVoiceConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMobileVoiceConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        active: bool | Omit = omit,
        connection_name: str | Omit = omit,
        inbound: mobile_voice_connection_create_params.Inbound | Omit = omit,
        outbound: mobile_voice_connection_create_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionCreateResponse:
        """
        Create a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/mobile_voice_connections",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "connection_name": connection_name,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                mobile_voice_connection_create_params.MobileVoiceConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionCreateResponse,
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
    ) -> MobileVoiceConnectionRetrieveResponse:
        """
        Retrieve a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/mobile_voice_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        connection_name: str | Omit = omit,
        inbound: mobile_voice_connection_update_params.Inbound | Omit = omit,
        outbound: mobile_voice_connection_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_api_version: Literal["1", "2"] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_event_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionUpdateResponse:
        """
        Update a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/mobile_voice_connections/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "connection_name": connection_name,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_api_version": webhook_api_version,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                mobile_voice_connection_update_params.MobileVoiceConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter_connection_name_contains: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MobileVoiceConnection, AsyncDefaultFlatPagination[MobileVoiceConnection]]:
        """
        List Mobile Voice Connections

        Args:
          filter_connection_name_contains: Filter by connection name containing the given string

          page_number: The page number to load

          page_size: The size of the page

          sort: Sort by field (e.g., created_at, connection_name, active). Prefix with - for
              descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/mobile_voice_connections",
            page=AsyncDefaultFlatPagination[MobileVoiceConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_connection_name_contains": filter_connection_name_contains,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    mobile_voice_connection_list_params.MobileVoiceConnectionListParams,
                ),
            ),
            model=MobileVoiceConnection,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MobileVoiceConnectionDeleteResponse:
        """
        Delete a Mobile Voice Connection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v2/mobile_voice_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MobileVoiceConnectionDeleteResponse,
        )


class MobileVoiceConnectionsResourceWithRawResponse:
    def __init__(self, mobile_voice_connections: MobileVoiceConnectionsResource) -> None:
        self._mobile_voice_connections = mobile_voice_connections

        self.create = to_raw_response_wrapper(
            mobile_voice_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mobile_voice_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mobile_voice_connections.update,
        )
        self.list = to_raw_response_wrapper(
            mobile_voice_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            mobile_voice_connections.delete,
        )


class AsyncMobileVoiceConnectionsResourceWithRawResponse:
    def __init__(self, mobile_voice_connections: AsyncMobileVoiceConnectionsResource) -> None:
        self._mobile_voice_connections = mobile_voice_connections

        self.create = async_to_raw_response_wrapper(
            mobile_voice_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mobile_voice_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mobile_voice_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            mobile_voice_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mobile_voice_connections.delete,
        )


class MobileVoiceConnectionsResourceWithStreamingResponse:
    def __init__(self, mobile_voice_connections: MobileVoiceConnectionsResource) -> None:
        self._mobile_voice_connections = mobile_voice_connections

        self.create = to_streamed_response_wrapper(
            mobile_voice_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mobile_voice_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mobile_voice_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            mobile_voice_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            mobile_voice_connections.delete,
        )


class AsyncMobileVoiceConnectionsResourceWithStreamingResponse:
    def __init__(self, mobile_voice_connections: AsyncMobileVoiceConnectionsResource) -> None:
        self._mobile_voice_connections = mobile_voice_connections

        self.create = async_to_streamed_response_wrapper(
            mobile_voice_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mobile_voice_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mobile_voice_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mobile_voice_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mobile_voice_connections.delete,
        )
