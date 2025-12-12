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
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.verified_number import VerifiedNumber
from ...types.verified_number_data_wrapper import VerifiedNumberDataWrapper
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
        extension: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedNumberCreateResponse:
        """Initiates phone number verification procedure.

        Supports DTMF extension dialing
        for voice calls to numbers behind IVR systems.

        Args:
          verification_method: Verification method.

          extension: Optional DTMF extension sequence to dial after the call is answered. This
              parameter enables verification of phone numbers behind IVR systems that require
              extension dialing. Valid characters: digits 0-9, letters A-D, symbols \\** and #.
              Pauses: w = 0.5 second pause, W = 1 second pause. Maximum length: 50 characters.
              Only works with 'call' verification method.

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
                    "extension": extension,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VerifiedNumber]:
        """
        Gets a paginated list of Verified Numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/verified_numbers",
            page=SyncDefaultFlatPagination[VerifiedNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    verified_number_list_params.VerifiedNumberListParams,
                ),
            ),
            model=VerifiedNumber,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        extension: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifiedNumberCreateResponse:
        """Initiates phone number verification procedure.

        Supports DTMF extension dialing
        for voice calls to numbers behind IVR systems.

        Args:
          verification_method: Verification method.

          extension: Optional DTMF extension sequence to dial after the call is answered. This
              parameter enables verification of phone numbers behind IVR systems that require
              extension dialing. Valid characters: digits 0-9, letters A-D, symbols \\** and #.
              Pauses: w = 0.5 second pause, W = 1 second pause. Maximum length: 50 characters.
              Only works with 'call' verification method.

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
                    "extension": extension,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VerifiedNumber, AsyncDefaultFlatPagination[VerifiedNumber]]:
        """
        Gets a paginated list of Verified Numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/verified_numbers",
            page=AsyncDefaultFlatPagination[VerifiedNumber],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    verified_number_list_params.VerifiedNumberListParams,
                ),
            ),
            model=VerifiedNumber,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
