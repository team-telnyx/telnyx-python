# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    authentication_provider_list_params,
    authentication_provider_create_params,
    authentication_provider_update_params,
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
from ..types.settings_param import SettingsParam
from ..types.authentication_provider_list_response import AuthenticationProviderListResponse
from ..types.authentication_provider_create_response import AuthenticationProviderCreateResponse
from ..types.authentication_provider_delete_response import AuthenticationProviderDeleteResponse
from ..types.authentication_provider_update_response import AuthenticationProviderUpdateResponse
from ..types.authentication_provider_retrieve_response import AuthenticationProviderRetrieveResponse

__all__ = ["AuthenticationProvidersResource", "AsyncAuthenticationProvidersResource"]


class AuthenticationProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AuthenticationProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        settings: SettingsParam,
        short_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        settings_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderCreateResponse:
        """
        Creates an authentication provider.

        Args:
          name: The name associated with the authentication provider.

          settings: The settings associated with the authentication provider.

          short_name: The short name associated with the authentication provider. This must be unique
              and URL-friendly, as it's going to be part of the login URL.

          active: The active status of the authentication provider

          settings_url: The URL for the identity provider metadata file to populate the settings
              automatically. If the settings attribute is provided, that will be used instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/authentication_providers",
            body=maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "short_name": short_name,
                    "active": active,
                    "settings_url": settings_url,
                },
                authentication_provider_create_params.AuthenticationProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderCreateResponse,
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
    ) -> AuthenticationProviderRetrieveResponse:
        """
        Retrieves the details of an existing authentication provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/authentication_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        settings: SettingsParam | NotGiven = NOT_GIVEN,
        settings_url: str | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderUpdateResponse:
        """
        Updates settings of an existing authentication provider.

        Args:
          active: The active status of the authentication provider

          name: The name associated with the authentication provider.

          settings: The settings associated with the authentication provider.

          settings_url: The URL for the identity provider metadata file to populate the settings
              automatically. If the settings attribute is provided, that will be used instead.

          short_name: The short name associated with the authentication provider. This must be unique
              and URL-friendly, as it's going to be part of the login URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/authentication_providers/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "name": name,
                    "settings": settings,
                    "settings_url": settings_url,
                    "short_name": short_name,
                },
                authentication_provider_update_params.AuthenticationProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderUpdateResponse,
        )

    def list(
        self,
        *,
        page: authentication_provider_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal[
            "name",
            "-name",
            "short_name",
            "-short_name",
            "active",
            "-active",
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderListResponse:
        """
        Returns a list of your SSO authentication providers.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code>-</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>name</code>: sorts the result by the
                  <code>name</code> field in ascending order.
                </li>
                <li>
                  <code>-name</code>: sorts the result by the
                  <code>name</code> field in descending order.
                </li>
              </ul><br/>If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/authentication_providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "sort": sort,
                    },
                    authentication_provider_list_params.AuthenticationProviderListParams,
                ),
            ),
            cast_to=AuthenticationProviderListResponse,
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
    ) -> AuthenticationProviderDeleteResponse:
        """
        Deletes an existing authentication provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/authentication_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderDeleteResponse,
        )


class AsyncAuthenticationProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAuthenticationProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        settings: SettingsParam,
        short_name: str,
        active: bool | NotGiven = NOT_GIVEN,
        settings_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderCreateResponse:
        """
        Creates an authentication provider.

        Args:
          name: The name associated with the authentication provider.

          settings: The settings associated with the authentication provider.

          short_name: The short name associated with the authentication provider. This must be unique
              and URL-friendly, as it's going to be part of the login URL.

          active: The active status of the authentication provider

          settings_url: The URL for the identity provider metadata file to populate the settings
              automatically. If the settings attribute is provided, that will be used instead.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/authentication_providers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "settings": settings,
                    "short_name": short_name,
                    "active": active,
                    "settings_url": settings_url,
                },
                authentication_provider_create_params.AuthenticationProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderCreateResponse,
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
    ) -> AuthenticationProviderRetrieveResponse:
        """
        Retrieves the details of an existing authentication provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/authentication_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        settings: SettingsParam | NotGiven = NOT_GIVEN,
        settings_url: str | NotGiven = NOT_GIVEN,
        short_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderUpdateResponse:
        """
        Updates settings of an existing authentication provider.

        Args:
          active: The active status of the authentication provider

          name: The name associated with the authentication provider.

          settings: The settings associated with the authentication provider.

          settings_url: The URL for the identity provider metadata file to populate the settings
              automatically. If the settings attribute is provided, that will be used instead.

          short_name: The short name associated with the authentication provider. This must be unique
              and URL-friendly, as it's going to be part of the login URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/authentication_providers/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "name": name,
                    "settings": settings,
                    "settings_url": settings_url,
                    "short_name": short_name,
                },
                authentication_provider_update_params.AuthenticationProviderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderUpdateResponse,
        )

    async def list(
        self,
        *,
        page: authentication_provider_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal[
            "name",
            "-name",
            "short_name",
            "-short_name",
            "active",
            "-active",
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationProviderListResponse:
        """
        Returns a list of your SSO authentication providers.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[number],
              page[size]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code>-</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>name</code>: sorts the result by the
                  <code>name</code> field in ascending order.
                </li>
                <li>
                  <code>-name</code>: sorts the result by the
                  <code>name</code> field in descending order.
                </li>
              </ul><br/>If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/authentication_providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "sort": sort,
                    },
                    authentication_provider_list_params.AuthenticationProviderListParams,
                ),
            ),
            cast_to=AuthenticationProviderListResponse,
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
    ) -> AuthenticationProviderDeleteResponse:
        """
        Deletes an existing authentication provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/authentication_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationProviderDeleteResponse,
        )


class AuthenticationProvidersResourceWithRawResponse:
    def __init__(self, authentication_providers: AuthenticationProvidersResource) -> None:
        self._authentication_providers = authentication_providers

        self.create = to_raw_response_wrapper(
            authentication_providers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            authentication_providers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            authentication_providers.update,
        )
        self.list = to_raw_response_wrapper(
            authentication_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            authentication_providers.delete,
        )


class AsyncAuthenticationProvidersResourceWithRawResponse:
    def __init__(self, authentication_providers: AsyncAuthenticationProvidersResource) -> None:
        self._authentication_providers = authentication_providers

        self.create = async_to_raw_response_wrapper(
            authentication_providers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            authentication_providers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            authentication_providers.update,
        )
        self.list = async_to_raw_response_wrapper(
            authentication_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            authentication_providers.delete,
        )


class AuthenticationProvidersResourceWithStreamingResponse:
    def __init__(self, authentication_providers: AuthenticationProvidersResource) -> None:
        self._authentication_providers = authentication_providers

        self.create = to_streamed_response_wrapper(
            authentication_providers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            authentication_providers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            authentication_providers.update,
        )
        self.list = to_streamed_response_wrapper(
            authentication_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            authentication_providers.delete,
        )


class AsyncAuthenticationProvidersResourceWithStreamingResponse:
    def __init__(self, authentication_providers: AsyncAuthenticationProvidersResource) -> None:
        self._authentication_providers = authentication_providers

        self.create = async_to_streamed_response_wrapper(
            authentication_providers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            authentication_providers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            authentication_providers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            authentication_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            authentication_providers.delete,
        )
