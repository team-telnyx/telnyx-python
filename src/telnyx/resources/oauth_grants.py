# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import oauth_grant_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
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
from ..types.oauth_grant import OAuthGrant
from ..types.oauth_grant_delete_response import OAuthGrantDeleteResponse
from ..types.oauth_grant_retrieve_response import OAuthGrantRetrieveResponse

__all__ = ["OAuthGrantsResource", "AsyncOAuthGrantsResource"]


class OAuthGrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return OAuthGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return OAuthGrantsResourceWithStreamingResponse(self)

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
    ) -> OAuthGrantRetrieveResponse:
        """
        Retrieve a single OAuth grant by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/oauth_grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantRetrieveResponse,
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
    ) -> SyncDefaultFlatPagination[OAuthGrant]:
        """
        Retrieve a paginated list of OAuth grants for the authenticated user

        Args:
          page_number: Page number

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_grants",
            page=SyncDefaultFlatPagination[OAuthGrant],
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
                    oauth_grant_list_params.OAuthGrantListParams,
                ),
            ),
            model=OAuthGrant,
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
    ) -> OAuthGrantDeleteResponse:
        """
        Revoke an OAuth grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/oauth_grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantDeleteResponse,
        )


class AsyncOAuthGrantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncOAuthGrantsResourceWithStreamingResponse(self)

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
    ) -> OAuthGrantRetrieveResponse:
        """
        Retrieve a single OAuth grant by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/oauth_grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantRetrieveResponse,
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
    ) -> AsyncPaginator[OAuthGrant, AsyncDefaultFlatPagination[OAuthGrant]]:
        """
        Retrieve a paginated list of OAuth grants for the authenticated user

        Args:
          page_number: Page number

          page_size: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/oauth_grants",
            page=AsyncDefaultFlatPagination[OAuthGrant],
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
                    oauth_grant_list_params.OAuthGrantListParams,
                ),
            ),
            model=OAuthGrant,
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
    ) -> OAuthGrantDeleteResponse:
        """
        Revoke an OAuth grant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/oauth_grants/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OAuthGrantDeleteResponse,
        )


class OAuthGrantsResourceWithRawResponse:
    def __init__(self, oauth_grants: OAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.retrieve = to_raw_response_wrapper(
            oauth_grants.retrieve,
        )
        self.list = to_raw_response_wrapper(
            oauth_grants.list,
        )
        self.delete = to_raw_response_wrapper(
            oauth_grants.delete,
        )


class AsyncOAuthGrantsResourceWithRawResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.retrieve = async_to_raw_response_wrapper(
            oauth_grants.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            oauth_grants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            oauth_grants.delete,
        )


class OAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: OAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.retrieve = to_streamed_response_wrapper(
            oauth_grants.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            oauth_grants.list,
        )
        self.delete = to_streamed_response_wrapper(
            oauth_grants.delete,
        )


class AsyncOAuthGrantsResourceWithStreamingResponse:
    def __init__(self, oauth_grants: AsyncOAuthGrantsResource) -> None:
        self._oauth_grants = oauth_grants

        self.retrieve = async_to_streamed_response_wrapper(
            oauth_grants.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            oauth_grants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            oauth_grants.delete,
        )
