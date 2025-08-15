# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    telephony_credential_list_params,
    telephony_credential_create_params,
    telephony_credential_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.telephony_credential_list_response import TelephonyCredentialListResponse
from ..types.telephony_credential_create_response import TelephonyCredentialCreateResponse
from ..types.telephony_credential_delete_response import TelephonyCredentialDeleteResponse
from ..types.telephony_credential_update_response import TelephonyCredentialUpdateResponse
from ..types.telephony_credential_retrieve_response import TelephonyCredentialRetrieveResponse

__all__ = ["TelephonyCredentialsResource", "AsyncTelephonyCredentialsResource"]


class TelephonyCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelephonyCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TelephonyCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelephonyCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TelephonyCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connection_id: str,
        expires_at: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialCreateResponse:
        """
        Create a credential.

        Args:
          connection_id: Identifies the Credential Connection this credential is associated with.

          expires_at: ISO-8601 formatted date indicating when the credential will expire.

          tag: Tags a credential. A single tag can hold at maximum 1000 credentials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/telephony_credentials",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "expires_at": expires_at,
                    "name": name,
                    "tag": tag,
                },
                telephony_credential_create_params.TelephonyCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialRetrieveResponse:
        """
        Get the details of an existing On-demand Credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/telephony_credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        connection_id: str | NotGiven = NOT_GIVEN,
        expires_at: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialUpdateResponse:
        """
        Update an existing credential.

        Args:
          connection_id: Identifies the Credential Connection this credential is associated with.

          expires_at: ISO-8601 formatted date indicating when the credential will expire.

          tag: Tags a credential. A single tag can hold at maximum 1000 credentials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/telephony_credentials/{id}",
            body=maybe_transform(
                {
                    "connection_id": connection_id,
                    "expires_at": expires_at,
                    "name": name,
                    "tag": tag,
                },
                telephony_credential_update_params.TelephonyCredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialUpdateResponse,
        )

    def list(
        self,
        *,
        filter: telephony_credential_list_params.Filter | NotGiven = NOT_GIVEN,
        page: telephony_credential_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialListResponse:
        """
        List all On-demand Credentials.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[name], filter[status], filter[resource_id], filter[sip_username]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/telephony_credentials",
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
                    telephony_credential_list_params.TelephonyCredentialListParams,
                ),
            ),
            cast_to=TelephonyCredentialListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialDeleteResponse:
        """
        Delete an existing credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/telephony_credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialDeleteResponse,
        )

    def create_token(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create an Access Token (JWT) for the credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._post(
            f"/telephony_credentials/{id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncTelephonyCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelephonyCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelephonyCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelephonyCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTelephonyCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connection_id: str,
        expires_at: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialCreateResponse:
        """
        Create a credential.

        Args:
          connection_id: Identifies the Credential Connection this credential is associated with.

          expires_at: ISO-8601 formatted date indicating when the credential will expire.

          tag: Tags a credential. A single tag can hold at maximum 1000 credentials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/telephony_credentials",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "expires_at": expires_at,
                    "name": name,
                    "tag": tag,
                },
                telephony_credential_create_params.TelephonyCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialRetrieveResponse:
        """
        Get the details of an existing On-demand Credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/telephony_credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        connection_id: str | NotGiven = NOT_GIVEN,
        expires_at: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialUpdateResponse:
        """
        Update an existing credential.

        Args:
          connection_id: Identifies the Credential Connection this credential is associated with.

          expires_at: ISO-8601 formatted date indicating when the credential will expire.

          tag: Tags a credential. A single tag can hold at maximum 1000 credentials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/telephony_credentials/{id}",
            body=await async_maybe_transform(
                {
                    "connection_id": connection_id,
                    "expires_at": expires_at,
                    "name": name,
                    "tag": tag,
                },
                telephony_credential_update_params.TelephonyCredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: telephony_credential_list_params.Filter | NotGiven = NOT_GIVEN,
        page: telephony_credential_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialListResponse:
        """
        List all On-demand Credentials.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[name], filter[status], filter[resource_id], filter[sip_username]

          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/telephony_credentials",
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
                    telephony_credential_list_params.TelephonyCredentialListParams,
                ),
            ),
            cast_to=TelephonyCredentialListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelephonyCredentialDeleteResponse:
        """
        Delete an existing credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/telephony_credentials/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelephonyCredentialDeleteResponse,
        )

    async def create_token(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Create an Access Token (JWT) for the credential.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._post(
            f"/telephony_credentials/{id}/token",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class TelephonyCredentialsResourceWithRawResponse:
    def __init__(self, telephony_credentials: TelephonyCredentialsResource) -> None:
        self._telephony_credentials = telephony_credentials

        self.create = to_raw_response_wrapper(
            telephony_credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            telephony_credentials.retrieve,
        )
        self.update = to_raw_response_wrapper(
            telephony_credentials.update,
        )
        self.list = to_raw_response_wrapper(
            telephony_credentials.list,
        )
        self.delete = to_raw_response_wrapper(
            telephony_credentials.delete,
        )
        self.create_token = to_raw_response_wrapper(
            telephony_credentials.create_token,
        )


class AsyncTelephonyCredentialsResourceWithRawResponse:
    def __init__(self, telephony_credentials: AsyncTelephonyCredentialsResource) -> None:
        self._telephony_credentials = telephony_credentials

        self.create = async_to_raw_response_wrapper(
            telephony_credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            telephony_credentials.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            telephony_credentials.update,
        )
        self.list = async_to_raw_response_wrapper(
            telephony_credentials.list,
        )
        self.delete = async_to_raw_response_wrapper(
            telephony_credentials.delete,
        )
        self.create_token = async_to_raw_response_wrapper(
            telephony_credentials.create_token,
        )


class TelephonyCredentialsResourceWithStreamingResponse:
    def __init__(self, telephony_credentials: TelephonyCredentialsResource) -> None:
        self._telephony_credentials = telephony_credentials

        self.create = to_streamed_response_wrapper(
            telephony_credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            telephony_credentials.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            telephony_credentials.update,
        )
        self.list = to_streamed_response_wrapper(
            telephony_credentials.list,
        )
        self.delete = to_streamed_response_wrapper(
            telephony_credentials.delete,
        )
        self.create_token = to_streamed_response_wrapper(
            telephony_credentials.create_token,
        )


class AsyncTelephonyCredentialsResourceWithStreamingResponse:
    def __init__(self, telephony_credentials: AsyncTelephonyCredentialsResource) -> None:
        self._telephony_credentials = telephony_credentials

        self.create = async_to_streamed_response_wrapper(
            telephony_credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            telephony_credentials.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            telephony_credentials.update,
        )
        self.list = async_to_streamed_response_wrapper(
            telephony_credentials.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            telephony_credentials.delete,
        )
        self.create_token = async_to_streamed_response_wrapper(
            telephony_credentials.create_token,
        )
