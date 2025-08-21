# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import integration_secret_list_params, integration_secret_create_params
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
from ..types.integration_secret_list_response import IntegrationSecretListResponse
from ..types.integration_secret_create_response import IntegrationSecretCreateResponse

__all__ = ["IntegrationSecretsResource", "AsyncIntegrationSecretsResource"]


class IntegrationSecretsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return IntegrationSecretsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        identifier: str,
        type: Literal["bearer", "basic"],
        token: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationSecretCreateResponse:
        """
        Create a new secret with an associated identifier that can be used to securely
        integrate with other services.

        Args:
          identifier: The unique identifier of the secret.

          type: The type of secret.

          token: The token for the secret. Required for bearer type secrets, ignored otherwise.

          password: The password for the secret. Required for basic type secrets, ignored otherwise.

          username: The username for the secret. Required for basic type secrets, ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/integration_secrets",
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "type": type,
                    "token": token,
                    "password": password,
                    "username": username,
                },
                integration_secret_create_params.IntegrationSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSecretCreateResponse,
        )

    def list(
        self,
        *,
        filter: integration_secret_list_params.Filter | NotGiven = NOT_GIVEN,
        page: integration_secret_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationSecretListResponse:
        """
        Retrieve a list of all integration secrets configured by the user.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/integration_secrets",
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
                    integration_secret_list_params.IntegrationSecretListParams,
                ),
            ),
            cast_to=IntegrationSecretListResponse,
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
    ) -> None:
        """
        Delete an integration secret given its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/integration_secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncIntegrationSecretsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationSecretsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationSecretsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationSecretsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncIntegrationSecretsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        identifier: str,
        type: Literal["bearer", "basic"],
        token: str | NotGiven = NOT_GIVEN,
        password: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationSecretCreateResponse:
        """
        Create a new secret with an associated identifier that can be used to securely
        integrate with other services.

        Args:
          identifier: The unique identifier of the secret.

          type: The type of secret.

          token: The token for the secret. Required for bearer type secrets, ignored otherwise.

          password: The password for the secret. Required for basic type secrets, ignored otherwise.

          username: The username for the secret. Required for basic type secrets, ignored otherwise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/integration_secrets",
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "type": type,
                    "token": token,
                    "password": password,
                    "username": username,
                },
                integration_secret_create_params.IntegrationSecretCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IntegrationSecretCreateResponse,
        )

    async def list(
        self,
        *,
        filter: integration_secret_list_params.Filter | NotGiven = NOT_GIVEN,
        page: integration_secret_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IntegrationSecretListResponse:
        """
        Retrieve a list of all integration secrets configured by the user.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[type]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/integration_secrets",
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
                    integration_secret_list_params.IntegrationSecretListParams,
                ),
            ),
            cast_to=IntegrationSecretListResponse,
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
    ) -> None:
        """
        Delete an integration secret given its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/integration_secrets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class IntegrationSecretsResourceWithRawResponse:
    def __init__(self, integration_secrets: IntegrationSecretsResource) -> None:
        self._integration_secrets = integration_secrets

        self.create = to_raw_response_wrapper(
            integration_secrets.create,
        )
        self.list = to_raw_response_wrapper(
            integration_secrets.list,
        )
        self.delete = to_raw_response_wrapper(
            integration_secrets.delete,
        )


class AsyncIntegrationSecretsResourceWithRawResponse:
    def __init__(self, integration_secrets: AsyncIntegrationSecretsResource) -> None:
        self._integration_secrets = integration_secrets

        self.create = async_to_raw_response_wrapper(
            integration_secrets.create,
        )
        self.list = async_to_raw_response_wrapper(
            integration_secrets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            integration_secrets.delete,
        )


class IntegrationSecretsResourceWithStreamingResponse:
    def __init__(self, integration_secrets: IntegrationSecretsResource) -> None:
        self._integration_secrets = integration_secrets

        self.create = to_streamed_response_wrapper(
            integration_secrets.create,
        )
        self.list = to_streamed_response_wrapper(
            integration_secrets.list,
        )
        self.delete = to_streamed_response_wrapper(
            integration_secrets.delete,
        )


class AsyncIntegrationSecretsResourceWithStreamingResponse:
    def __init__(self, integration_secrets: AsyncIntegrationSecretsResource) -> None:
        self._integration_secrets = integration_secrets

        self.create = async_to_streamed_response_wrapper(
            integration_secrets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            integration_secrets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            integration_secrets.delete,
        )
