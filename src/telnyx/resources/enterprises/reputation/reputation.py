# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .loa import (
    LoaResource,
    AsyncLoaResource,
    LoaResourceWithRawResponse,
    AsyncLoaResourceWithRawResponse,
    LoaResourceWithStreamingResponse,
    AsyncLoaResourceWithStreamingResponse,
)
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
from .remediation import (
    RemediationResource,
    AsyncRemediationResource,
    RemediationResourceWithRawResponse,
    AsyncRemediationResourceWithRawResponse,
    RemediationResourceWithStreamingResponse,
    AsyncRemediationResourceWithStreamingResponse,
)
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
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def numbers(self) -> NumbersResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResource(self._client)

    @cached_property
    def loa(self) -> LoaResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return LoaResource(self._client)

    @cached_property
    def remediation(self) -> RemediationResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return RemediationResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
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
        Phone Number Reputation tracks how your outbound caller-IDs are perceived (spam
        risk, engagement, etc.) across the call-screening ecosystem. This endpoint reads
        the enterprise-level settings: whether the product is enabled, the refresh
        cadence, and the stored Letter of Authorization document id.

        Returns `404` if reputation has never been enabled for this enterprise.

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
        """Disable Phone Number Reputation.

        All registered numbers are de-registered as a
        cascade. The enterprise itself is unaffected. Returns `204` on success, `404` if
        reputation is not enabled for this enterprise.

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
        """Activate Phone Number Reputation for the given enterprise.

        Requires an uploaded
        Letter of Authorization document (the `loa_document_id` references the Telnyx
        Documents API) and a refresh-frequency selection. After activation, individual
        phone numbers can be registered via `POST .../reputation/numbers`.

        **Prerequisite**: the calling user must have agreed to the Phone Number
        Reputation Terms of Service (`POST /terms_of_service/number_reputation/agree`).

        Failure modes:

        - `403` - Phone Number Reputation Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.
        - `400` - reputation already enabled for this enterprise.
        - `422` - `loa_document_id` missing or `check_frequency` invalid.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          loa_document_id: Id of the signed Letter of Authorization document, returned by the Telnyx
              Documents API after upload (upload via `POST /v2/documents`; see
              https://developers.telnyx.com/api/documents).

          check_frequency: How often Telnyx refreshes the stored reputation data for this enterprise's
              registered numbers.

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
        Update how often Telnyx refreshes the reputation data for this enterprise's
        registered numbers. The new frequency takes effect on the next scheduled
        refresh.

        The enterprise's reputation must be in `approved` status. A request made while
        the status is `pending` is rejected with `400 Bad Request`.

        Args:
          check_frequency: How often Telnyx refreshes the stored reputation data for this enterprise's
              registered numbers.

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
    """Phone-number reputation monitoring (spam-score lookup and tracking)."""

    @cached_property
    def numbers(self) -> AsyncNumbersResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResource(self._client)

    @cached_property
    def loa(self) -> AsyncLoaResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncLoaResource(self._client)

    @cached_property
    def remediation(self) -> AsyncRemediationResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncRemediationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
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
        Phone Number Reputation tracks how your outbound caller-IDs are perceived (spam
        risk, engagement, etc.) across the call-screening ecosystem. This endpoint reads
        the enterprise-level settings: whether the product is enabled, the refresh
        cadence, and the stored Letter of Authorization document id.

        Returns `404` if reputation has never been enabled for this enterprise.

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
        """Disable Phone Number Reputation.

        All registered numbers are de-registered as a
        cascade. The enterprise itself is unaffected. Returns `204` on success, `404` if
        reputation is not enabled for this enterprise.

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
        """Activate Phone Number Reputation for the given enterprise.

        Requires an uploaded
        Letter of Authorization document (the `loa_document_id` references the Telnyx
        Documents API) and a refresh-frequency selection. After activation, individual
        phone numbers can be registered via `POST .../reputation/numbers`.

        **Prerequisite**: the calling user must have agreed to the Phone Number
        Reputation Terms of Service (`POST /terms_of_service/number_reputation/agree`).

        Failure modes:

        - `403` - Phone Number Reputation Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.
        - `400` - reputation already enabled for this enterprise.
        - `422` - `loa_document_id` missing or `check_frequency` invalid.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          loa_document_id: Id of the signed Letter of Authorization document, returned by the Telnyx
              Documents API after upload (upload via `POST /v2/documents`; see
              https://developers.telnyx.com/api/documents).

          check_frequency: How often Telnyx refreshes the stored reputation data for this enterprise's
              registered numbers.

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
        Update how often Telnyx refreshes the reputation data for this enterprise's
        registered numbers. The new frequency takes effect on the next scheduled
        refresh.

        The enterprise's reputation must be in `approved` status. A request made while
        the status is `pending` is rejected with `400 Bad Request`.

        Args:
          check_frequency: How often Telnyx refreshes the stored reputation data for this enterprise's
              registered numbers.

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
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResourceWithRawResponse(self._reputation.numbers)

    @cached_property
    def loa(self) -> LoaResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return LoaResourceWithRawResponse(self._reputation.loa)

    @cached_property
    def remediation(self) -> RemediationResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return RemediationResourceWithRawResponse(self._reputation.remediation)


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
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResourceWithRawResponse(self._reputation.numbers)

    @cached_property
    def loa(self) -> AsyncLoaResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncLoaResourceWithRawResponse(self._reputation.loa)

    @cached_property
    def remediation(self) -> AsyncRemediationResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncRemediationResourceWithRawResponse(self._reputation.remediation)


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
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return NumbersResourceWithStreamingResponse(self._reputation.numbers)

    @cached_property
    def loa(self) -> LoaResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return LoaResourceWithStreamingResponse(self._reputation.loa)

    @cached_property
    def remediation(self) -> RemediationResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return RemediationResourceWithStreamingResponse(self._reputation.remediation)


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
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncNumbersResourceWithStreamingResponse(self._reputation.numbers)

    @cached_property
    def loa(self) -> AsyncLoaResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncLoaResourceWithStreamingResponse(self._reputation.loa)

    @cached_property
    def remediation(self) -> AsyncRemediationResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncRemediationResourceWithStreamingResponse(self._reputation.remediation)
