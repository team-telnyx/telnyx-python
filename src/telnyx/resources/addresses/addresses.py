# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import address_list_params, address_create_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
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
from ...types.address_list_response import AddressListResponse
from ...types.address_create_response import AddressCreateResponse
from ...types.address_delete_response import AddressDeleteResponse
from ...types.address_retrieve_response import AddressRetrieveResponse

__all__ = ["AddressesResource", "AsyncAddressesResource"]


class AddressesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        business_name: str,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        street_address: str,
        address_book: bool | NotGiven = NOT_GIVEN,
        administrative_area: str | NotGiven = NOT_GIVEN,
        borough: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        neighborhood: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        validate_address: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        Creates an address.

        Args:
          business_name: The business name associated with the address. An address must have either a
              first last name or a business name.

          country_code: The two-character (ISO 3166-1 alpha-2) country code of the address.

          first_name: The first name associated with the address. An address must have either a first
              last name or a business name.

          last_name: The last name associated with the address. An address must have either a first
              last name or a business name.

          locality: The locality of the address. For US addresses, this corresponds to the city of
              the address.

          street_address: The primary street address information about the address.

          address_book: Indicates whether or not the address should be considered part of your list of
              addresses that appear for regular use.

          administrative_area: The locality of the address. For US addresses, this corresponds to the state of
              the address.

          borough: The borough of the address. This field is not used for addresses in the US but
              is used for some international addresses.

          customer_reference: A customer reference string for customer look ups.

          extended_address: Additional street address information about the address such as, but not limited
              to, unit number or apartment number.

          neighborhood: The neighborhood of the address. This field is not used for addresses in the US
              but is used for some international addresses.

          phone_number: The phone number associated with the address.

          postal_code: The postal code of the address.

          validate_address: Indicates whether or not the address should be validated for emergency use upon
              creation or not. This should be left with the default value of `true` unless you
              have used the `/addresses/actions/validate` endpoint to validate the address
              separately prior to creation. If an address is not validated for emergency use
              upon creation and it is not valid, it will not be able to be used for emergency
              services.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/addresses",
            body=maybe_transform(
                {
                    "business_name": business_name,
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "street_address": street_address,
                    "address_book": address_book,
                    "administrative_area": administrative_area,
                    "borough": borough,
                    "customer_reference": customer_reference,
                    "extended_address": extended_address,
                    "neighborhood": neighborhood,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "validate_address": validate_address,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
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
    ) -> AddressRetrieveResponse:
        """
        Retrieves the details of an existing address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: address_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "first_name", "last_name", "business_name", "street_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns a list of your addresses.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference][eq], filter[customer_reference][contains],
              filter[used_as_emergency], filter[street_address][contains],
              filter[address_book][eq]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

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
            "/addresses",
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
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
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
    ) -> AddressDeleteResponse:
        """
        Deletes an existing address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
        )


class AsyncAddressesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        business_name: str,
        country_code: str,
        first_name: str,
        last_name: str,
        locality: str,
        street_address: str,
        address_book: bool | NotGiven = NOT_GIVEN,
        administrative_area: str | NotGiven = NOT_GIVEN,
        borough: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        extended_address: str | NotGiven = NOT_GIVEN,
        neighborhood: str | NotGiven = NOT_GIVEN,
        phone_number: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        validate_address: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressCreateResponse:
        """
        Creates an address.

        Args:
          business_name: The business name associated with the address. An address must have either a
              first last name or a business name.

          country_code: The two-character (ISO 3166-1 alpha-2) country code of the address.

          first_name: The first name associated with the address. An address must have either a first
              last name or a business name.

          last_name: The last name associated with the address. An address must have either a first
              last name or a business name.

          locality: The locality of the address. For US addresses, this corresponds to the city of
              the address.

          street_address: The primary street address information about the address.

          address_book: Indicates whether or not the address should be considered part of your list of
              addresses that appear for regular use.

          administrative_area: The locality of the address. For US addresses, this corresponds to the state of
              the address.

          borough: The borough of the address. This field is not used for addresses in the US but
              is used for some international addresses.

          customer_reference: A customer reference string for customer look ups.

          extended_address: Additional street address information about the address such as, but not limited
              to, unit number or apartment number.

          neighborhood: The neighborhood of the address. This field is not used for addresses in the US
              but is used for some international addresses.

          phone_number: The phone number associated with the address.

          postal_code: The postal code of the address.

          validate_address: Indicates whether or not the address should be validated for emergency use upon
              creation or not. This should be left with the default value of `true` unless you
              have used the `/addresses/actions/validate` endpoint to validate the address
              separately prior to creation. If an address is not validated for emergency use
              upon creation and it is not valid, it will not be able to be used for emergency
              services.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/addresses",
            body=await async_maybe_transform(
                {
                    "business_name": business_name,
                    "country_code": country_code,
                    "first_name": first_name,
                    "last_name": last_name,
                    "locality": locality,
                    "street_address": street_address,
                    "address_book": address_book,
                    "administrative_area": administrative_area,
                    "borough": borough,
                    "customer_reference": customer_reference,
                    "extended_address": extended_address,
                    "neighborhood": neighborhood,
                    "phone_number": phone_number,
                    "postal_code": postal_code,
                    "validate_address": validate_address,
                },
                address_create_params.AddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressCreateResponse,
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
    ) -> AddressRetrieveResponse:
        """
        Retrieves the details of an existing address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: address_list_params.Filter | NotGiven = NOT_GIVEN,
        page: address_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["created_at", "first_name", "last_name", "business_name", "street_address"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddressListResponse:
        """
        Returns a list of your addresses.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference][eq], filter[customer_reference][contains],
              filter[used_as_emergency], filter[street_address][contains],
              filter[address_book][eq]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

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
            "/addresses",
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
                    address_list_params.AddressListParams,
                ),
            ),
            cast_to=AddressListResponse,
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
    ) -> AddressDeleteResponse:
        """
        Deletes an existing address.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddressDeleteResponse,
        )


class AddressesResourceWithRawResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            addresses.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._addresses.actions)


class AsyncAddressesResourceWithRawResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_raw_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            addresses.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._addresses.actions)


class AddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AddressesResource) -> None:
        self._addresses = addresses

        self.create = to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            addresses.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._addresses.actions)


class AsyncAddressesResourceWithStreamingResponse:
    def __init__(self, addresses: AsyncAddressesResource) -> None:
        self._addresses = addresses

        self.create = async_to_streamed_response_wrapper(
            addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            addresses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            addresses.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._addresses.actions)
