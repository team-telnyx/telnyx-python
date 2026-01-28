# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import mobile_push_credential_list_params, mobile_push_credential_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.push_credential import PushCredential
from ..types.push_credential_response import PushCredentialResponse

__all__ = ["MobilePushCredentialsResource", "AsyncMobilePushCredentialsResource"]


class MobilePushCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MobilePushCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MobilePushCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MobilePushCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MobilePushCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        create_mobile_push_credential_request: mobile_push_credential_create_params.CreateMobilePushCredentialRequest,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mobile_push_credentials",
            body=maybe_transform(
                create_mobile_push_credential_request,
                mobile_push_credential_create_params.MobilePushCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushCredentialResponse,
        )

    def retrieve(
        self,
        push_credential_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushCredentialResponse:
        """
        Retrieves mobile push credential based on the given `push_credential_id`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not push_credential_id:
            raise ValueError(f"Expected a non-empty value for `push_credential_id` but received {push_credential_id!r}")
        return self._get(
            f"/mobile_push_credentials/{push_credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushCredentialResponse,
        )

    def list(
        self,
        *,
        filter: mobile_push_credential_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PushCredential]:
        """
        List mobile push credentials

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type],
              filter[alias]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mobile_push_credentials",
            page=SyncDefaultFlatPagination[PushCredential],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    mobile_push_credential_list_params.MobilePushCredentialListParams,
                ),
            ),
            model=PushCredential,
        )

    def delete(
        self,
        push_credential_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a mobile push credential based on the given `push_credential_id`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not push_credential_id:
            raise ValueError(f"Expected a non-empty value for `push_credential_id` but received {push_credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/mobile_push_credentials/{push_credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMobilePushCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMobilePushCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMobilePushCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMobilePushCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMobilePushCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        create_mobile_push_credential_request: mobile_push_credential_create_params.CreateMobilePushCredentialRequest,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mobile_push_credentials",
            body=await async_maybe_transform(
                create_mobile_push_credential_request,
                mobile_push_credential_create_params.MobilePushCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushCredentialResponse,
        )

    async def retrieve(
        self,
        push_credential_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PushCredentialResponse:
        """
        Retrieves mobile push credential based on the given `push_credential_id`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not push_credential_id:
            raise ValueError(f"Expected a non-empty value for `push_credential_id` but received {push_credential_id!r}")
        return await self._get(
            f"/mobile_push_credentials/{push_credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PushCredentialResponse,
        )

    def list(
        self,
        *,
        filter: mobile_push_credential_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PushCredential, AsyncDefaultFlatPagination[PushCredential]]:
        """
        List mobile push credentials

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type],
              filter[alias]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mobile_push_credentials",
            page=AsyncDefaultFlatPagination[PushCredential],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    mobile_push_credential_list_params.MobilePushCredentialListParams,
                ),
            ),
            model=PushCredential,
        )

    async def delete(
        self,
        push_credential_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a mobile push credential based on the given `push_credential_id`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not push_credential_id:
            raise ValueError(f"Expected a non-empty value for `push_credential_id` but received {push_credential_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/mobile_push_credentials/{push_credential_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MobilePushCredentialsResourceWithRawResponse:
    def __init__(self, mobile_push_credentials: MobilePushCredentialsResource) -> None:
        self._mobile_push_credentials = mobile_push_credentials

        self.create = to_raw_response_wrapper(
            mobile_push_credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mobile_push_credentials.retrieve,
        )
        self.list = to_raw_response_wrapper(
            mobile_push_credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            mobile_push_credentials.delete,
        )


class AsyncMobilePushCredentialsResourceWithRawResponse:
    def __init__(self, mobile_push_credentials: AsyncMobilePushCredentialsResource) -> None:
        self._mobile_push_credentials = mobile_push_credentials

        self.create = async_to_raw_response_wrapper(
            mobile_push_credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mobile_push_credentials.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            mobile_push_credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mobile_push_credentials.delete,
        )


class MobilePushCredentialsResourceWithStreamingResponse:
    def __init__(self, mobile_push_credentials: MobilePushCredentialsResource) -> None:
        self._mobile_push_credentials = mobile_push_credentials

        self.create = to_streamed_response_wrapper(
            mobile_push_credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mobile_push_credentials.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            mobile_push_credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            mobile_push_credentials.delete,
        )


class AsyncMobilePushCredentialsResourceWithStreamingResponse:
    def __init__(self, mobile_push_credentials: AsyncMobilePushCredentialsResource) -> None:
        self._mobile_push_credentials = mobile_push_credentials

        self.create = async_to_streamed_response_wrapper(
            mobile_push_credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mobile_push_credentials.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            mobile_push_credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mobile_push_credentials.delete,
        )
