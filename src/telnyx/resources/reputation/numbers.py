# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.reputation import number_list_params, number_retrieve_params
from ...types.reputation.number_retrieve_response import NumberRetrieveResponse
from ...types.shared.reputation_phone_number_with_reputation_data import ReputationPhoneNumberWithReputationData

__all__ = ["NumbersResource", "AsyncNumbersResource"]


class NumbersResource(SyncAPIResource):
    """
    Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
    """

    @cached_property
    def with_raw_response(self) -> NumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumbersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Get reputation data for a specific phone number without requiring an
        `enterprise_id`.

        Same response as the enterprise-scoped endpoint. Uses cached data by default.

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false, returns
              cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/reputation/numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"fresh": fresh}, number_retrieve_params.NumberRetrieveParams),
            ),
            cast_to=NumberRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData]:
        """List all phone numbers enrolled in Number Reputation monitoring for your
        account.

        This is a simplified endpoint that does not require an `enterprise_id`
        — it returns numbers across all your enterprises.

        Supports pagination and filtering by phone number.

        Args:
          page_number: Page number (1-indexed)

          page_size: Number of items per page

          phone_number: Filter by specific phone number (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reputation/numbers",
            page=SyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            model=ReputationPhoneNumberWithReputationData,
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
    ) -> None:
        """
        Remove a phone number from Number Reputation monitoring without requiring an
        `enterprise_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/reputation/numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNumbersResource(AsyncAPIResource):
    """
    Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
    """

    @cached_property
    def with_raw_response(self) -> AsyncNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumbersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Get reputation data for a specific phone number without requiring an
        `enterprise_id`.

        Same response as the enterprise-scoped endpoint. Uses cached data by default.

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false, returns
              cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/reputation/numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"fresh": fresh}, number_retrieve_params.NumberRetrieveParams),
            ),
            cast_to=NumberRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        phone_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        ReputationPhoneNumberWithReputationData, AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData]
    ]:
        """List all phone numbers enrolled in Number Reputation monitoring for your
        account.

        This is a simplified endpoint that does not require an `enterprise_id`
        — it returns numbers across all your enterprises.

        Supports pagination and filtering by phone number.

        Args:
          page_number: Page number (1-indexed)

          page_size: Number of items per page

          phone_number: Filter by specific phone number (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/reputation/numbers",
            page=AsyncDefaultFlatPagination[ReputationPhoneNumberWithReputationData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "phone_number": phone_number,
                    },
                    number_list_params.NumberListParams,
                ),
            ),
            model=ReputationPhoneNumberWithReputationData,
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
    ) -> None:
        """
        Remove a phone number from Number Reputation monitoring without requiring an
        `enterprise_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/reputation/numbers/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NumbersResourceWithRawResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            numbers.delete,
        )


class AsyncNumbersResourceWithRawResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = async_to_raw_response_wrapper(
            numbers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            numbers.delete,
        )


class NumbersResourceWithStreamingResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            numbers.delete,
        )


class AsyncNumbersResourceWithStreamingResponse:
    def __init__(self, numbers: AsyncNumbersResource) -> None:
        self._numbers = numbers

        self.retrieve = async_to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            numbers.delete,
        )
