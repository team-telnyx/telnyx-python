# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
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
from ...types.bundle_pricing import user_bundle_list_params, user_bundle_create_params, user_bundle_list_unused_params
from ...types.bundle_pricing.user_bundle import UserBundle
from ...types.bundle_pricing.user_bundle_create_response import UserBundleCreateResponse
from ...types.bundle_pricing.user_bundle_retrieve_response import UserBundleRetrieveResponse
from ...types.bundle_pricing.user_bundle_deactivate_response import UserBundleDeactivateResponse
from ...types.bundle_pricing.user_bundle_list_unused_response import UserBundleListUnusedResponse
from ...types.bundle_pricing.user_bundle_list_resources_response import UserBundleListResourcesResponse

__all__ = ["UserBundlesResource", "AsyncUserBundlesResource"]


class UserBundlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserBundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UserBundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserBundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UserBundlesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        idempotency_key: str | Omit = omit,
        items: Iterable[user_bundle_create_params.Item] | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleCreateResponse:
        """
        Creates multiple user bundles for the user.

        Args:
          idempotency_key: Idempotency key for the request. Can be any UUID, but should always be unique
              for each request.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._post(
            "/bundle_pricing/user_bundles/bulk",
            body=maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "items": items,
                },
                user_bundle_create_params.UserBundleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleCreateResponse,
        )

    def retrieve(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleRetrieveResponse:
        """
        Retrieves a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            f"/bundle_pricing/user_bundles/{user_bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: user_bundle_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[UserBundle]:
        """
        Get a paginated list of user bundles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get_api_list(
            "/bundle_pricing/user_bundles",
            page=SyncDefaultFlatPagination[UserBundle],
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
                    user_bundle_list_params.UserBundleListParams,
                ),
            ),
            model=UserBundle,
        )

    def deactivate(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleDeactivateResponse:
        """
        Deactivates a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._delete(
            f"/bundle_pricing/user_bundles/{user_bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleDeactivateResponse,
        )

    def list_resources(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleListResourcesResponse:
        """
        Retrieves the resources of a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            f"/bundle_pricing/user_bundles/{user_bundle_id}/resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleListResourcesResponse,
        )

    def list_unused(
        self,
        *,
        filter: user_bundle_list_unused_params.Filter | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleListUnusedResponse:
        """
        Returns all user bundles that aren't in use.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get(
            "/bundle_pricing/user_bundles/unused",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, user_bundle_list_unused_params.UserBundleListUnusedParams),
            ),
            cast_to=UserBundleListUnusedResponse,
        )


class AsyncUserBundlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserBundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserBundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserBundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUserBundlesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        idempotency_key: str | Omit = omit,
        items: Iterable[user_bundle_create_params.Item] | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleCreateResponse:
        """
        Creates multiple user bundles for the user.

        Args:
          idempotency_key: Idempotency key for the request. Can be any UUID, but should always be unique
              for each request.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._post(
            "/bundle_pricing/user_bundles/bulk",
            body=await async_maybe_transform(
                {
                    "idempotency_key": idempotency_key,
                    "items": items,
                },
                user_bundle_create_params.UserBundleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleCreateResponse,
        )

    async def retrieve(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleRetrieveResponse:
        """
        Retrieves a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            f"/bundle_pricing/user_bundles/{user_bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: user_bundle_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserBundle, AsyncDefaultFlatPagination[UserBundle]]:
        """
        Get a paginated list of user bundles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return self._get_api_list(
            "/bundle_pricing/user_bundles",
            page=AsyncDefaultFlatPagination[UserBundle],
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
                    user_bundle_list_params.UserBundleListParams,
                ),
            ),
            model=UserBundle,
        )

    async def deactivate(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleDeactivateResponse:
        """
        Deactivates a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._delete(
            f"/bundle_pricing/user_bundles/{user_bundle_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleDeactivateResponse,
        )

    async def list_resources(
        self,
        user_bundle_id: str,
        *,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleListResourcesResponse:
        """
        Retrieves the resources of a user bundle by its ID.

        Args:
          user_bundle_id: User bundle's ID, this is used to identify the user bundle in the API.

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not user_bundle_id:
            raise ValueError(f"Expected a non-empty value for `user_bundle_id` but received {user_bundle_id!r}")
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            f"/bundle_pricing/user_bundles/{user_bundle_id}/resources",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserBundleListResourcesResponse,
        )

    async def list_unused(
        self,
        *,
        filter: user_bundle_list_unused_params.Filter | Omit = omit,
        authorization_bearer: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserBundleListUnusedResponse:
        """
        Returns all user bundles that aren't in use.

        Args:
          filter: Consolidated filter parameter (deepObject style). Supports filtering by
              country_iso and resource. Examples: filter[country_iso]=US or
              filter[resource]=+15617819942

          authorization_bearer: Authenticates the request with your Telnyx API V2 KEY

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"authorization_bearer": authorization_bearer}), **(extra_headers or {})}
        return await self._get(
            "/bundle_pricing/user_bundles/unused",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"filter": filter}, user_bundle_list_unused_params.UserBundleListUnusedParams
                ),
            ),
            cast_to=UserBundleListUnusedResponse,
        )


class UserBundlesResourceWithRawResponse:
    def __init__(self, user_bundles: UserBundlesResource) -> None:
        self._user_bundles = user_bundles

        self.create = to_raw_response_wrapper(
            user_bundles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            user_bundles.retrieve,
        )
        self.list = to_raw_response_wrapper(
            user_bundles.list,
        )
        self.deactivate = to_raw_response_wrapper(
            user_bundles.deactivate,
        )
        self.list_resources = to_raw_response_wrapper(
            user_bundles.list_resources,
        )
        self.list_unused = to_raw_response_wrapper(
            user_bundles.list_unused,
        )


class AsyncUserBundlesResourceWithRawResponse:
    def __init__(self, user_bundles: AsyncUserBundlesResource) -> None:
        self._user_bundles = user_bundles

        self.create = async_to_raw_response_wrapper(
            user_bundles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            user_bundles.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            user_bundles.list,
        )
        self.deactivate = async_to_raw_response_wrapper(
            user_bundles.deactivate,
        )
        self.list_resources = async_to_raw_response_wrapper(
            user_bundles.list_resources,
        )
        self.list_unused = async_to_raw_response_wrapper(
            user_bundles.list_unused,
        )


class UserBundlesResourceWithStreamingResponse:
    def __init__(self, user_bundles: UserBundlesResource) -> None:
        self._user_bundles = user_bundles

        self.create = to_streamed_response_wrapper(
            user_bundles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            user_bundles.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            user_bundles.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            user_bundles.deactivate,
        )
        self.list_resources = to_streamed_response_wrapper(
            user_bundles.list_resources,
        )
        self.list_unused = to_streamed_response_wrapper(
            user_bundles.list_unused,
        )


class AsyncUserBundlesResourceWithStreamingResponse:
    def __init__(self, user_bundles: AsyncUserBundlesResource) -> None:
        self._user_bundles = user_bundles

        self.create = async_to_streamed_response_wrapper(
            user_bundles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            user_bundles.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            user_bundles.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            user_bundles.deactivate,
        )
        self.list_resources = async_to_streamed_response_wrapper(
            user_bundles.list_resources,
        )
        self.list_unused = async_to_streamed_response_wrapper(
            user_bundles.list_unused,
        )
