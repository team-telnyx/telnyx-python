# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, overload

import httpx

from ..types import mobile_push_credential_list_params, mobile_push_credential_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.push_credential_response import PushCredentialResponse
from ..types.mobile_push_credential_list_response import MobilePushCredentialListResponse

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

    @overload
    def create(
        self,
        *,
        alias: str,
        certificate: str,
        private_key: str,
        type: Literal["ios"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          alias: Alias to uniquely identify the credential

          certificate: Certificate as received from APNs

          private_key: Corresponding private key to the certificate as received from APNs

          type: Type of mobile push credential. Should be <code>ios</code> here

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        alias: str,
        project_account_json_file: Dict[str, object],
        type: Literal["android"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          alias: Alias to uniquely identify the credential

          project_account_json_file: Private key file in JSON format

          type: Type of mobile push credential. Should be <code>android</code> here

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["alias", "certificate", "private_key", "type"], ["alias", "project_account_json_file", "type"])
    def create(
        self,
        *,
        alias: str,
        certificate: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        type: Literal["ios"] | Literal["android"],
        project_account_json_file: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        return self._post(
            "/mobile_push_credentials",
            body=maybe_transform(
                {
                    "alias": alias,
                    "certificate": certificate,
                    "private_key": private_key,
                    "type": type,
                    "project_account_json_file": project_account_json_file,
                },
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        filter: mobile_push_credential_list_params.Filter | NotGiven = NOT_GIVEN,
        page: mobile_push_credential_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MobilePushCredentialListResponse:
        """
        List mobile push credentials

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type],
              filter[alias]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/mobile_push_credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    mobile_push_credential_list_params.MobilePushCredentialListParams,
                ),
            ),
            cast_to=MobilePushCredentialListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    @overload
    async def create(
        self,
        *,
        alias: str,
        certificate: str,
        private_key: str,
        type: Literal["ios"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          alias: Alias to uniquely identify the credential

          certificate: Certificate as received from APNs

          private_key: Corresponding private key to the certificate as received from APNs

          type: Type of mobile push credential. Should be <code>ios</code> here

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        alias: str,
        project_account_json_file: Dict[str, object],
        type: Literal["android"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        """
        Creates a new mobile push credential

        Args:
          alias: Alias to uniquely identify the credential

          project_account_json_file: Private key file in JSON format

          type: Type of mobile push credential. Should be <code>android</code> here

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["alias", "certificate", "private_key", "type"], ["alias", "project_account_json_file", "type"])
    async def create(
        self,
        *,
        alias: str,
        certificate: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        type: Literal["ios"] | Literal["android"],
        project_account_json_file: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PushCredentialResponse:
        return await self._post(
            "/mobile_push_credentials",
            body=await async_maybe_transform(
                {
                    "alias": alias,
                    "certificate": certificate,
                    "private_key": private_key,
                    "type": type,
                    "project_account_json_file": project_account_json_file,
                },
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def list(
        self,
        *,
        filter: mobile_push_credential_list_params.Filter | NotGiven = NOT_GIVEN,
        page: mobile_push_credential_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MobilePushCredentialListResponse:
        """
        List mobile push credentials

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type],
              filter[alias]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/mobile_push_credentials",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    mobile_push_credential_list_params.MobilePushCredentialListParams,
                ),
            ),
            cast_to=MobilePushCredentialListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
