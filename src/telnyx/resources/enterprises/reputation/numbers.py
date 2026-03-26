# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.enterprises.reputation import number_list_params, number_create_params, number_retrieve_params
from ....types.enterprises.reputation.number_create_response import NumberCreateResponse
from ....types.enterprises.reputation.number_retrieve_response import NumberRetrieveResponse
from ....types.shared.reputation_phone_number_with_reputation_data import ReputationPhoneNumberWithReputationData

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

    def create(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCreateResponse:
        """
        Associate one or more phone numbers with an enterprise for Number Reputation
        monitoring.

        **Validations:**

        - Phone numbers must be in E.164 format (e.g., `+16035551234`)
        - Phone numbers must be in-service and belong to your account (verified via
          Warehouse)
        - Phone numbers must be US local numbers
        - Phone numbers cannot already be associated with any enterprise

        **Note:** This operation is atomic — if any number fails validation, the entire
        request fails.

        **Maximum:** 100 phone numbers per request.

        Args:
          phone_numbers: List of phone numbers to associate for reputation monitoring (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            body=maybe_transform({"phone_numbers": phone_numbers}, number_create_params.NumberCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCreateResponse,
        )

    def retrieve(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Get detailed reputation data for a specific phone number associated with an
        enterprise.

        **Query Parameters:**

        - `fresh` (default: `false`): When `true`, fetches fresh reputation data (incurs
          API cost). When `false`, returns cached data. If no cached data exists, fresh
          data is automatically fetched.

        **Returns:**

        - `spam_risk`: Overall spam risk level (`low`, `medium`, `high`)
        - `spam_category`: Spam category classification
        - `maturity_score`: Maturity metric (0–100)
        - `connection_score`: Connection quality metric (0–100)
        - `engagement_score`: Engagement metric (0–100)
        - `sentiment_score`: Sentiment metric (0–100)
        - `last_refreshed_at`: Timestamp of last data refresh

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false, returns
              cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
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
        enterprise_id: str,
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
        """
        List all phone numbers associated with an enterprise for Number Reputation
        monitoring.

        Returns phone numbers with their cached reputation data (if available). Supports
        pagination and filtering by phone number.

        Args:
          page_number: Page number (1-indexed)

          page_size: Number of items per page

          phone_number: Filter by specific phone number (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
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
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a phone number from Number Reputation monitoring for an enterprise.

        The number will no longer be tracked and reputation data will no longer be
        refreshed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
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

    async def create(
        self,
        enterprise_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberCreateResponse:
        """
        Associate one or more phone numbers with an enterprise for Number Reputation
        monitoring.

        **Validations:**

        - Phone numbers must be in E.164 format (e.g., `+16035551234`)
        - Phone numbers must be in-service and belong to your account (verified via
          Warehouse)
        - Phone numbers must be US local numbers
        - Phone numbers cannot already be associated with any enterprise

        **Note:** This operation is atomic — if any number fails validation, the entire
        request fails.

        **Maximum:** 100 phone numbers per request.

        Args:
          phone_numbers: List of phone numbers to associate for reputation monitoring (max 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
            body=await async_maybe_transform({"phone_numbers": phone_numbers}, number_create_params.NumberCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberCreateResponse,
        )

    async def retrieve(
        self,
        phone_number: str,
        *,
        enterprise_id: str,
        fresh: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberRetrieveResponse:
        """
        Get detailed reputation data for a specific phone number associated with an
        enterprise.

        **Query Parameters:**

        - `fresh` (default: `false`): When `true`, fetches fresh reputation data (incurs
          API cost). When `false`, returns cached data. If no cached data exists, fresh
          data is automatically fetched.

        **Returns:**

        - `spam_risk`: Overall spam risk level (`low`, `medium`, `high`)
        - `spam_category`: Spam category classification
        - `maturity_score`: Maturity metric (0–100)
        - `connection_score`: Connection quality metric (0–100)
        - `engagement_score`: Engagement metric (0–100)
        - `sentiment_score`: Sentiment metric (0–100)
        - `last_refreshed_at`: Timestamp of last data refresh

        Args:
          fresh: When true, fetches fresh reputation data (incurs API cost). When false, returns
              cached data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
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
        enterprise_id: str,
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
        """
        List all phone numbers associated with an enterprise for Number Reputation
        monitoring.

        Returns phone numbers with their cached reputation data (if available). Supports
        pagination and filtering by phone number.

        Args:
          page_number: Page number (1-indexed)

          page_size: Number of items per page

          phone_number: Filter by specific phone number (E.164 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/reputation/numbers", enterprise_id=enterprise_id),
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
        enterprise_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a phone number from Number Reputation monitoring for an enterprise.

        The number will no longer be tracked and reputation data will no longer be
        refreshed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/enterprises/{enterprise_id}/reputation/numbers/{phone_number}",
                enterprise_id=enterprise_id,
                phone_number=phone_number,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NumbersResourceWithRawResponse:
    def __init__(self, numbers: NumbersResource) -> None:
        self._numbers = numbers

        self.create = to_raw_response_wrapper(
            numbers.create,
        )
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

        self.create = async_to_raw_response_wrapper(
            numbers.create,
        )
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

        self.create = to_streamed_response_wrapper(
            numbers.create,
        )
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

        self.create = async_to_streamed_response_wrapper(
            numbers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            numbers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            numbers.delete,
        )
