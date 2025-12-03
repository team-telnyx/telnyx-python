# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import access_ip_address_list_params, access_ip_address_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.access_ip_address_response import AccessIPAddressResponse

__all__ = ["AccessIPAddressResource", "AsyncAccessIPAddressResource"]


class AccessIPAddressResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessIPAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AccessIPAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessIPAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AccessIPAddressResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        ip_address: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Create new Access IP Address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/access_ip_address",
            body=maybe_transform(
                {
                    "ip_address": ip_address,
                    "description": description,
                },
                access_ip_address_create_params.AccessIPAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )

    def retrieve(
        self,
        access_ip_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Retrieve an access IP address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_address_id:
            raise ValueError(
                f"Expected a non-empty value for `access_ip_address_id` but received {access_ip_address_id!r}"
            )
        return self._get(
            f"/access_ip_address/{access_ip_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )

    def list(
        self,
        *,
        filter: access_ip_address_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[AccessIPAddressResponse]:
        """
        List all Access IP Addresses

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[ip_source],
              filter[ip_address], filter[created_at]. Supports complex bracket operations for
              dynamic filtering.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/access_ip_address",
            page=SyncDefaultFlatPagination[AccessIPAddressResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    access_ip_address_list_params.AccessIPAddressListParams,
                ),
            ),
            model=AccessIPAddressResponse,
        )

    def delete(
        self,
        access_ip_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Delete access IP address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_address_id:
            raise ValueError(
                f"Expected a non-empty value for `access_ip_address_id` but received {access_ip_address_id!r}"
            )
        return self._delete(
            f"/access_ip_address/{access_ip_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )


class AsyncAccessIPAddressResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessIPAddressResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessIPAddressResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessIPAddressResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAccessIPAddressResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        ip_address: str,
        description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Create new Access IP Address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/access_ip_address",
            body=await async_maybe_transform(
                {
                    "ip_address": ip_address,
                    "description": description,
                },
                access_ip_address_create_params.AccessIPAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )

    async def retrieve(
        self,
        access_ip_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Retrieve an access IP address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_address_id:
            raise ValueError(
                f"Expected a non-empty value for `access_ip_address_id` but received {access_ip_address_id!r}"
            )
        return await self._get(
            f"/access_ip_address/{access_ip_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )

    def list(
        self,
        *,
        filter: access_ip_address_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AccessIPAddressResponse, AsyncDefaultFlatPagination[AccessIPAddressResponse]]:
        """
        List all Access IP Addresses

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[ip_source],
              filter[ip_address], filter[created_at]. Supports complex bracket operations for
              dynamic filtering.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/access_ip_address",
            page=AsyncDefaultFlatPagination[AccessIPAddressResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    access_ip_address_list_params.AccessIPAddressListParams,
                ),
            ),
            model=AccessIPAddressResponse,
        )

    async def delete(
        self,
        access_ip_address_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccessIPAddressResponse:
        """
        Delete access IP address

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not access_ip_address_id:
            raise ValueError(
                f"Expected a non-empty value for `access_ip_address_id` but received {access_ip_address_id!r}"
            )
        return await self._delete(
            f"/access_ip_address/{access_ip_address_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccessIPAddressResponse,
        )


class AccessIPAddressResourceWithRawResponse:
    def __init__(self, access_ip_address: AccessIPAddressResource) -> None:
        self._access_ip_address = access_ip_address

        self.create = to_raw_response_wrapper(
            access_ip_address.create,
        )
        self.retrieve = to_raw_response_wrapper(
            access_ip_address.retrieve,
        )
        self.list = to_raw_response_wrapper(
            access_ip_address.list,
        )
        self.delete = to_raw_response_wrapper(
            access_ip_address.delete,
        )


class AsyncAccessIPAddressResourceWithRawResponse:
    def __init__(self, access_ip_address: AsyncAccessIPAddressResource) -> None:
        self._access_ip_address = access_ip_address

        self.create = async_to_raw_response_wrapper(
            access_ip_address.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            access_ip_address.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            access_ip_address.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_ip_address.delete,
        )


class AccessIPAddressResourceWithStreamingResponse:
    def __init__(self, access_ip_address: AccessIPAddressResource) -> None:
        self._access_ip_address = access_ip_address

        self.create = to_streamed_response_wrapper(
            access_ip_address.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            access_ip_address.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            access_ip_address.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_ip_address.delete,
        )


class AsyncAccessIPAddressResourceWithStreamingResponse:
    def __init__(self, access_ip_address: AsyncAccessIPAddressResource) -> None:
        self._access_ip_address = access_ip_address

        self.create = async_to_streamed_response_wrapper(
            access_ip_address.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            access_ip_address.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            access_ip_address.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_ip_address.delete,
        )
