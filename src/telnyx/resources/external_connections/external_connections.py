# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    external_connection_list_params,
    external_connection_create_params,
    external_connection_update_params,
    external_connection_update_location_params,
)
from .uploads import (
    UploadsResource,
    AsyncUploadsResource,
    UploadsResourceWithRawResponse,
    AsyncUploadsResourceWithRawResponse,
    UploadsResourceWithStreamingResponse,
    AsyncUploadsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .releases import (
    ReleasesResource,
    AsyncReleasesResource,
    ReleasesResourceWithRawResponse,
    AsyncReleasesResourceWithRawResponse,
    ReleasesResourceWithStreamingResponse,
    AsyncReleasesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .log_messages import (
    LogMessagesResource,
    AsyncLogMessagesResource,
    LogMessagesResourceWithRawResponse,
    AsyncLogMessagesResourceWithRawResponse,
    LogMessagesResourceWithStreamingResponse,
    AsyncLogMessagesResourceWithStreamingResponse,
)
from .phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .civic_addresses import (
    CivicAddressesResource,
    AsyncCivicAddressesResource,
    CivicAddressesResourceWithRawResponse,
    AsyncCivicAddressesResourceWithRawResponse,
    CivicAddressesResourceWithStreamingResponse,
    AsyncCivicAddressesResourceWithStreamingResponse,
)
from ...types.external_connection_list_response import ExternalConnectionListResponse
from ...types.external_connection_create_response import ExternalConnectionCreateResponse
from ...types.external_connection_delete_response import ExternalConnectionDeleteResponse
from ...types.external_connection_update_response import ExternalConnectionUpdateResponse
from ...types.external_connection_retrieve_response import ExternalConnectionRetrieveResponse
from ...types.external_connection_update_location_response import ExternalConnectionUpdateLocationResponse

__all__ = ["ExternalConnectionsResource", "AsyncExternalConnectionsResource"]


class ExternalConnectionsResource(SyncAPIResource):
    @cached_property
    def log_messages(self) -> LogMessagesResource:
        return LogMessagesResource(self._client)

    @cached_property
    def civic_addresses(self) -> CivicAddressesResource:
        return CivicAddressesResource(self._client)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        return PhoneNumbersResource(self._client)

    @cached_property
    def releases(self) -> ReleasesResource:
        return ReleasesResource(self._client)

    @cached_property
    def uploads(self) -> UploadsResource:
        return UploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ExternalConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ExternalConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        external_sip_connection: Literal["zoom"],
        outbound: external_connection_create_params.Outbound,
        active: bool | NotGiven = NOT_GIVEN,
        inbound: external_connection_create_params.Inbound | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionCreateResponse:
        """
        Creates a new External Connection based on the parameters sent in the request.
        The external_sip_connection and outbound voice profile id are required. Once
        created, you can assign phone numbers to your application using the
        `/phone_numbers` endpoint.

        Args:
          external_sip_connection: The service that will be consuming this connection.

          active: Specifies whether the connection can be used.

          tags: Tags associated with the connection.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/external_connections",
            body=maybe_transform(
                {
                    "external_sip_connection": external_sip_connection,
                    "outbound": outbound,
                    "active": active,
                    "inbound": inbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                external_connection_create_params.ExternalConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionCreateResponse,
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
    ) -> ExternalConnectionRetrieveResponse:
        """
        Return the details of an existing External Connection inside the 'data'
        attribute of the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        outbound: external_connection_update_params.Outbound,
        active: bool | NotGiven = NOT_GIVEN,
        inbound: external_connection_update_params.Inbound | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionUpdateResponse:
        """
        Updates settings of an existing External Connection based on the parameters of
        the request.

        Args:
          active: Specifies whether the connection can be used.

          tags: Tags associated with the connection.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/external_connections/{id}",
            body=maybe_transform(
                {
                    "outbound": outbound,
                    "active": active,
                    "inbound": inbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                external_connection_update_params.ExternalConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionUpdateResponse,
        )

    def list(
        self,
        *,
        filter: external_connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: external_connection_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionListResponse:
        """
        This endpoint returns a list of your External Connections inside the 'data'
        attribute of the response. External Connections are used by Telnyx customers to
        seamless configure SIP trunking integrations with Telnyx Partners, through
        External Voice Integrations in Mission Control Portal.

        Args:
          filter: Filter parameter for external connections (deepObject style). Supports filtering
              by connection_name, external_sip_connection, id, created_at, and phone_number.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/external_connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    external_connection_list_params.ExternalConnectionListParams,
                ),
            ),
            cast_to=ExternalConnectionListResponse,
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
    ) -> ExternalConnectionDeleteResponse:
        """Permanently deletes an External Connection.

        Deletion may be prevented if the
        application is in use by phone numbers, is active, or if it is an Operator
        Connect connection. To remove an Operator Connect integration please contact
        Telnyx support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/external_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionDeleteResponse,
        )

    def update_location(
        self,
        location_id: str,
        *,
        id: str,
        static_emergency_address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionUpdateLocationResponse:
        """
        Update a location's static emergency address

        Args:
          static_emergency_address_id: A new static emergency address ID to update the location with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return self._patch(
            f"/external_connections/{id}/locations/{location_id}",
            body=maybe_transform(
                {"static_emergency_address_id": static_emergency_address_id},
                external_connection_update_location_params.ExternalConnectionUpdateLocationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionUpdateLocationResponse,
        )


class AsyncExternalConnectionsResource(AsyncAPIResource):
    @cached_property
    def log_messages(self) -> AsyncLogMessagesResource:
        return AsyncLogMessagesResource(self._client)

    @cached_property
    def civic_addresses(self) -> AsyncCivicAddressesResource:
        return AsyncCivicAddressesResource(self._client)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def releases(self) -> AsyncReleasesResource:
        return AsyncReleasesResource(self._client)

    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        return AsyncUploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncExternalConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_sip_connection: Literal["zoom"],
        outbound: external_connection_create_params.Outbound,
        active: bool | NotGiven = NOT_GIVEN,
        inbound: external_connection_create_params.Inbound | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionCreateResponse:
        """
        Creates a new External Connection based on the parameters sent in the request.
        The external_sip_connection and outbound voice profile id are required. Once
        created, you can assign phone numbers to your application using the
        `/phone_numbers` endpoint.

        Args:
          external_sip_connection: The service that will be consuming this connection.

          active: Specifies whether the connection can be used.

          tags: Tags associated with the connection.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/external_connections",
            body=await async_maybe_transform(
                {
                    "external_sip_connection": external_sip_connection,
                    "outbound": outbound,
                    "active": active,
                    "inbound": inbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                external_connection_create_params.ExternalConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionCreateResponse,
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
    ) -> ExternalConnectionRetrieveResponse:
        """
        Return the details of an existing External Connection inside the 'data'
        attribute of the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        outbound: external_connection_update_params.Outbound,
        active: bool | NotGiven = NOT_GIVEN,
        inbound: external_connection_update_params.Inbound | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook_event_failover_url: Optional[str] | NotGiven = NOT_GIVEN,
        webhook_event_url: str | NotGiven = NOT_GIVEN,
        webhook_timeout_secs: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionUpdateResponse:
        """
        Updates settings of an existing External Connection based on the parameters of
        the request.

        Args:
          active: Specifies whether the connection can be used.

          tags: Tags associated with the connection.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/external_connections/{id}",
            body=await async_maybe_transform(
                {
                    "outbound": outbound,
                    "active": active,
                    "inbound": inbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_event_url": webhook_event_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                external_connection_update_params.ExternalConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: external_connection_list_params.Filter | NotGiven = NOT_GIVEN,
        page: external_connection_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionListResponse:
        """
        This endpoint returns a list of your External Connections inside the 'data'
        attribute of the response. External Connections are used by Telnyx customers to
        seamless configure SIP trunking integrations with Telnyx Partners, through
        External Voice Integrations in Mission Control Portal.

        Args:
          filter: Filter parameter for external connections (deepObject style). Supports filtering
              by connection_name, external_sip_connection, id, created_at, and phone_number.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/external_connections",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    external_connection_list_params.ExternalConnectionListParams,
                ),
            ),
            cast_to=ExternalConnectionListResponse,
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
    ) -> ExternalConnectionDeleteResponse:
        """Permanently deletes an External Connection.

        Deletion may be prevented if the
        application is in use by phone numbers, is active, or if it is an Operator
        Connect connection. To remove an Operator Connect integration please contact
        Telnyx support.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/external_connections/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionDeleteResponse,
        )

    async def update_location(
        self,
        location_id: str,
        *,
        id: str,
        static_emergency_address_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalConnectionUpdateLocationResponse:
        """
        Update a location's static emergency address

        Args:
          static_emergency_address_id: A new static emergency address ID to update the location with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not location_id:
            raise ValueError(f"Expected a non-empty value for `location_id` but received {location_id!r}")
        return await self._patch(
            f"/external_connections/{id}/locations/{location_id}",
            body=await async_maybe_transform(
                {"static_emergency_address_id": static_emergency_address_id},
                external_connection_update_location_params.ExternalConnectionUpdateLocationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalConnectionUpdateLocationResponse,
        )


class ExternalConnectionsResourceWithRawResponse:
    def __init__(self, external_connections: ExternalConnectionsResource) -> None:
        self._external_connections = external_connections

        self.create = to_raw_response_wrapper(
            external_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            external_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            external_connections.update,
        )
        self.list = to_raw_response_wrapper(
            external_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            external_connections.delete,
        )
        self.update_location = to_raw_response_wrapper(
            external_connections.update_location,
        )

    @cached_property
    def log_messages(self) -> LogMessagesResourceWithRawResponse:
        return LogMessagesResourceWithRawResponse(self._external_connections.log_messages)

    @cached_property
    def civic_addresses(self) -> CivicAddressesResourceWithRawResponse:
        return CivicAddressesResourceWithRawResponse(self._external_connections.civic_addresses)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        return PhoneNumbersResourceWithRawResponse(self._external_connections.phone_numbers)

    @cached_property
    def releases(self) -> ReleasesResourceWithRawResponse:
        return ReleasesResourceWithRawResponse(self._external_connections.releases)

    @cached_property
    def uploads(self) -> UploadsResourceWithRawResponse:
        return UploadsResourceWithRawResponse(self._external_connections.uploads)


class AsyncExternalConnectionsResourceWithRawResponse:
    def __init__(self, external_connections: AsyncExternalConnectionsResource) -> None:
        self._external_connections = external_connections

        self.create = async_to_raw_response_wrapper(
            external_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            external_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            external_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            external_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            external_connections.delete,
        )
        self.update_location = async_to_raw_response_wrapper(
            external_connections.update_location,
        )

    @cached_property
    def log_messages(self) -> AsyncLogMessagesResourceWithRawResponse:
        return AsyncLogMessagesResourceWithRawResponse(self._external_connections.log_messages)

    @cached_property
    def civic_addresses(self) -> AsyncCivicAddressesResourceWithRawResponse:
        return AsyncCivicAddressesResourceWithRawResponse(self._external_connections.civic_addresses)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        return AsyncPhoneNumbersResourceWithRawResponse(self._external_connections.phone_numbers)

    @cached_property
    def releases(self) -> AsyncReleasesResourceWithRawResponse:
        return AsyncReleasesResourceWithRawResponse(self._external_connections.releases)

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithRawResponse:
        return AsyncUploadsResourceWithRawResponse(self._external_connections.uploads)


class ExternalConnectionsResourceWithStreamingResponse:
    def __init__(self, external_connections: ExternalConnectionsResource) -> None:
        self._external_connections = external_connections

        self.create = to_streamed_response_wrapper(
            external_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            external_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            external_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            external_connections.delete,
        )
        self.update_location = to_streamed_response_wrapper(
            external_connections.update_location,
        )

    @cached_property
    def log_messages(self) -> LogMessagesResourceWithStreamingResponse:
        return LogMessagesResourceWithStreamingResponse(self._external_connections.log_messages)

    @cached_property
    def civic_addresses(self) -> CivicAddressesResourceWithStreamingResponse:
        return CivicAddressesResourceWithStreamingResponse(self._external_connections.civic_addresses)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        return PhoneNumbersResourceWithStreamingResponse(self._external_connections.phone_numbers)

    @cached_property
    def releases(self) -> ReleasesResourceWithStreamingResponse:
        return ReleasesResourceWithStreamingResponse(self._external_connections.releases)

    @cached_property
    def uploads(self) -> UploadsResourceWithStreamingResponse:
        return UploadsResourceWithStreamingResponse(self._external_connections.uploads)


class AsyncExternalConnectionsResourceWithStreamingResponse:
    def __init__(self, external_connections: AsyncExternalConnectionsResource) -> None:
        self._external_connections = external_connections

        self.create = async_to_streamed_response_wrapper(
            external_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            external_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            external_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            external_connections.delete,
        )
        self.update_location = async_to_streamed_response_wrapper(
            external_connections.update_location,
        )

    @cached_property
    def log_messages(self) -> AsyncLogMessagesResourceWithStreamingResponse:
        return AsyncLogMessagesResourceWithStreamingResponse(self._external_connections.log_messages)

    @cached_property
    def civic_addresses(self) -> AsyncCivicAddressesResourceWithStreamingResponse:
        return AsyncCivicAddressesResourceWithStreamingResponse(self._external_connections.civic_addresses)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._external_connections.phone_numbers)

    @cached_property
    def releases(self) -> AsyncReleasesResourceWithStreamingResponse:
        return AsyncReleasesResourceWithStreamingResponse(self._external_connections.releases)

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithStreamingResponse:
        return AsyncUploadsResourceWithStreamingResponse(self._external_connections.uploads)
