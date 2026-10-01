# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .profiles.profiles import (
    ProfilesResource,
    AsyncProfilesResource,
    ProfilesResourceWithRawResponse,
    AsyncProfilesResourceWithRawResponse,
    ProfilesResourceWithStreamingResponse,
    AsyncProfilesResourceWithStreamingResponse,
)
from .....types.ai.memory import namespace_create_params
from .....types.ai.memory.namespace_list_response import NamespaceListResponse
from .....types.ai.memory.namespace_create_response import NamespaceCreateResponse
from .....types.ai.memory.namespace_retrieve_response import NamespaceRetrieveResponse

__all__ = ["NamespacesResource", "AsyncNamespacesResource"]


class NamespacesResource(SyncAPIResource):
    @cached_property
    def profiles(self) -> ProfilesResource:
        return ProfilesResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """How a namespace's summaries are written."""
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return NamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return NamespacesResourceWithStreamingResponse(self)

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
    ) -> NamespaceCreateResponse:
        """Create a namespace.

        An organization can have at most five, `default` among them
        — a sixth returns `403`.

        Args:
          name: A name for the new namespace, unique within your organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/memory/namespaces",
            body=maybe_transform({"name": name}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceCreateResponse,
        )

    def retrieve(
        self,
        operation_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceRetrieveResponse:
        """Whether a write has finished.

        Both `ingest` and `remember` return an
        `operation_id`, and a memory is not recallable until its operation completes —
        extraction, embedding and consolidation all run first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/operations/{operation_id}",
                namespace=namespace,
                operation_id=operation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """Every namespace in your organization, `default` among them."""
        return self._get(
            "/ai/memory/namespaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceListResponse,
        )

    def delete(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a namespace and every profile and memory in it.

        `default` cannot be
        deleted. This cannot be undone.

        Args:
          namespace: The namespace to delete. `default` cannot be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/ai/memory/namespaces/{namespace}", namespace=namespace),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncNamespacesResource(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        return AsyncProfilesResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """How a namespace's summaries are written."""
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamespacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncNamespacesResourceWithStreamingResponse(self)

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
    ) -> NamespaceCreateResponse:
        """Create a namespace.

        An organization can have at most five, `default` among them
        — a sixth returns `403`.

        Args:
          name: A name for the new namespace, unique within your organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/memory/namespaces",
            body=await async_maybe_transform({"name": name}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceCreateResponse,
        )

    async def retrieve(
        self,
        operation_id: str,
        *,
        namespace: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceRetrieveResponse:
        """Whether a write has finished.

        Both `ingest` and `remember` return an
        `operation_id`, and a memory is not recallable until its operation completes —
        extraction, embedding and consolidation all run first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            path_template(
                "/ai/memory/namespaces/{namespace}/operations/{operation_id}",
                namespace=namespace,
                operation_id=operation_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamespaceListResponse:
        """Every namespace in your organization, `default` among them."""
        return await self._get(
            "/ai/memory/namespaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamespaceListResponse,
        )

    async def delete(
        self,
        namespace: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a namespace and every profile and memory in it.

        `default` cannot be
        deleted. This cannot be undone.

        Args:
          namespace: The namespace to delete. `default` cannot be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not namespace:
            raise ValueError(f"Expected a non-empty value for `namespace` but received {namespace!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/ai/memory/namespaces/{namespace}", namespace=namespace),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class NamespacesResourceWithRawResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_raw_response_wrapper(
            namespaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            namespaces.retrieve,
        )
        self.list = to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            namespaces.delete,
        )

    @cached_property
    def profiles(self) -> ProfilesResourceWithRawResponse:
        return ProfilesResourceWithRawResponse(self._namespaces.profiles)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """How a namespace's summaries are written."""
        return SettingsResourceWithRawResponse(self._namespaces.settings)


class AsyncNamespacesResourceWithRawResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_raw_response_wrapper(
            namespaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            namespaces.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            namespaces.delete,
        )

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithRawResponse:
        return AsyncProfilesResourceWithRawResponse(self._namespaces.profiles)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """How a namespace's summaries are written."""
        return AsyncSettingsResourceWithRawResponse(self._namespaces.settings)


class NamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: NamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = to_streamed_response_wrapper(
            namespaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            namespaces.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            namespaces.delete,
        )

    @cached_property
    def profiles(self) -> ProfilesResourceWithStreamingResponse:
        return ProfilesResourceWithStreamingResponse(self._namespaces.profiles)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """How a namespace's summaries are written."""
        return SettingsResourceWithStreamingResponse(self._namespaces.settings)


class AsyncNamespacesResourceWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespacesResource) -> None:
        self._namespaces = namespaces

        self.create = async_to_streamed_response_wrapper(
            namespaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            namespaces.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            namespaces.delete,
        )

    @cached_property
    def profiles(self) -> AsyncProfilesResourceWithStreamingResponse:
        return AsyncProfilesResourceWithStreamingResponse(self._namespaces.profiles)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """How a namespace's summaries are written."""
        return AsyncSettingsResourceWithStreamingResponse(self._namespaces.settings)
