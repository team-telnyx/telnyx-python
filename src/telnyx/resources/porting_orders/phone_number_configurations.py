# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.porting_orders import phone_number_configuration_list_params, phone_number_configuration_create_params
from ...types.porting_orders.phone_number_configuration_list_response import PhoneNumberConfigurationListResponse
from ...types.porting_orders.phone_number_configuration_create_response import PhoneNumberConfigurationCreateResponse

__all__ = ["PhoneNumberConfigurationsResource", "AsyncPhoneNumberConfigurationsResource"]


class PhoneNumberConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number_configurations: Iterable[phone_number_configuration_create_params.PhoneNumberConfiguration]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberConfigurationCreateResponse:
        """
        Creates a list of phone number configurations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/porting_orders/phone_number_configurations",
            body=maybe_transform(
                {"phone_number_configurations": phone_number_configurations},
                phone_number_configuration_create_params.PhoneNumberConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberConfigurationCreateResponse,
        )

    def list(
        self,
        *,
        filter: phone_number_configuration_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_configuration_list_params.Page | NotGiven = NOT_GIVEN,
        sort: phone_number_configuration_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberConfigurationListResponse:
        """
        Returns a list of phone number configurations paginated.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order.status][in][], filter[porting_phone_number][in][],
              filter[user_bundle_id][in][]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/porting_orders/phone_number_configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_configuration_list_params.PhoneNumberConfigurationListParams,
                ),
            ),
            cast_to=PhoneNumberConfigurationListResponse,
        )


class AsyncPhoneNumberConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number_configurations: Iterable[phone_number_configuration_create_params.PhoneNumberConfiguration]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberConfigurationCreateResponse:
        """
        Creates a list of phone number configurations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/porting_orders/phone_number_configurations",
            body=await async_maybe_transform(
                {"phone_number_configurations": phone_number_configurations},
                phone_number_configuration_create_params.PhoneNumberConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberConfigurationCreateResponse,
        )

    async def list(
        self,
        *,
        filter: phone_number_configuration_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_configuration_list_params.Page | NotGiven = NOT_GIVEN,
        sort: phone_number_configuration_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberConfigurationListResponse:
        """
        Returns a list of phone number configurations paginated.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[porting_order.status][in][], filter[porting_phone_number][in][],
              filter[user_bundle_id][in][]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/porting_orders/phone_number_configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_configuration_list_params.PhoneNumberConfigurationListParams,
                ),
            ),
            cast_to=PhoneNumberConfigurationListResponse,
        )


class PhoneNumberConfigurationsResourceWithRawResponse:
    def __init__(self, phone_number_configurations: PhoneNumberConfigurationsResource) -> None:
        self._phone_number_configurations = phone_number_configurations

        self.create = to_raw_response_wrapper(
            phone_number_configurations.create,
        )
        self.list = to_raw_response_wrapper(
            phone_number_configurations.list,
        )


class AsyncPhoneNumberConfigurationsResourceWithRawResponse:
    def __init__(self, phone_number_configurations: AsyncPhoneNumberConfigurationsResource) -> None:
        self._phone_number_configurations = phone_number_configurations

        self.create = async_to_raw_response_wrapper(
            phone_number_configurations.create,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number_configurations.list,
        )


class PhoneNumberConfigurationsResourceWithStreamingResponse:
    def __init__(self, phone_number_configurations: PhoneNumberConfigurationsResource) -> None:
        self._phone_number_configurations = phone_number_configurations

        self.create = to_streamed_response_wrapper(
            phone_number_configurations.create,
        )
        self.list = to_streamed_response_wrapper(
            phone_number_configurations.list,
        )


class AsyncPhoneNumberConfigurationsResourceWithStreamingResponse:
    def __init__(self, phone_number_configurations: AsyncPhoneNumberConfigurationsResource) -> None:
        self._phone_number_configurations = phone_number_configurations

        self.create = async_to_streamed_response_wrapper(
            phone_number_configurations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number_configurations.list,
        )
