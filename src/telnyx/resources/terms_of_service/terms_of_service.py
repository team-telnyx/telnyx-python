# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import terms_of_service_retrieve_info_params, terms_of_service_retrieve_status_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .agreements import (
    AgreementsResource,
    AsyncAgreementsResource,
    AgreementsResourceWithRawResponse,
    AsyncAgreementsResourceWithRawResponse,
    AgreementsResourceWithStreamingResponse,
    AsyncAgreementsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .branded_calling import (
    BrandedCallingResource,
    AsyncBrandedCallingResource,
    BrandedCallingResourceWithRawResponse,
    AsyncBrandedCallingResourceWithRawResponse,
    BrandedCallingResourceWithStreamingResponse,
    AsyncBrandedCallingResourceWithStreamingResponse,
)
from .number_reputation import (
    NumberReputationResource,
    AsyncNumberReputationResource,
    NumberReputationResourceWithRawResponse,
    AsyncNumberReputationResourceWithRawResponse,
    NumberReputationResourceWithStreamingResponse,
    AsyncNumberReputationResourceWithStreamingResponse,
)
from ...types.terms_of_service import TosProductType
from ...types.terms_of_service_retrieve_info_response import TermsOfServiceRetrieveInfoResponse
from ...types.terms_of_service_retrieve_status_response import TermsOfServiceRetrieveStatusResponse

if TYPE_CHECKING:
    from ...types.terms_of_service.tos_product_type import TosProductType

__all__ = ["TermsOfServiceResource", "AsyncTermsOfServiceResource"]


class TermsOfServiceResource(SyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def number_reputation(self) -> NumberReputationResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return NumberReputationResource(self._client)

    @cached_property
    def agreements(self) -> AgreementsResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AgreementsResource(self._client)

    @cached_property
    def branded_calling(self) -> BrandedCallingResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return BrandedCallingResource(self._client)

    @cached_property
    def with_raw_response(self) -> TermsOfServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TermsOfServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TermsOfServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TermsOfServiceResourceWithStreamingResponse(self)

    def retrieve_info(
        self,
        *,
        product_type: TosProductType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TermsOfServiceRetrieveInfoResponse:
        """
        Returns the available Terms of Service agreements (product, current version,
        terms URL, effective date). Omit `product_type` to return all products; pass it
        to scope to one.

        Args:
          product_type: Optional product filter. Omit to return info for all products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/terms_of_service/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"product_type": product_type},
                    terms_of_service_retrieve_info_params.TermsOfServiceRetrieveInfoParams,
                ),
            ),
            cast_to=TermsOfServiceRetrieveInfoResponse,
        )

    def retrieve_status(
        self,
        *,
        product_type: TosProductType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TermsOfServiceRetrieveStatusResponse:
        """
        Returns whether the authenticated user has agreed to the current Terms of
        Service for the product given by `product_type`. Used during onboarding to
        decide whether to prompt the user with the ToS dialog before continuing.

        `agreement_required: true` means the user has not yet agreed (or has agreed to
        an outdated version) and must agree before using that product's endpoints.

        Args:
          product_type: Which product's ToS to check. Defaults to `branded_calling`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/terms_of_service/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"product_type": product_type},
                    terms_of_service_retrieve_status_params.TermsOfServiceRetrieveStatusParams,
                ),
            ),
            cast_to=TermsOfServiceRetrieveStatusResponse,
        )


class AsyncTermsOfServiceResource(AsyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncNumberReputationResource(self._client)

    @cached_property
    def agreements(self) -> AsyncAgreementsResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncAgreementsResource(self._client)

    @cached_property
    def branded_calling(self) -> AsyncBrandedCallingResource:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncBrandedCallingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTermsOfServiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTermsOfServiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTermsOfServiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTermsOfServiceResourceWithStreamingResponse(self)

    async def retrieve_info(
        self,
        *,
        product_type: TosProductType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TermsOfServiceRetrieveInfoResponse:
        """
        Returns the available Terms of Service agreements (product, current version,
        terms URL, effective date). Omit `product_type` to return all products; pass it
        to scope to one.

        Args:
          product_type: Optional product filter. Omit to return info for all products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/terms_of_service/info",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"product_type": product_type},
                    terms_of_service_retrieve_info_params.TermsOfServiceRetrieveInfoParams,
                ),
            ),
            cast_to=TermsOfServiceRetrieveInfoResponse,
        )

    async def retrieve_status(
        self,
        *,
        product_type: TosProductType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TermsOfServiceRetrieveStatusResponse:
        """
        Returns whether the authenticated user has agreed to the current Terms of
        Service for the product given by `product_type`. Used during onboarding to
        decide whether to prompt the user with the ToS dialog before continuing.

        `agreement_required: true` means the user has not yet agreed (or has agreed to
        an outdated version) and must agree before using that product's endpoints.

        Args:
          product_type: Which product's ToS to check. Defaults to `branded_calling`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/terms_of_service/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"product_type": product_type},
                    terms_of_service_retrieve_status_params.TermsOfServiceRetrieveStatusParams,
                ),
            ),
            cast_to=TermsOfServiceRetrieveStatusResponse,
        )


class TermsOfServiceResourceWithRawResponse:
    def __init__(self, terms_of_service: TermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

        self.retrieve_info = to_raw_response_wrapper(
            terms_of_service.retrieve_info,
        )
        self.retrieve_status = to_raw_response_wrapper(
            terms_of_service.retrieve_status,
        )

    @cached_property
    def number_reputation(self) -> NumberReputationResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return NumberReputationResourceWithRawResponse(self._terms_of_service.number_reputation)

    @cached_property
    def agreements(self) -> AgreementsResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AgreementsResourceWithRawResponse(self._terms_of_service.agreements)

    @cached_property
    def branded_calling(self) -> BrandedCallingResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return BrandedCallingResourceWithRawResponse(self._terms_of_service.branded_calling)


class AsyncTermsOfServiceResourceWithRawResponse:
    def __init__(self, terms_of_service: AsyncTermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

        self.retrieve_info = async_to_raw_response_wrapper(
            terms_of_service.retrieve_info,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            terms_of_service.retrieve_status,
        )

    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncNumberReputationResourceWithRawResponse(self._terms_of_service.number_reputation)

    @cached_property
    def agreements(self) -> AsyncAgreementsResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncAgreementsResourceWithRawResponse(self._terms_of_service.agreements)

    @cached_property
    def branded_calling(self) -> AsyncBrandedCallingResourceWithRawResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncBrandedCallingResourceWithRawResponse(self._terms_of_service.branded_calling)


class TermsOfServiceResourceWithStreamingResponse:
    def __init__(self, terms_of_service: TermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

        self.retrieve_info = to_streamed_response_wrapper(
            terms_of_service.retrieve_info,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            terms_of_service.retrieve_status,
        )

    @cached_property
    def number_reputation(self) -> NumberReputationResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return NumberReputationResourceWithStreamingResponse(self._terms_of_service.number_reputation)

    @cached_property
    def agreements(self) -> AgreementsResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AgreementsResourceWithStreamingResponse(self._terms_of_service.agreements)

    @cached_property
    def branded_calling(self) -> BrandedCallingResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return BrandedCallingResourceWithStreamingResponse(self._terms_of_service.branded_calling)


class AsyncTermsOfServiceResourceWithStreamingResponse:
    def __init__(self, terms_of_service: AsyncTermsOfServiceResource) -> None:
        self._terms_of_service = terms_of_service

        self.retrieve_info = async_to_streamed_response_wrapper(
            terms_of_service.retrieve_info,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            terms_of_service.retrieve_status,
        )

    @cached_property
    def number_reputation(self) -> AsyncNumberReputationResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncNumberReputationResourceWithStreamingResponse(self._terms_of_service.number_reputation)

    @cached_property
    def agreements(self) -> AsyncAgreementsResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncAgreementsResourceWithStreamingResponse(self._terms_of_service.agreements)

    @cached_property
    def branded_calling(self) -> AsyncBrandedCallingResourceWithStreamingResponse:
        """
        Accept and review the Branded Calling and Phone Number Reputation terms of service.
        """
        return AsyncBrandedCallingResourceWithStreamingResponse(self._terms_of_service.branded_calling)
