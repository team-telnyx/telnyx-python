# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import alphanumeric_sender_id_list_params, alphanumeric_sender_id_create_params
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
from ..types.alphanumeric_sender_id_list_response import AlphanumericSenderIDListResponse
from ..types.alphanumeric_sender_id_create_response import AlphanumericSenderIDCreateResponse
from ..types.alphanumeric_sender_id_delete_response import AlphanumericSenderIDDeleteResponse
from ..types.alphanumeric_sender_id_retrieve_response import AlphanumericSenderIDRetrieveResponse

__all__ = ["AlphanumericSenderIDsResource", "AsyncAlphanumericSenderIDsResource"]


class AlphanumericSenderIDsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlphanumericSenderIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AlphanumericSenderIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlphanumericSenderIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AlphanumericSenderIDsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        alphanumeric_sender_id: str,
        messaging_profile_id: str,
        us_long_code_fallback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlphanumericSenderIDCreateResponse:
        """
        Create a new alphanumeric sender ID associated with a messaging profile.

        Args:
          alphanumeric_sender_id: The alphanumeric sender ID string.

          messaging_profile_id: The messaging profile to associate the sender ID with.

          us_long_code_fallback: A US long code number to use as fallback when sending to US destinations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/alphanumeric_sender_ids",
            body=maybe_transform(
                {
                    "alphanumeric_sender_id": alphanumeric_sender_id,
                    "messaging_profile_id": messaging_profile_id,
                    "us_long_code_fallback": us_long_code_fallback,
                },
                alphanumeric_sender_id_create_params.AlphanumericSenderIDCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDCreateResponse,
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
    ) -> AlphanumericSenderIDRetrieveResponse:
        """
        Retrieve a specific alphanumeric sender ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/alphanumeric_sender_ids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_messaging_profile_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[AlphanumericSenderIDListResponse]:
        """
        List all alphanumeric sender IDs for the authenticated user.

        Args:
          filter_messaging_profile_id: Filter by messaging profile ID.

          page_number: Page number.

          page_size: Page size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/alphanumeric_sender_ids",
            page=SyncDefaultFlatPagination[AlphanumericSenderIDListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_messaging_profile_id": filter_messaging_profile_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    alphanumeric_sender_id_list_params.AlphanumericSenderIDListParams,
                ),
            ),
            model=AlphanumericSenderIDListResponse,
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
    ) -> AlphanumericSenderIDDeleteResponse:
        """
        Delete an alphanumeric sender ID and disassociate it from its messaging profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/alphanumeric_sender_ids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDDeleteResponse,
        )


class AsyncAlphanumericSenderIDsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlphanumericSenderIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlphanumericSenderIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlphanumericSenderIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAlphanumericSenderIDsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        alphanumeric_sender_id: str,
        messaging_profile_id: str,
        us_long_code_fallback: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlphanumericSenderIDCreateResponse:
        """
        Create a new alphanumeric sender ID associated with a messaging profile.

        Args:
          alphanumeric_sender_id: The alphanumeric sender ID string.

          messaging_profile_id: The messaging profile to associate the sender ID with.

          us_long_code_fallback: A US long code number to use as fallback when sending to US destinations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/alphanumeric_sender_ids",
            body=await async_maybe_transform(
                {
                    "alphanumeric_sender_id": alphanumeric_sender_id,
                    "messaging_profile_id": messaging_profile_id,
                    "us_long_code_fallback": us_long_code_fallback,
                },
                alphanumeric_sender_id_create_params.AlphanumericSenderIDCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDCreateResponse,
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
    ) -> AlphanumericSenderIDRetrieveResponse:
        """
        Retrieve a specific alphanumeric sender ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/alphanumeric_sender_ids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_messaging_profile_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AlphanumericSenderIDListResponse, AsyncDefaultFlatPagination[AlphanumericSenderIDListResponse]]:
        """
        List all alphanumeric sender IDs for the authenticated user.

        Args:
          filter_messaging_profile_id: Filter by messaging profile ID.

          page_number: Page number.

          page_size: Page size.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/alphanumeric_sender_ids",
            page=AsyncDefaultFlatPagination[AlphanumericSenderIDListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_messaging_profile_id": filter_messaging_profile_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    alphanumeric_sender_id_list_params.AlphanumericSenderIDListParams,
                ),
            ),
            model=AlphanumericSenderIDListResponse,
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
    ) -> AlphanumericSenderIDDeleteResponse:
        """
        Delete an alphanumeric sender ID and disassociate it from its messaging profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/alphanumeric_sender_ids/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlphanumericSenderIDDeleteResponse,
        )


class AlphanumericSenderIDsResourceWithRawResponse:
    def __init__(self, alphanumeric_sender_ids: AlphanumericSenderIDsResource) -> None:
        self._alphanumeric_sender_ids = alphanumeric_sender_ids

        self.create = to_raw_response_wrapper(
            alphanumeric_sender_ids.create,
        )
        self.retrieve = to_raw_response_wrapper(
            alphanumeric_sender_ids.retrieve,
        )
        self.list = to_raw_response_wrapper(
            alphanumeric_sender_ids.list,
        )
        self.delete = to_raw_response_wrapper(
            alphanumeric_sender_ids.delete,
        )


class AsyncAlphanumericSenderIDsResourceWithRawResponse:
    def __init__(self, alphanumeric_sender_ids: AsyncAlphanumericSenderIDsResource) -> None:
        self._alphanumeric_sender_ids = alphanumeric_sender_ids

        self.create = async_to_raw_response_wrapper(
            alphanumeric_sender_ids.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            alphanumeric_sender_ids.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            alphanumeric_sender_ids.list,
        )
        self.delete = async_to_raw_response_wrapper(
            alphanumeric_sender_ids.delete,
        )


class AlphanumericSenderIDsResourceWithStreamingResponse:
    def __init__(self, alphanumeric_sender_ids: AlphanumericSenderIDsResource) -> None:
        self._alphanumeric_sender_ids = alphanumeric_sender_ids

        self.create = to_streamed_response_wrapper(
            alphanumeric_sender_ids.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            alphanumeric_sender_ids.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            alphanumeric_sender_ids.list,
        )
        self.delete = to_streamed_response_wrapper(
            alphanumeric_sender_ids.delete,
        )


class AsyncAlphanumericSenderIDsResourceWithStreamingResponse:
    def __init__(self, alphanumeric_sender_ids: AsyncAlphanumericSenderIDsResource) -> None:
        self._alphanumeric_sender_ids = alphanumeric_sender_ids

        self.create = async_to_streamed_response_wrapper(
            alphanumeric_sender_ids.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            alphanumeric_sender_ids.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            alphanumeric_sender_ids.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            alphanumeric_sender_ids.delete,
        )
