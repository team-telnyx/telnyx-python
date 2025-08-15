# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import user_address_list_params, user_address_create_params
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
from ..types.user_address_list_response import UserAddressListResponse
from ..types.user_address_create_response import UserAddressCreateResponse
from ..types.user_address_retrieve_response import UserAddressRetrieveResponse

__all__ = ["UserAddressesResource", "AsyncUserAddressesResource"]


class UserAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UserAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UserAddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_name: str,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        street_address: str,
        administrative_area: str | NotGiven = NOT_GIVEN,
        borough: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        neighborhood: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        skip_address_verification: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddressCreateResponse:
        """
        Creates a user address.

        Args:
          business_name: The business name associated with the user address.

          country_code: The two-character (ISO 3166-1 alpha-2) country code of the user address.

          first_name: The first name associated with the user address.

          last_name: The last name associated with the user address.

          locality: The locality of the user address. For US addresses, this corresponds to the city
              of the address.

          street_address: The primary street address information about the user address.

          administrative_area: The locality of the user address. For US addresses, this corresponds to the
              state of the address.

          borough: The borough of the user address. This field is not used for addresses in the US
              but is used for some international addresses.

          customer_reference: A customer reference string for customer look ups.

          extended_address: Additional street address information about the user address such as, but not
              limited to, unit number or apartment number.

          neighborhood: The neighborhood of the user address. This field is not used for addresses in
              the US but is used for some international addresses.

          phone_number: The phone number associated with the user address.

          postal_code: The postal code of the user address.

          skip_address_verification: An optional boolean value specifying if verification of the address should be
              skipped or not. UserAddresses are generally used for shipping addresses, and
              failure to validate your shipping address will likely result in a failure to
              deliver SIM cards or other items ordered from Telnyx. Do not use this parameter
              unless you are sure that the address is correct even though it cannot be
              validated. If this is set to any value other than true, verification of the
              address will be attempted, and the user address will not be allowed if
              verification fails. If verification fails but suggested values are available
              that might make the address correct, they will be present in the response as
              well. If this value is set to true, then the verification will not be attempted.
              Defaults to false (verification will be performed).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user_addresses",
            body=maybe_transform(
                {
                    "business_name": business_name,
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "street_address": street_address,
                    "administrative_area": administrative_area,
                    "borough": borough,
                    "customer_reference": customer_reference,
                    "extended_address": extended_address,
                    "neighborhood": neighborhood,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "skip_address_verification": skip_address_verification,
                },
                user_address_create_params.UserAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddressCreateResponse,
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
    ) -> UserAddressRetrieveResponse:
        """
        Retrieves the details of an existing user address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/user_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddressRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: user_address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: user_address_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "first_name", "last_name", "business_name", "street_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddressListResponse:
        """
        Returns a list of your user addresses.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference][eq], filter[customer_reference][contains],
              filter[street_address][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>street_address</code>: sorts the result by the
                  <code>street_address</code> field in ascending order.
                </li>

                <li>
                  <code>-street_address</code>: sorts the result by the
                  <code>street_address</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user_addresses",
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
                    user_address_list_params.UserAddressListParams,
                ),
            ),
            cast_to=UserAddressListResponse,
        )


class AsyncUserAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUserAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_name: str,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        street_address: str,
        administrative_area: str | NotGiven = NOT_GIVEN,
        borough: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        neighborhood: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        skip_address_verification: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddressCreateResponse:
        """
        Creates a user address.

        Args:
          business_name: The business name associated with the user address.

          country_code: The two-character (ISO 3166-1 alpha-2) country code of the user address.

          first_name: The first name associated with the user address.

          last_name: The last name associated with the user address.

          locality: The locality of the user address. For US addresses, this corresponds to the city
              of the address.

          street_address: The primary street address information about the user address.

          administrative_area: The locality of the user address. For US addresses, this corresponds to the
              state of the address.

          borough: The borough of the user address. This field is not used for addresses in the US
              but is used for some international addresses.

          customer_reference: A customer reference string for customer look ups.

          extended_address: Additional street address information about the user address such as, but not
              limited to, unit number or apartment number.

          neighborhood: The neighborhood of the user address. This field is not used for addresses in
              the US but is used for some international addresses.

          phone_number: The phone number associated with the user address.

          postal_code: The postal code of the user address.

          skip_address_verification: An optional boolean value specifying if verification of the address should be
              skipped or not. UserAddresses are generally used for shipping addresses, and
              failure to validate your shipping address will likely result in a failure to
              deliver SIM cards or other items ordered from Telnyx. Do not use this parameter
              unless you are sure that the address is correct even though it cannot be
              validated. If this is set to any value other than true, verification of the
              address will be attempted, and the user address will not be allowed if
              verification fails. If verification fails but suggested values are available
              that might make the address correct, they will be present in the response as
              well. If this value is set to true, then the verification will not be attempted.
              Defaults to false (verification will be performed).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user_addresses",
            body=await async_maybe_transform(
                {
                    "business_name": business_name,
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "street_address": street_address,
                    "administrative_area": administrative_area,
                    "borough": borough,
                    "customer_reference": customer_reference,
                    "extended_address": extended_address,
                    "neighborhood": neighborhood,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "skip_address_verification": skip_address_verification,
                },
                user_address_create_params.UserAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddressCreateResponse,
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
    ) -> UserAddressRetrieveResponse:
        """
        Retrieves the details of an existing user address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/user_addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddressRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: user_address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: user_address_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "first_name", "last_name", "business_name", "street_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddressListResponse:
        """
        Returns a list of your user addresses.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference][eq], filter[customer_reference][contains],
              filter[street_address][contains]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>street_address</code>: sorts the result by the
                  <code>street_address</code> field in ascending order.
                </li>

                <li>
                  <code>-street_address</code>: sorts the result by the
                  <code>street_address</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user_addresses",
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
                    user_address_list_params.UserAddressListParams,
                ),
            ),
            cast_to=UserAddressListResponse,
        )


class UserAddressesResourceWithRawResponse:
    def __init__(self, user_addresses: UserAddressesResource) -> None:
        self._user_addresses = user_addresses

        self.create = to_raw_response_wrapper(
            user_addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            user_addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            user_addresses.list,
        )


class AsyncUserAddressesResourceWithRawResponse:
    def __init__(self, user_addresses: AsyncUserAddressesResource) -> None:
        self._user_addresses = user_addresses

        self.create = async_to_raw_response_wrapper(
            user_addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            user_addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            user_addresses.list,
        )


class UserAddressesResourceWithStreamingResponse:
    def __init__(self, user_addresses: UserAddressesResource) -> None:
        self._user_addresses = user_addresses

        self.create = to_streamed_response_wrapper(
            user_addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            user_addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            user_addresses.list,
        )


class AsyncUserAddressesResourceWithStreamingResponse:
    def __init__(self, user_addresses: AsyncUserAddressesResource) -> None:
        self._user_addresses = user_addresses

        self.create = async_to_streamed_response_wrapper(
            user_addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            user_addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            user_addresses.list,
        )
