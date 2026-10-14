# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ...types.whatsapp import signup_list_params
from ...types.whatsapp.signup_list_response import SignupListResponse
from ...types.whatsapp.signup_retrieve_status_response import SignupRetrieveStatusResponse

__all__ = ["SignupResource", "AsyncSignupResource"]


class SignupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SignupResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_customer_id: str | Omit = omit,
        filter_waba_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[SignupListResponse]:
        """
        List finished WhatsApp Embedded Signup sessions, with status `SUCCESS` or
        `FAILURE`, newest first. Use the `errors` of a failed session to see why
        provisioning stopped.

        Args:
          filter_created_at_gte: Return sessions created at or after this time (RFC 3339)

          filter_created_at_lte: Return sessions created at or before this time (RFC 3339)

          filter_customer_id: Filter by the tech provider customer reference

          filter_waba_id: Filter by Meta WABA ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/whatsapp/signup",
            page=SyncDefaultFlatPagination[SignupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_customer_id": filter_customer_id,
                        "filter_waba_id": filter_waba_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    signup_list_params.SignupListParams,
                ),
            ),
            model=SignupListResponse,
        )

    def retrieve_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignupRetrieveStatusResponse:
        """
        Retrieve the current state and status of a WhatsApp Embedded Signup session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/whatsapp/signup/{id}/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignupRetrieveStatusResponse,
        )


class AsyncSignupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSignupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSignupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSignupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSignupResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter_created_at_gte: Union[str, datetime] | Omit = omit,
        filter_created_at_lte: Union[str, datetime] | Omit = omit,
        filter_customer_id: str | Omit = omit,
        filter_waba_id: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SignupListResponse, AsyncDefaultFlatPagination[SignupListResponse]]:
        """
        List finished WhatsApp Embedded Signup sessions, with status `SUCCESS` or
        `FAILURE`, newest first. Use the `errors` of a failed session to see why
        provisioning stopped.

        Args:
          filter_created_at_gte: Return sessions created at or after this time (RFC 3339)

          filter_created_at_lte: Return sessions created at or before this time (RFC 3339)

          filter_customer_id: Filter by the tech provider customer reference

          filter_waba_id: Filter by Meta WABA ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/whatsapp/signup",
            page=AsyncDefaultFlatPagination[SignupListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_created_at_gte": filter_created_at_gte,
                        "filter_created_at_lte": filter_created_at_lte,
                        "filter_customer_id": filter_customer_id,
                        "filter_waba_id": filter_waba_id,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    signup_list_params.SignupListParams,
                ),
            ),
            model=SignupListResponse,
        )

    async def retrieve_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignupRetrieveStatusResponse:
        """
        Retrieve the current state and status of a WhatsApp Embedded Signup session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/whatsapp/signup/{id}/status", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SignupRetrieveStatusResponse,
        )


class SignupResourceWithRawResponse:
    def __init__(self, signup: SignupResource) -> None:
        self._signup = signup

        self.list = to_raw_response_wrapper(
            signup.list,
        )
        self.retrieve_status = to_raw_response_wrapper(
            signup.retrieve_status,
        )


class AsyncSignupResourceWithRawResponse:
    def __init__(self, signup: AsyncSignupResource) -> None:
        self._signup = signup

        self.list = async_to_raw_response_wrapper(
            signup.list,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            signup.retrieve_status,
        )


class SignupResourceWithStreamingResponse:
    def __init__(self, signup: SignupResource) -> None:
        self._signup = signup

        self.list = to_streamed_response_wrapper(
            signup.list,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            signup.retrieve_status,
        )


class AsyncSignupResourceWithStreamingResponse:
    def __init__(self, signup: AsyncSignupResource) -> None:
        self._signup = signup

        self.list = async_to_streamed_response_wrapper(
            signup.list,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            signup.retrieve_status,
        )
