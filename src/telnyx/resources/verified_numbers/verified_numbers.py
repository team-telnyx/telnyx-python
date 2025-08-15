# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import verified_number_list_params, verified_number_create_params
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
from ...types.verified_number_data_wrapper import VerifiedNumberDataWrapper
from ...types.verified_number_list_response import VerifiedNumberListResponse
from ...types.verified_number_create_response import VerifiedNumberCreateResponse

__all__ = ["VerifiedNumbersResource", "AsyncVerifiedNumbersResource"]


class VerifiedNumbersResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VerifiedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VerifiedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifiedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VerifiedNumbersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number: str,
        verification_method: Literal["sms", "call"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberCreateResponse:
        """
        Initiates phone number verification procedure.

        Args:
          verification_method: Verification method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verified_numbers",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "verification_method": verification_method,
                },
                verified_number_create_params.VerifiedNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberCreateResponse,
        )

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberDataWrapper:
        """
        Retrieve a verified number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/verified_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberDataWrapper,
        )

    def list(
        self,
        *,
        page: verified_number_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberListResponse:
        """
        Gets a paginated list of Verified Numbers.

        Args:
          page: Consolidated page parameter (deepObject style). Use page[size] and page[number]
              in the query string. Originally: page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/verified_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, verified_number_list_params.VerifiedNumberListParams),
            ),
            cast_to=VerifiedNumberListResponse,
        )

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberDataWrapper:
        """
        Delete a verified number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._delete(
            f"/verified_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberDataWrapper,
        )


class AsyncVerifiedNumbersResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVerifiedNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifiedNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifiedNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVerifiedNumbersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number: str,
        verification_method: Literal["sms", "call"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberCreateResponse:
        """
        Initiates phone number verification procedure.

        Args:
          verification_method: Verification method.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verified_numbers",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "verification_method": verification_method,
                },
                verified_number_create_params.VerifiedNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberCreateResponse,
        )

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberDataWrapper:
        """
        Retrieve a verified number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/verified_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberDataWrapper,
        )

    async def list(
        self,
        *,
        page: verified_number_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberListResponse:
        """
        Gets a paginated list of Verified Numbers.

        Args:
          page: Consolidated page parameter (deepObject style). Use page[size] and page[number]
              in the query string. Originally: page[size], page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/verified_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, verified_number_list_params.VerifiedNumberListParams),
            ),
            cast_to=VerifiedNumberListResponse,
        )

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerifiedNumberDataWrapper:
        """
        Delete a verified number

        Args:
          phone_number: +E164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._delete(
            f"/verified_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifiedNumberDataWrapper,
        )


class VerifiedNumbersResourceWithRawResponse:
    def __init__(self, verified_numbers: VerifiedNumbersResource) -> None:
        self._verified_numbers = verified_numbers

        self.create = to_raw_response_wrapper(
            verified_numbers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verified_numbers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            verified_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            verified_numbers.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._verified_numbers.actions)


class AsyncVerifiedNumbersResourceWithRawResponse:
    def __init__(self, verified_numbers: AsyncVerifiedNumbersResource) -> None:
        self._verified_numbers = verified_numbers

        self.create = async_to_raw_response_wrapper(
            verified_numbers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verified_numbers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            verified_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            verified_numbers.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._verified_numbers.actions)


class VerifiedNumbersResourceWithStreamingResponse:
    def __init__(self, verified_numbers: VerifiedNumbersResource) -> None:
        self._verified_numbers = verified_numbers

        self.create = to_streamed_response_wrapper(
            verified_numbers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verified_numbers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            verified_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            verified_numbers.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._verified_numbers.actions)


class AsyncVerifiedNumbersResourceWithStreamingResponse:
    def __init__(self, verified_numbers: AsyncVerifiedNumbersResource) -> None:
        self._verified_numbers = verified_numbers

        self.create = async_to_streamed_response_wrapper(
            verified_numbers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verified_numbers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            verified_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            verified_numbers.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._verified_numbers.actions)
