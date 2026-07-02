# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.kvs import key_set_params, key_list_params
from ....types.storage.kvs.key_list_response import KeyListResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    """Read and write keys within a KV namespace"""

    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def retrieve(
        self,
        key: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Returns the raw stored value for a key.

        The response body is the value exactly
        as it was written; the `Content-Type` header echoes the value's stored content
        type (defaults to `application/octet-stream`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Lists the keys in a namespace.

        Returns key names and metadata only, never
        values. Results are paginated with `limit` and an opaque `cursor`.

        Args:
          cursor: Opaque pagination cursor from a previous response's `meta.cursor`.

          limit: Maximum number of keys to return. Values above 1000 are treated as 1000.

          prefix: Return only keys that start with this prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/storage/kvs/{id}/keys", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
        )

    def delete(
        self,
        key: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a key.

        Idempotent: deleting a key that does not exist still succeeds.
        The namespace itself must exist and be provisioned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set(
        self,
        key: str,
        *,
        id: str,
        body: FileTypes,
        ttl_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates or replaces the value for a key.

        The request body is stored verbatim as
        the value — no base64, no JSON envelope — up to 1 MiB. The request's
        `Content-Type` header is stored with the value and echoed back on retrieval.
        Returns `201` when the key is created and `200` when an existing key is updated.

        Args:
          body: Raw value bytes, stored verbatim.

          ttl_secs: Time-to-live in seconds. When set, the key expires and is deleted after this
              duration. Requires a namespace provisioned with TTL support; namespaces without
              it return a `409`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            body=maybe_transform(body, key_set_params.KeySetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ttl_secs": ttl_secs}, key_set_params.KeySetParams),
            ),
            cast_to=NoneType,
        )


class AsyncKeysResource(AsyncAPIResource):
    """Read and write keys within a KV namespace"""

    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        key: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Returns the raw stored value for a key.

        The response body is the value exactly
        as it was written; the `Content-Type` header echoes the value's stored content
        type (defaults to `application/octet-stream`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
        self,
        id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """Lists the keys in a namespace.

        Returns key names and metadata only, never
        values. Results are paginated with `limit` and an opaque `cursor`.

        Args:
          cursor: Opaque pagination cursor from a previous response's `meta.cursor`.

          limit: Maximum number of keys to return. Values above 1000 are treated as 1000.

          prefix: Return only keys that start with this prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/storage/kvs/{id}/keys", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "prefix": prefix,
                    },
                    key_list_params.KeyListParams,
                ),
            ),
            cast_to=KeyListResponse,
        )

    async def delete(
        self,
        key: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a key.

        Idempotent: deleting a key that does not exist still succeeds.
        The namespace itself must exist and be provisioned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set(
        self,
        key: str,
        *,
        id: str,
        body: FileTypes,
        ttl_secs: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates or replaces the value for a key.

        The request body is stored verbatim as
        the value — no base64, no JSON envelope — up to 1 MiB. The request's
        `Content-Type` header is stored with the value and echoed back on retrieval.
        Returns `201` when the key is created and `200` when an existing key is updated.

        Args:
          body: Raw value bytes, stored verbatim.

          ttl_secs: Time-to-live in seconds. When set, the key expires and is deleted after this
              duration. Requires a namespace provisioned with TTL support; namespaces without
              it return a `409`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not key:
            raise ValueError(f"Expected a non-empty value for `key` but received {key!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            path_template("/storage/kvs/{id}/keys/{key}", id=id, key=key),
            body=await async_maybe_transform(body, key_set_params.KeySetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ttl_secs": ttl_secs}, key_set_params.KeySetParams),
            ),
            cast_to=NoneType,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.retrieve = to_custom_raw_response_wrapper(
            keys.retrieve,
            BinaryAPIResponse,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.delete = to_raw_response_wrapper(
            keys.delete,
        )
        self.set = to_raw_response_wrapper(
            keys.set,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.retrieve = async_to_custom_raw_response_wrapper(
            keys.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.delete = async_to_raw_response_wrapper(
            keys.delete,
        )
        self.set = async_to_raw_response_wrapper(
            keys.set,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.retrieve = to_custom_streamed_response_wrapper(
            keys.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = to_streamed_response_wrapper(
            keys.delete,
        )
        self.set = to_streamed_response_wrapper(
            keys.set,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.retrieve = async_to_custom_streamed_response_wrapper(
            keys.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            keys.delete,
        )
        self.set = async_to_streamed_response_wrapper(
            keys.set,
        )
