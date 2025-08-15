# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import custom_storage_credential_create_params, custom_storage_credential_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.custom_storage_credential_create_response import CustomStorageCredentialCreateResponse
from ..types.custom_storage_credential_update_response import CustomStorageCredentialUpdateResponse
from ..types.custom_storage_credential_retrieve_response import CustomStorageCredentialRetrieveResponse

__all__ = ["CustomStorageCredentialsResource", "AsyncCustomStorageCredentialsResource"]


class CustomStorageCredentialsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomStorageCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CustomStorageCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomStorageCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CustomStorageCredentialsResourceWithStreamingResponse(self)

    def create(
        self,
        connection_id: str,
        *,
        backend: Literal["gcs", "s3", "azure"],
        configuration: custom_storage_credential_create_params.Configuration,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialCreateResponse:
        """
        Creates a custom storage credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            f"/custom_storage_credentials/{connection_id}",
            body=maybe_transform(
                {
                    "backend": backend,
                    "configuration": configuration,
                },
                custom_storage_credential_create_params.CustomStorageCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialCreateResponse,
        )

    def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialRetrieveResponse:
        """
        Returns the information about custom storage credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            f"/custom_storage_credentials/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialRetrieveResponse,
        )

    def update(
        self,
        connection_id: str,
        *,
        backend: Literal["gcs", "s3", "azure"],
        configuration: custom_storage_credential_update_params.Configuration,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialUpdateResponse:
        """
        Updates a stored custom credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._put(
            f"/custom_storage_credentials/{connection_id}",
            body=maybe_transform(
                {
                    "backend": backend,
                    "configuration": configuration,
                },
                custom_storage_credential_update_params.CustomStorageCredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialUpdateResponse,
        )

    def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored custom credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/custom_storage_credentials/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomStorageCredentialsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomStorageCredentialsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomStorageCredentialsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomStorageCredentialsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCustomStorageCredentialsResourceWithStreamingResponse(self)

    async def create(
        self,
        connection_id: str,
        *,
        backend: Literal["gcs", "s3", "azure"],
        configuration: custom_storage_credential_create_params.Configuration,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialCreateResponse:
        """
        Creates a custom storage credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            f"/custom_storage_credentials/{connection_id}",
            body=await async_maybe_transform(
                {
                    "backend": backend,
                    "configuration": configuration,
                },
                custom_storage_credential_create_params.CustomStorageCredentialCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialCreateResponse,
        )

    async def retrieve(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialRetrieveResponse:
        """
        Returns the information about custom storage credentials.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            f"/custom_storage_credentials/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialRetrieveResponse,
        )

    async def update(
        self,
        connection_id: str,
        *,
        backend: Literal["gcs", "s3", "azure"],
        configuration: custom_storage_credential_update_params.Configuration,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomStorageCredentialUpdateResponse:
        """
        Updates a stored custom credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._put(
            f"/custom_storage_credentials/{connection_id}",
            body=await async_maybe_transform(
                {
                    "backend": backend,
                    "configuration": configuration,
                },
                custom_storage_credential_update_params.CustomStorageCredentialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomStorageCredentialUpdateResponse,
        )

    async def delete(
        self,
        connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored custom credentials configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/custom_storage_credentials/{connection_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomStorageCredentialsResourceWithRawResponse:
    def __init__(self, custom_storage_credentials: CustomStorageCredentialsResource) -> None:
        self._custom_storage_credentials = custom_storage_credentials

        self.create = to_raw_response_wrapper(
            custom_storage_credentials.create,
        )
        self.retrieve = to_raw_response_wrapper(
            custom_storage_credentials.retrieve,
        )
        self.update = to_raw_response_wrapper(
            custom_storage_credentials.update,
        )
        self.delete = to_raw_response_wrapper(
            custom_storage_credentials.delete,
        )


class AsyncCustomStorageCredentialsResourceWithRawResponse:
    def __init__(self, custom_storage_credentials: AsyncCustomStorageCredentialsResource) -> None:
        self._custom_storage_credentials = custom_storage_credentials

        self.create = async_to_raw_response_wrapper(
            custom_storage_credentials.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            custom_storage_credentials.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            custom_storage_credentials.update,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_storage_credentials.delete,
        )


class CustomStorageCredentialsResourceWithStreamingResponse:
    def __init__(self, custom_storage_credentials: CustomStorageCredentialsResource) -> None:
        self._custom_storage_credentials = custom_storage_credentials

        self.create = to_streamed_response_wrapper(
            custom_storage_credentials.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            custom_storage_credentials.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            custom_storage_credentials.update,
        )
        self.delete = to_streamed_response_wrapper(
            custom_storage_credentials.delete,
        )


class AsyncCustomStorageCredentialsResourceWithStreamingResponse:
    def __init__(self, custom_storage_credentials: AsyncCustomStorageCredentialsResource) -> None:
        self._custom_storage_credentials = custom_storage_credentials

        self.create = async_to_streamed_response_wrapper(
            custom_storage_credentials.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            custom_storage_credentials.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_storage_credentials.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_storage_credentials.delete,
        )
