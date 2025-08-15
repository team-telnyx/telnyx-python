# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import webhook_delivery_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.webhook_delivery_list_response import WebhookDeliveryListResponse
from ..types.webhook_delivery_retrieve_response import WebhookDeliveryRetrieveResponse

__all__ = ["WebhookDeliveriesResource", "AsyncWebhookDeliveriesResource"]


class WebhookDeliveriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WebhookDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WebhookDeliveriesResourceWithStreamingResponse(self)

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
    ) -> WebhookDeliveryRetrieveResponse:
        """
        Provides webhook_delivery debug data, such as timestamps, delivery status and
        attempts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/webhook_deliveries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeliveryRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: webhook_delivery_list_params.Filter | NotGiven = NOT_GIVEN,
        page: webhook_delivery_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeliveryListResponse:
        """
        Lists webhook_deliveries for the authenticated user

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[status][eq], filter[event_type], filter[webhook][contains],
              filter[attempts][contains], filter[started_at][gte], filter[started_at][lte],
              filter[finished_at][gte], filter[finished_at][lte]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/webhook_deliveries",
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
                    webhook_delivery_list_params.WebhookDeliveryListParams,
                ),
            ),
            cast_to=WebhookDeliveryListResponse,
        )


class AsyncWebhookDeliveriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWebhookDeliveriesResourceWithStreamingResponse(self)

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
    ) -> WebhookDeliveryRetrieveResponse:
        """
        Provides webhook_delivery debug data, such as timestamps, delivery status and
        attempts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/webhook_deliveries/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookDeliveryRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: webhook_delivery_list_params.Filter | NotGiven = NOT_GIVEN,
        page: webhook_delivery_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebhookDeliveryListResponse:
        """
        Lists webhook_deliveries for the authenticated user

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[status][eq], filter[event_type], filter[webhook][contains],
              filter[attempts][contains], filter[started_at][gte], filter[started_at][lte],
              filter[finished_at][gte], filter[finished_at][lte]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/webhook_deliveries",
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
                    webhook_delivery_list_params.WebhookDeliveryListParams,
                ),
            ),
            cast_to=WebhookDeliveryListResponse,
        )


class WebhookDeliveriesResourceWithRawResponse:
    def __init__(self, webhook_deliveries: WebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.retrieve = to_raw_response_wrapper(
            webhook_deliveries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            webhook_deliveries.list,
        )


class AsyncWebhookDeliveriesResourceWithRawResponse:
    def __init__(self, webhook_deliveries: AsyncWebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.retrieve = async_to_raw_response_wrapper(
            webhook_deliveries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_deliveries.list,
        )


class WebhookDeliveriesResourceWithStreamingResponse:
    def __init__(self, webhook_deliveries: WebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.retrieve = to_streamed_response_wrapper(
            webhook_deliveries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            webhook_deliveries.list,
        )


class AsyncWebhookDeliveriesResourceWithStreamingResponse:
    def __init__(self, webhook_deliveries: AsyncWebhookDeliveriesResource) -> None:
        self._webhook_deliveries = webhook_deliveries

        self.retrieve = async_to_streamed_response_wrapper(
            webhook_deliveries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_deliveries.list,
        )
