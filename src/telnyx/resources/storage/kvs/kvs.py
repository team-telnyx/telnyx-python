# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.storage import kv_list_params, kv_create_params
from ....types.storage.kv_namespace import KvNamespace
from ....types.storage.kv_namespace_response_wrapper import KvNamespaceResponseWrapper

__all__ = ["KvsResource", "AsyncKvsResource"]


class KvsResource(SyncAPIResource):
    """Manage KV storage namespaces"""

    @cached_property
    def keys(self) -> KeysResource:
        """Read and write keys within a KV namespace"""
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> KvsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return KvsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KvsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return KvsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvNamespaceResponseWrapper:
        """Creates a new KV namespace.

        Provisioning is asynchronous: the namespace is
        returned with status `pending` and becomes usable once it reaches
        `provision_ok`.

        Args:
          name: Namespace name. May contain lowercase letters, numbers, and hyphens only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/storage/kvs",
            body=maybe_transform({"name": name}, kv_create_params.KvCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
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
    ) -> KvNamespaceResponseWrapper:
        """
        Retrieves a KV namespace by its ID, including its provisioning status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/storage/kvs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
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
    ) -> SyncDefaultFlatPagination[KvNamespace]:
        """Lists the KV namespaces for the authenticated user's organization.

        Results use
        page-based pagination (`page[number]`/`page[size]`).

        Args:
          page_number: The page number to load.

          page_size: The size of the page. Values above 250 are treated as 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/kvs",
            page=SyncDefaultFlatPagination[KvNamespace],
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
                    kv_list_params.KvListParams,
                ),
            ),
            model=KvNamespace,
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
    ) -> KvNamespaceResponseWrapper:
        """Deletes a KV namespace and all of the keys it contains.

        Deletion is
        asynchronous: the namespace is returned with status `deleting`. Deleting a
        namespace whose deletion is already in progress returns a `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/storage/kvs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
        )


class AsyncKvsResource(AsyncAPIResource):
    """Manage KV storage namespaces"""

    @cached_property
    def keys(self) -> AsyncKeysResource:
        """Read and write keys within a KV namespace"""
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncKvsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKvsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKvsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncKvsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KvNamespaceResponseWrapper:
        """Creates a new KV namespace.

        Provisioning is asynchronous: the namespace is
        returned with status `pending` and becomes usable once it reaches
        `provision_ok`.

        Args:
          name: Namespace name. May contain lowercase letters, numbers, and hyphens only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/storage/kvs",
            body=await async_maybe_transform({"name": name}, kv_create_params.KvCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
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
    ) -> KvNamespaceResponseWrapper:
        """
        Retrieves a KV namespace by its ID, including its provisioning status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/storage/kvs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
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
    ) -> AsyncPaginator[KvNamespace, AsyncDefaultFlatPagination[KvNamespace]]:
        """Lists the KV namespaces for the authenticated user's organization.

        Results use
        page-based pagination (`page[number]`/`page[size]`).

        Args:
          page_number: The page number to load.

          page_size: The size of the page. Values above 250 are treated as 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/storage/kvs",
            page=AsyncDefaultFlatPagination[KvNamespace],
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
                    kv_list_params.KvListParams,
                ),
            ),
            model=KvNamespace,
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
    ) -> KvNamespaceResponseWrapper:
        """Deletes a KV namespace and all of the keys it contains.

        Deletion is
        asynchronous: the namespace is returned with status `deleting`. Deleting a
        namespace whose deletion is already in progress returns a `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/storage/kvs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KvNamespaceResponseWrapper,
        )


class KvsResourceWithRawResponse:
    def __init__(self, kvs: KvsResource) -> None:
        self._kvs = kvs

        self.create = to_raw_response_wrapper(
            kvs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            kvs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            kvs.list,
        )
        self.delete = to_raw_response_wrapper(
            kvs.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        """Read and write keys within a KV namespace"""
        return KeysResourceWithRawResponse(self._kvs.keys)


class AsyncKvsResourceWithRawResponse:
    def __init__(self, kvs: AsyncKvsResource) -> None:
        self._kvs = kvs

        self.create = async_to_raw_response_wrapper(
            kvs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            kvs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            kvs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            kvs.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        """Read and write keys within a KV namespace"""
        return AsyncKeysResourceWithRawResponse(self._kvs.keys)


class KvsResourceWithStreamingResponse:
    def __init__(self, kvs: KvsResource) -> None:
        self._kvs = kvs

        self.create = to_streamed_response_wrapper(
            kvs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            kvs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            kvs.list,
        )
        self.delete = to_streamed_response_wrapper(
            kvs.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        """Read and write keys within a KV namespace"""
        return KeysResourceWithStreamingResponse(self._kvs.keys)


class AsyncKvsResourceWithStreamingResponse:
    def __init__(self, kvs: AsyncKvsResource) -> None:
        self._kvs = kvs

        self.create = async_to_streamed_response_wrapper(
            kvs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            kvs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            kvs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            kvs.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        """Read and write keys within a KV namespace"""
        return AsyncKeysResourceWithStreamingResponse(self._kvs.keys)
