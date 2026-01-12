# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import oauth_client_list_params, oauth_client_create_params, oauth_client_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.oauth_client import OAuthClient
from ..types.oauth_client_create_response import OAuthClientCreateResponse
from ..types.oauth_client_update_response import OAuthClientUpdateResponse
from ..types.oauth_client_retrieve_response import OAuthClientRetrieveResponse

__all__ = ["OAuthClientsResource", "AsyncOAuthClientsResource"]


class OAuthClientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OAuthClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OAuthClientsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allowed_grant_types: List[Literal["client_credentials", "authorization_code", "refresh_token"]],
        allowed_scopes: SequenceNotStr[str],
        client_type: Literal["public", "confidential"],
        name: str,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        require_pkce: bool | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthClientCreateResponse:
        """
        Create a new OAuth client

        Args:
          allowed_grant_types: List of allowed OAuth grant types

          allowed_scopes: List of allowed OAuth scopes

          client_type: OAuth client type

          name: The name of the OAuth client

          logo_uri: URL of the client logo

          policy_uri: URL of the client's privacy policy

          redirect_uris: List of redirect URIs (required for authorization_code flow)

          require_pkce: Whether PKCE (Proof Key for Code Exchange) is required for this client

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/oauth_clients",
            body=maybe_transform(
                {
                    "allowed_grant_types": allowed_grant_types,
                    "allowed_scopes": allowed_scopes,
                    "client_type": client_type,
                    "name": name,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "require_pkce": require_pkce,
                    "tos_uri": tos_uri,
                },
                oauth_client_create_params.OAuthClientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientCreateResponse,
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
    ) -> OAuthClientRetrieveResponse:
        """
        Retrieve a single OAuth client by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/oauth_clients/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        allowed_grant_types: List[Literal["client_credentials", "authorization_code", "refresh_token"]] | Omit = omit,
        allowed_scopes: SequenceNotStr[str] | Omit = omit,
        logo_uri: str | Omit = omit,
        name: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        require_pkce: bool | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthClientUpdateResponse:
        """
        Update an existing OAuth client

        Args:
          allowed_grant_types: List of allowed OAuth grant types

          allowed_scopes: List of allowed OAuth scopes

          logo_uri: URL of the client logo

          name: The name of the OAuth client

          policy_uri: URL of the client's privacy policy

          redirect_uris: List of redirect URIs

          require_pkce: Whether PKCE (Proof Key for Code Exchange) is required for this client

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/oauth_clients/{id}",
            body=maybe_transform(
                {
                    "allowed_grant_types": allowed_grant_types,
                    "allowed_scopes": allowed_scopes,
                    "logo_uri": logo_uri,
                    "name": name,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "require_pkce": require_pkce,
                    "tos_uri": tos_uri,
                },
                oauth_client_update_params.OAuthClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientUpdateResponse,
        )

    def list(
        self,
        *,
        filter_allowed_grant_types_contains: Literal["client_credentials", "authorization_code", "refresh_token"]
        | Omit = omit,
        filter_client_id: str | Omit = omit,
        filter_client_type: Literal["confidential", "public"] | Omit = omit,
        filter_name: str | Omit = omit,
        filter_name_contains: str | Omit = omit,
        filter_verified: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[OAuthClient]:
        """
        Retrieve a paginated list of OAuth clients for the authenticated user

        Args:
          filter_allowed_grant_types_contains: Filter by allowed grant type

          filter_client_id: Filter by client ID

          filter_client_type: Filter by client type

          filter_name: Filter by exact client name

          filter_name_contains: Filter by client name containing text

          filter_verified: Filter by verification status

          page_number: Page number

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_clients",
            page=SyncDefaultFlatPagination[OAuthClient],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_allowed_grant_types_contains": filter_allowed_grant_types_contains,
                        "filter_client_id": filter_client_id,
                        "filter_client_type": filter_client_type,
                        "filter_name": filter_name,
                        "filter_name_contains": filter_name_contains,
                        "filter_verified": filter_verified,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    oauth_client_list_params.OAuthClientListParams,
                ),
            ),
            model=OAuthClient,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an OAuth client

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
            f"/oauth_clients/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOAuthClientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthClientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthClientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthClientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOAuthClientsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allowed_grant_types: List[Literal["client_credentials", "authorization_code", "refresh_token"]],
        allowed_scopes: SequenceNotStr[str],
        client_type: Literal["public", "confidential"],
        name: str,
        logo_uri: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        require_pkce: bool | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthClientCreateResponse:
        """
        Create a new OAuth client

        Args:
          allowed_grant_types: List of allowed OAuth grant types

          allowed_scopes: List of allowed OAuth scopes

          client_type: OAuth client type

          name: The name of the OAuth client

          logo_uri: URL of the client logo

          policy_uri: URL of the client's privacy policy

          redirect_uris: List of redirect URIs (required for authorization_code flow)

          require_pkce: Whether PKCE (Proof Key for Code Exchange) is required for this client

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/oauth_clients",
            body=await async_maybe_transform(
                {
                    "allowed_grant_types": allowed_grant_types,
                    "allowed_scopes": allowed_scopes,
                    "client_type": client_type,
                    "name": name,
                    "logo_uri": logo_uri,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "require_pkce": require_pkce,
                    "tos_uri": tos_uri,
                },
                oauth_client_create_params.OAuthClientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientCreateResponse,
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
    ) -> OAuthClientRetrieveResponse:
        """
        Retrieve a single OAuth client by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/oauth_clients/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        allowed_grant_types: List[Literal["client_credentials", "authorization_code", "refresh_token"]] | Omit = omit,
        allowed_scopes: SequenceNotStr[str] | Omit = omit,
        logo_uri: str | Omit = omit,
        name: str | Omit = omit,
        policy_uri: str | Omit = omit,
        redirect_uris: SequenceNotStr[str] | Omit = omit,
        require_pkce: bool | Omit = omit,
        tos_uri: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthClientUpdateResponse:
        """
        Update an existing OAuth client

        Args:
          allowed_grant_types: List of allowed OAuth grant types

          allowed_scopes: List of allowed OAuth scopes

          logo_uri: URL of the client logo

          name: The name of the OAuth client

          policy_uri: URL of the client's privacy policy

          redirect_uris: List of redirect URIs

          require_pkce: Whether PKCE (Proof Key for Code Exchange) is required for this client

          tos_uri: URL of the client's terms of service

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/oauth_clients/{id}",
            body=await async_maybe_transform(
                {
                    "allowed_grant_types": allowed_grant_types,
                    "allowed_scopes": allowed_scopes,
                    "logo_uri": logo_uri,
                    "name": name,
                    "policy_uri": policy_uri,
                    "redirect_uris": redirect_uris,
                    "require_pkce": require_pkce,
                    "tos_uri": tos_uri,
                },
                oauth_client_update_params.OAuthClientUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthClientUpdateResponse,
        )

    def list(
        self,
        *,
        filter_allowed_grant_types_contains: Literal["client_credentials", "authorization_code", "refresh_token"]
        | Omit = omit,
        filter_client_id: str | Omit = omit,
        filter_client_type: Literal["confidential", "public"] | Omit = omit,
        filter_name: str | Omit = omit,
        filter_name_contains: str | Omit = omit,
        filter_verified: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[OAuthClient, AsyncDefaultFlatPagination[OAuthClient]]:
        """
        Retrieve a paginated list of OAuth clients for the authenticated user

        Args:
          filter_allowed_grant_types_contains: Filter by allowed grant type

          filter_client_id: Filter by client ID

          filter_client_type: Filter by client type

          filter_name: Filter by exact client name

          filter_name_contains: Filter by client name containing text

          filter_verified: Filter by verification status

          page_number: Page number

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_clients",
            page=AsyncDefaultFlatPagination[OAuthClient],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_allowed_grant_types_contains": filter_allowed_grant_types_contains,
                        "filter_client_id": filter_client_id,
                        "filter_client_type": filter_client_type,
                        "filter_name": filter_name,
                        "filter_name_contains": filter_name_contains,
                        "filter_verified": filter_verified,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    oauth_client_list_params.OAuthClientListParams,
                ),
            ),
            model=OAuthClient,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an OAuth client

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
            f"/oauth_clients/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OAuthClientsResourceWithRawResponse:
    def __init__(self, oauth_clients: OAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = to_raw_response_wrapper(
            oauth_clients.create,
        )
        self.retrieve = to_raw_response_wrapper(
            oauth_clients.retrieve,
        )
        self.update = to_raw_response_wrapper(
            oauth_clients.update,
        )
        self.list = to_raw_response_wrapper(
            oauth_clients.list,
        )
        self.delete = to_raw_response_wrapper(
            oauth_clients.delete,
        )


class AsyncOAuthClientsResourceWithRawResponse:
    def __init__(self, oauth_clients: AsyncOAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = async_to_raw_response_wrapper(
            oauth_clients.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            oauth_clients.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            oauth_clients.update,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_clients.list,
        )
        self.delete = async_to_raw_response_wrapper(
            oauth_clients.delete,
        )


class OAuthClientsResourceWithStreamingResponse:
    def __init__(self, oauth_clients: OAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = to_streamed_response_wrapper(
            oauth_clients.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            oauth_clients.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            oauth_clients.update,
        )
        self.list = to_streamed_response_wrapper(
            oauth_clients.list,
        )
        self.delete = to_streamed_response_wrapper(
            oauth_clients.delete,
        )


class AsyncOAuthClientsResourceWithStreamingResponse:
    def __init__(self, oauth_clients: AsyncOAuthClientsResource) -> None:
        self._oauth_clients = oauth_clients

        self.create = async_to_streamed_response_wrapper(
            oauth_clients.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            oauth_clients.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            oauth_clients.update,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_clients.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            oauth_clients.delete,
        )
