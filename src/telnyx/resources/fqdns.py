# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import fqdn_list_params, fqdn_create_params, fqdn_update_params
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
from ..types.fqdn_list_response import FqdnListResponse
from ..types.fqdn_create_response import FqdnCreateResponse
from ..types.fqdn_delete_response import FqdnDeleteResponse
from ..types.fqdn_update_response import FqdnUpdateResponse
from ..types.fqdn_retrieve_response import FqdnRetrieveResponse

__all__ = ["FqdnsResource", "AsyncFqdnsResource"]


class FqdnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FqdnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FqdnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FqdnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FqdnsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        dns_record_type: str,
        fqdn: str,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnCreateResponse:
        """
        Create a new FQDN object.

        Args:
          connection_id: ID of the FQDN connection to which this IP should be attached.

          dns_record_type: The DNS record type for the FQDN. For cases where a port is not set, the DNS
              record type must be 'srv'. For cases where a port is set, the DNS record type
              must be 'a'. If the DNS record type is 'a' and a port is not specified, 5060
              will be used.

          fqdn: FQDN represented by this resource.

          port: Port to use when connecting to this FQDN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fqdns",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "dns_record_type": dns_record_type,
                    "fqdn": fqdn,
                    "port": port,
                },
                fqdn_create_params.FqdnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnCreateResponse,
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
    ) -> FqdnRetrieveResponse:
        """
        Return the details regarding a specific FQDN.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/fqdns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        connection_id: str | NotGiven = NOT_GIVEN,
        dns_record_type: str | NotGiven = NOT_GIVEN,
        fqdn: str | NotGiven = NOT_GIVEN,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnUpdateResponse:
        """
        Update the details of a specific FQDN.

        Args:
          connection_id: ID of the FQDN connection to which this IP should be attached.

          dns_record_type: The DNS record type for the FQDN. For cases where a port is not set, the DNS
              record type must be 'srv'. For cases where a port is set, the DNS record type
              must be 'a'. If the DNS record type is 'a' and a port is not specified, 5060
              will be used.

          fqdn: FQDN represented by this resource.

          port: Port to use when connecting to this FQDN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fqdns/{id}",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "dns_record_type": dns_record_type,
                    "fqdn": fqdn,
                    "port": port,
                },
                fqdn_update_params.FqdnUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnUpdateResponse,
        )

    def list(
        self,
        *,
        filter: fqdn_list_params.Filter | NotGiven = NOT_GIVEN,
        page: fqdn_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnListResponse:
        """
        Get all FQDNs belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_id], filter[fqdn], filter[port], filter[dns_record_type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fqdns",
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
                    fqdn_list_params.FqdnListParams,
                ),
            ),
            cast_to=FqdnListResponse,
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
    ) -> FqdnDeleteResponse:
        """
        Delete an FQDN.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/fqdns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnDeleteResponse,
        )


class AsyncFqdnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFqdnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFqdnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFqdnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFqdnsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        dns_record_type: str,
        fqdn: str,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnCreateResponse:
        """
        Create a new FQDN object.

        Args:
          connection_id: ID of the FQDN connection to which this IP should be attached.

          dns_record_type: The DNS record type for the FQDN. For cases where a port is not set, the DNS
              record type must be 'srv'. For cases where a port is set, the DNS record type
              must be 'a'. If the DNS record type is 'a' and a port is not specified, 5060
              will be used.

          fqdn: FQDN represented by this resource.

          port: Port to use when connecting to this FQDN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fqdns",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "dns_record_type": dns_record_type,
                    "fqdn": fqdn,
                    "port": port,
                },
                fqdn_create_params.FqdnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnCreateResponse,
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
    ) -> FqdnRetrieveResponse:
        """
        Return the details regarding a specific FQDN.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/fqdns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        connection_id: str | NotGiven = NOT_GIVEN,
        dns_record_type: str | NotGiven = NOT_GIVEN,
        fqdn: str | NotGiven = NOT_GIVEN,
        port: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnUpdateResponse:
        """
        Update the details of a specific FQDN.

        Args:
          connection_id: ID of the FQDN connection to which this IP should be attached.

          dns_record_type: The DNS record type for the FQDN. For cases where a port is not set, the DNS
              record type must be 'srv'. For cases where a port is set, the DNS record type
              must be 'a'. If the DNS record type is 'a' and a port is not specified, 5060
              will be used.

          fqdn: FQDN represented by this resource.

          port: Port to use when connecting to this FQDN.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fqdns/{id}",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "dns_record_type": dns_record_type,
                    "fqdn": fqdn,
                    "port": port,
                },
                fqdn_update_params.FqdnUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: fqdn_list_params.Filter | NotGiven = NOT_GIVEN,
        page: fqdn_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FqdnListResponse:
        """
        Get all FQDNs belonging to the user that match the given filters.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[connection_id], filter[fqdn], filter[port], filter[dns_record_type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fqdns",
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
                    fqdn_list_params.FqdnListParams,
                ),
            ),
            cast_to=FqdnListResponse,
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
    ) -> FqdnDeleteResponse:
        """
        Delete an FQDN.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/fqdns/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FqdnDeleteResponse,
        )


class FqdnsResourceWithRawResponse:
    def __init__(self, fqdns: FqdnsResource) -> None:
        self._fqdns = fqdns

        self.create = to_raw_response_wrapper(
            fqdns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fqdns.retrieve,
        )
        self.update = to_raw_response_wrapper(
            fqdns.update,
        )
        self.list = to_raw_response_wrapper(
            fqdns.list,
        )
        self.delete = to_raw_response_wrapper(
            fqdns.delete,
        )


class AsyncFqdnsResourceWithRawResponse:
    def __init__(self, fqdns: AsyncFqdnsResource) -> None:
        self._fqdns = fqdns

        self.create = async_to_raw_response_wrapper(
            fqdns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fqdns.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            fqdns.update,
        )
        self.list = async_to_raw_response_wrapper(
            fqdns.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fqdns.delete,
        )


class FqdnsResourceWithStreamingResponse:
    def __init__(self, fqdns: FqdnsResource) -> None:
        self._fqdns = fqdns

        self.create = to_streamed_response_wrapper(
            fqdns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fqdns.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            fqdns.update,
        )
        self.list = to_streamed_response_wrapper(
            fqdns.list,
        )
        self.delete = to_streamed_response_wrapper(
            fqdns.delete,
        )


class AsyncFqdnsResourceWithStreamingResponse:
    def __init__(self, fqdns: AsyncFqdnsResource) -> None:
        self._fqdns = fqdns

        self.create = async_to_streamed_response_wrapper(
            fqdns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fqdns.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            fqdns.update,
        )
        self.list = async_to_streamed_response_wrapper(
            fqdns.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fqdns.delete,
        )
