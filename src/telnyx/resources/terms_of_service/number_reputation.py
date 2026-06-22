# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.terms_of_service.tos_agreement_wrapped import TosAgreementWrapped

__all__ = ["NumberReputationResource", "AsyncNumberReputationResource"]


class NumberReputationResource(SyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> NumberReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NumberReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NumberReputationResourceWithStreamingResponse(self)

    def agree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TosAgreementWrapped:
        """
        Records the authenticated user's agreement to the current Phone Number
        Reputation ToS. No body required. Idempotent.

        Prerequisite for using any of the `/v2/.../reputation/*` endpoints.
        """
        return self._post(
            "/terms_of_service/number_reputation/agree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TosAgreementWrapped,
        )


class AsyncNumberReputationResource(AsyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> AsyncNumberReputationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberReputationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberReputationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNumberReputationResourceWithStreamingResponse(self)

    async def agree(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TosAgreementWrapped:
        """
        Records the authenticated user's agreement to the current Phone Number
        Reputation ToS. No body required. Idempotent.

        Prerequisite for using any of the `/v2/.../reputation/*` endpoints.
        """
        return await self._post(
            "/terms_of_service/number_reputation/agree",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TosAgreementWrapped,
        )


class NumberReputationResourceWithRawResponse:
    def __init__(self, number_reputation: NumberReputationResource) -> None:
        self._number_reputation = number_reputation

        self.agree = to_raw_response_wrapper(
            number_reputation.agree,
        )


class AsyncNumberReputationResourceWithRawResponse:
    def __init__(self, number_reputation: AsyncNumberReputationResource) -> None:
        self._number_reputation = number_reputation

        self.agree = async_to_raw_response_wrapper(
            number_reputation.agree,
        )


class NumberReputationResourceWithStreamingResponse:
    def __init__(self, number_reputation: NumberReputationResource) -> None:
        self._number_reputation = number_reputation

        self.agree = to_streamed_response_wrapper(
            number_reputation.agree,
        )


class AsyncNumberReputationResourceWithStreamingResponse:
    def __init__(self, number_reputation: AsyncNumberReputationResource) -> None:
        self._number_reputation = number_reputation

        self.agree = async_to_streamed_response_wrapper(
            number_reputation.agree,
        )
