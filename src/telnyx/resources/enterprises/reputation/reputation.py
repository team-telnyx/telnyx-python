# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .numbers import (
    NumbersResource,
    AsyncNumbersResource,
    NumbersResourceWithRawResponse,
    AsyncNumbersResourceWithRawResponse,
    NumbersResourceWithStreamingResponse,
    AsyncNumbersResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.enterprises import reputation_enable_params, reputation_update_frequency_params
from ....types.enterprises.reputation_enable_response import ReputationEnableResponse
from ....types.enterprises.reputation_retrieve_response import ReputationRetrieveResponse
from ....types.enterprises.reputation_update_frequency_response import ReputationUpdateFrequencyResponse

__all__ = ["ReputationResource", "AsyncReputationResource"]


class ReputationResource(SyncAPIResource):
    """
    Manage Number Reputation enrollment and check frequency settings for an enterprise
    """

    @cached_property
    def numbers(self) -> NumbersResource:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return NumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReputationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationRetrieveResponse:
        """
        Retrieve the current Number Reputation settings for an enterprise.

        Returns the enrollment status (`pending`, `approved`, `rejected`, `deleted`),
        check frequency, and any rejection reasons.

        Returns `404` if reputation has not been enabled for this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationRetrieveResponse,
        )

    def disable(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disable Number Reputation for an enterprise.

        This will:

        - Delete the reputation settings record
        - Log the deletion for audit purposes
        - Stop all future automated reputation checks

        **Note:** Can only be performed on `approved` reputation settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def enable(
        self,
        enterprise_id: str,
        *,
        loa_document_id: str,
        check_frequency: Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationEnableResponse:
        """
        Enable Number Reputation service for an enterprise.

        **Requirements:**

        - Signed LOA (Letter of Authorization) document ID
        - Reputation check frequency (defaults to `business_daily`)
        - Number Reputation Terms of Service must be accepted

        **Flow:**

        1. Registers the enterprise for reputation monitoring
        2. Creates reputation settings with `pending` status
        3. Awaits admin approval before monitoring begins

        **Resubmission After Rejection:** If a previously rejected record exists, this
        endpoint will delete it and create a new `pending` record.

        **Available Frequencies:**

        - `business_daily` — Monday–Friday
        - `daily` — Every day
        - `weekly` — Once per week
        - `biweekly` — Once every two weeks
        - `monthly` — Once per month
        - `never` — Manual refresh only

        Args:
          loa_document_id: ID of the signed Letter of Authorization (LOA) document uploaded to the document
              service

          check_frequency: Frequency for automatically refreshing reputation data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "loa_document_id": loa_document_id,
                    "check_frequency": check_frequency,
                },
                reputation_enable_params.ReputationEnableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationEnableResponse,
        )

    def update_frequency(
        self,
        enterprise_id: str,
        *,
        check_frequency: Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationUpdateFrequencyResponse:
        """
        Update how often reputation data is automatically refreshed.

        **Note:** The enterprise must have `approved` reputation settings. Updating
        frequency on `pending` or `rejected` settings will return an error.

        **Available Frequencies:**

        - `business_daily` — Monday–Friday
        - `daily` — Every day including weekends
        - `weekly` — Once per week
        - `biweekly` — Once every two weeks
        - `monthly` — Once per month
        - `never` — Manual refresh only (no automatic checks)

        Args:
          check_frequency: New frequency for refreshing reputation data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._patch(
            path_template("/enterprises/{enterprise_id}/reputation/frequency", enterprise_id=enterprise_id),
            body=maybe_transform(
                {"check_frequency": check_frequency}, reputation_update_frequency_params.ReputationUpdateFrequencyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationUpdateFrequencyResponse,
        )


class AsyncReputationResource(AsyncAPIResource):
    """
    Manage Number Reputation enrollment and check frequency settings for an enterprise
    """

    @cached_property
    def numbers(self) -> AsyncNumbersResource:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return AsyncNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReputationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationRetrieveResponse:
        """
        Retrieve the current Number Reputation settings for an enterprise.

        Returns the enrollment status (`pending`, `approved`, `rejected`, `deleted`),
        check frequency, and any rejection reasons.

        Returns `404` if reputation has not been enabled for this enterprise.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._get(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationRetrieveResponse,
        )

    async def disable(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Disable Number Reputation for an enterprise.

        This will:

        - Delete the reputation settings record
        - Log the deletion for audit purposes
        - Stop all future automated reputation checks

        **Note:** Can only be performed on `approved` reputation settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def enable(
        self,
        enterprise_id: str,
        *,
        loa_document_id: str,
        check_frequency: Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationEnableResponse:
        """
        Enable Number Reputation service for an enterprise.

        **Requirements:**

        - Signed LOA (Letter of Authorization) document ID
        - Reputation check frequency (defaults to `business_daily`)
        - Number Reputation Terms of Service must be accepted

        **Flow:**

        1. Registers the enterprise for reputation monitoring
        2. Creates reputation settings with `pending` status
        3. Awaits admin approval before monitoring begins

        **Resubmission After Rejection:** If a previously rejected record exists, this
        endpoint will delete it and create a new `pending` record.

        **Available Frequencies:**

        - `business_daily` — Monday–Friday
        - `daily` — Every day
        - `weekly` — Once per week
        - `biweekly` — Once every two weeks
        - `monthly` — Once per month
        - `never` — Manual refresh only

        Args:
          loa_document_id: ID of the signed Letter of Authorization (LOA) document uploaded to the document
              service

          check_frequency: Frequency for automatically refreshing reputation data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/reputation", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "loa_document_id": loa_document_id,
                    "check_frequency": check_frequency,
                },
                reputation_enable_params.ReputationEnableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationEnableResponse,
        )

    async def update_frequency(
        self,
        enterprise_id: str,
        *,
        check_frequency: Literal["business_daily", "daily", "weekly", "biweekly", "monthly", "never"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReputationUpdateFrequencyResponse:
        """
        Update how often reputation data is automatically refreshed.

        **Note:** The enterprise must have `approved` reputation settings. Updating
        frequency on `pending` or `rejected` settings will return an error.

        **Available Frequencies:**

        - `business_daily` — Monday–Friday
        - `daily` — Every day including weekends
        - `weekly` — Once per week
        - `biweekly` — Once every two weeks
        - `monthly` — Once per month
        - `never` — Manual refresh only (no automatic checks)

        Args:
          check_frequency: New frequency for refreshing reputation data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._patch(
            path_template("/enterprises/{enterprise_id}/reputation/frequency", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {"check_frequency": check_frequency}, reputation_update_frequency_params.ReputationUpdateFrequencyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReputationUpdateFrequencyResponse,
        )


class ReputationResourceWithRawResponse:
    def __init__(self, reputation: ReputationResource) -> None:
        self._reputation = reputation

        self.retrieve = to_raw_response_wrapper(
            reputation.retrieve,
        )
        self.disable = to_raw_response_wrapper(
            reputation.disable,
        )
        self.enable = to_raw_response_wrapper(
            reputation.enable,
        )
        self.update_frequency = to_raw_response_wrapper(
            reputation.update_frequency,
        )

    @cached_property
    def numbers(self) -> NumbersResourceWithRawResponse:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return NumbersResourceWithRawResponse(self._reputation.numbers)


class AsyncReputationResourceWithRawResponse:
    def __init__(self, reputation: AsyncReputationResource) -> None:
        self._reputation = reputation

        self.retrieve = async_to_raw_response_wrapper(
            reputation.retrieve,
        )
        self.disable = async_to_raw_response_wrapper(
            reputation.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            reputation.enable,
        )
        self.update_frequency = async_to_raw_response_wrapper(
            reputation.update_frequency,
        )

    @cached_property
    def numbers(self) -> AsyncNumbersResourceWithRawResponse:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return AsyncNumbersResourceWithRawResponse(self._reputation.numbers)


class ReputationResourceWithStreamingResponse:
    def __init__(self, reputation: ReputationResource) -> None:
        self._reputation = reputation

        self.retrieve = to_streamed_response_wrapper(
            reputation.retrieve,
        )
        self.disable = to_streamed_response_wrapper(
            reputation.disable,
        )
        self.enable = to_streamed_response_wrapper(
            reputation.enable,
        )
        self.update_frequency = to_streamed_response_wrapper(
            reputation.update_frequency,
        )

    @cached_property
    def numbers(self) -> NumbersResourceWithStreamingResponse:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return NumbersResourceWithStreamingResponse(self._reputation.numbers)


class AsyncReputationResourceWithStreamingResponse:
    def __init__(self, reputation: AsyncReputationResource) -> None:
        self._reputation = reputation

        self.retrieve = async_to_streamed_response_wrapper(
            reputation.retrieve,
        )
        self.disable = async_to_streamed_response_wrapper(
            reputation.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            reputation.enable,
        )
        self.update_frequency = async_to_streamed_response_wrapper(
            reputation.update_frequency,
        )

    @cached_property
    def numbers(self) -> AsyncNumbersResourceWithStreamingResponse:
        """
        Associate phone numbers with an enterprise for reputation monitoring and retrieve reputation scores
        """
        return AsyncNumbersResourceWithStreamingResponse(self._reputation.numbers)
