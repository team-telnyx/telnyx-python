# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
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
from ...types.terms_of_service import agreement_list_params
from ...types.terms_of_service.agreement_list_response import AgreementListResponse
from ...types.terms_of_service.agreement_retrieve_response import AgreementRetrieveResponse

__all__ = ["AgreementsResource", "AsyncAgreementsResource"]


class AgreementsResource(SyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> AgreementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AgreementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgreementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AgreementsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agreement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgreementRetrieveResponse:
        """Retrieve a single ToS agreement record.

        Returns `404` if the agreement does not
        exist or does not belong to the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agreement_id:
            raise ValueError(f"Expected a non-empty value for `agreement_id` but received {agreement_id!r}")
        return self._get(
            path_template("/terms_of_service/agreements/{agreement_id}", agreement_id=agreement_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgreementRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_type: Literal["branded_calling", "number_reputation"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[AgreementListResponse]:
        """Returns the Terms of Service agreements the authenticated user has on file.

        Each
        entry records the version agreed to and when. Most users only have one agreement
        per product, but if the ToS is updated and the user re-agrees a new entry is
        added.

        Results are paginated with the standard `page[number]` / `page[size]`
        parameters; the response uses the standard `{data, meta}` JSON:API envelope.

        By default this returns agreements for **all** products the user has agreed to.
        Pass the `product_type` query parameter to scope the result to a single product.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          product_type: Optional filter. Omit to list the user's agreements for **every** product
              (branded_calling and number_reputation); pass a value to return only that
              product's agreements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/terms_of_service/agreements",
            page=SyncDefaultFlatPagination[AgreementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_type": product_type,
                    },
                    agreement_list_params.AgreementListParams,
                ),
            ),
            model=AgreementListResponse,
        )


class AsyncAgreementsResource(AsyncAPIResource):
    """
    Accept and review the Branded Calling and Phone Number Reputation terms of service.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAgreementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgreementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgreementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAgreementsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agreement_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgreementRetrieveResponse:
        """Retrieve a single ToS agreement record.

        Returns `404` if the agreement does not
        exist or does not belong to the authenticated user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agreement_id:
            raise ValueError(f"Expected a non-empty value for `agreement_id` but received {agreement_id!r}")
        return await self._get(
            path_template("/terms_of_service/agreements/{agreement_id}", agreement_id=agreement_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgreementRetrieveResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        product_type: Literal["branded_calling", "number_reputation"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgreementListResponse, AsyncDefaultFlatPagination[AgreementListResponse]]:
        """Returns the Terms of Service agreements the authenticated user has on file.

        Each
        entry records the version agreed to and when. Most users only have one agreement
        per product, but if the ToS is updated and the user re-agrees a new entry is
        added.

        Results are paginated with the standard `page[number]` / `page[size]`
        parameters; the response uses the standard `{data, meta}` JSON:API envelope.

        By default this returns agreements for **all** products the user has agreed to.
        Pass the `product_type` query parameter to scope the result to a single product.

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          product_type: Optional filter. Omit to list the user's agreements for **every** product
              (branded_calling and number_reputation); pass a value to return only that
              product's agreements.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/terms_of_service/agreements",
            page=AsyncDefaultFlatPagination[AgreementListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "product_type": product_type,
                    },
                    agreement_list_params.AgreementListParams,
                ),
            ),
            model=AgreementListResponse,
        )


class AgreementsResourceWithRawResponse:
    def __init__(self, agreements: AgreementsResource) -> None:
        self._agreements = agreements

        self.retrieve = to_raw_response_wrapper(
            agreements.retrieve,
        )
        self.list = to_raw_response_wrapper(
            agreements.list,
        )


class AsyncAgreementsResourceWithRawResponse:
    def __init__(self, agreements: AsyncAgreementsResource) -> None:
        self._agreements = agreements

        self.retrieve = async_to_raw_response_wrapper(
            agreements.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            agreements.list,
        )


class AgreementsResourceWithStreamingResponse:
    def __init__(self, agreements: AgreementsResource) -> None:
        self._agreements = agreements

        self.retrieve = to_streamed_response_wrapper(
            agreements.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            agreements.list,
        )


class AsyncAgreementsResourceWithStreamingResponse:
    def __init__(self, agreements: AsyncAgreementsResource) -> None:
        self._agreements = agreements

        self.retrieve = async_to_streamed_response_wrapper(
            agreements.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            agreements.list,
        )
