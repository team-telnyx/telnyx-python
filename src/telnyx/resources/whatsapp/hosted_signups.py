# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.whatsapp import hosted_signup_list_params, hosted_signup_create_params
from ...types.whatsapp.hosted_signup_list_response import HostedSignupListResponse
from ...types.whatsapp.hosted_signup_create_response import HostedSignupCreateResponse
from ...types.whatsapp.hosted_signup_retrieve_response import HostedSignupRetrieveResponse

__all__ = ["HostedSignupsResource", "AsyncHostedSignupsResource"]


class HostedSignupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostedSignupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return HostedSignupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostedSignupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return HostedSignupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        app_id: str,
        expires_at: Union[str, datetime] | Omit = omit,
        signup_type: Literal["standard", "coexistence"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostedSignupCreateResponse:
        """
        Create a time-limited onboarding URL on the Telnyx-hosted Embedded Signup page
        for a Tech Provider's end customer. Set `signup_type` to `coexistence` to launch
        Meta's WhatsApp Business app coexistence flow instead of standard Cloud API
        onboarding.

        Args:
          app_id: Meta App ID linked to the Telnyx account. The app must be enabled.

          expires_at: When the onboarding URL expires, in RFC 3339 format. Must be in the future and
              at most 3 days ahead. Defaults to 24 hours after creation.

          signup_type: Onboarding flow the hosted page launches. Use `coexistence` for a number that
              remains active in the WhatsApp Business app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/whatsapp/hosted_signups",
            body=maybe_transform(
                {
                    "app_id": app_id,
                    "expires_at": expires_at,
                    "signup_type": signup_type,
                },
                hosted_signup_create_params.HostedSignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostedSignupCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostedSignupRetrieveResponse:
        """
        Retrieve a hosted signup and its onboarding URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/whatsapp/hosted_signups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostedSignupRetrieveResponse,
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
    ) -> SyncDefaultFlatPagination[HostedSignupListResponse]:
        """List hosted signups created by the account, newest first.

        Expired hosted signups
        are included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/whatsapp/hosted_signups",
            page=SyncDefaultFlatPagination[HostedSignupListResponse],
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
                    hosted_signup_list_params.HostedSignupListParams,
                ),
            ),
            model=HostedSignupListResponse,
        )


class AsyncHostedSignupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostedSignupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostedSignupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostedSignupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncHostedSignupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        app_id: str,
        expires_at: Union[str, datetime] | Omit = omit,
        signup_type: Literal["standard", "coexistence"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostedSignupCreateResponse:
        """
        Create a time-limited onboarding URL on the Telnyx-hosted Embedded Signup page
        for a Tech Provider's end customer. Set `signup_type` to `coexistence` to launch
        Meta's WhatsApp Business app coexistence flow instead of standard Cloud API
        onboarding.

        Args:
          app_id: Meta App ID linked to the Telnyx account. The app must be enabled.

          expires_at: When the onboarding URL expires, in RFC 3339 format. Must be in the future and
              at most 3 days ahead. Defaults to 24 hours after creation.

          signup_type: Onboarding flow the hosted page launches. Use `coexistence` for a number that
              remains active in the WhatsApp Business app.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/whatsapp/hosted_signups",
            body=await async_maybe_transform(
                {
                    "app_id": app_id,
                    "expires_at": expires_at,
                    "signup_type": signup_type,
                },
                hosted_signup_create_params.HostedSignupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostedSignupCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HostedSignupRetrieveResponse:
        """
        Retrieve a hosted signup and its onboarding URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/whatsapp/hosted_signups/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostedSignupRetrieveResponse,
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
    ) -> AsyncPaginator[HostedSignupListResponse, AsyncDefaultFlatPagination[HostedSignupListResponse]]:
        """List hosted signups created by the account, newest first.

        Expired hosted signups
        are included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/whatsapp/hosted_signups",
            page=AsyncDefaultFlatPagination[HostedSignupListResponse],
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
                    hosted_signup_list_params.HostedSignupListParams,
                ),
            ),
            model=HostedSignupListResponse,
        )


class HostedSignupsResourceWithRawResponse:
    def __init__(self, hosted_signups: HostedSignupsResource) -> None:
        self._hosted_signups = hosted_signups

        self.create = to_raw_response_wrapper(
            hosted_signups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            hosted_signups.retrieve,
        )
        self.list = to_raw_response_wrapper(
            hosted_signups.list,
        )


class AsyncHostedSignupsResourceWithRawResponse:
    def __init__(self, hosted_signups: AsyncHostedSignupsResource) -> None:
        self._hosted_signups = hosted_signups

        self.create = async_to_raw_response_wrapper(
            hosted_signups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            hosted_signups.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            hosted_signups.list,
        )


class HostedSignupsResourceWithStreamingResponse:
    def __init__(self, hosted_signups: HostedSignupsResource) -> None:
        self._hosted_signups = hosted_signups

        self.create = to_streamed_response_wrapper(
            hosted_signups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            hosted_signups.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            hosted_signups.list,
        )


class AsyncHostedSignupsResourceWithStreamingResponse:
    def __init__(self, hosted_signups: AsyncHostedSignupsResource) -> None:
        self._hosted_signups = hosted_signups

        self.create = async_to_streamed_response_wrapper(
            hosted_signups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            hosted_signups.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            hosted_signups.list,
        )
