# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import browser_session_list_params, browser_session_create_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browser_session_list_response import BrowserSessionListResponse
from ...types.browser_session_create_response import BrowserSessionCreateResponse
from ...types.browser_session_delete_response import BrowserSessionDeleteResponse
from ...types.browser_session_retrieve_response import BrowserSessionRetrieveResponse
from ...types.browser_session_retrieve_artifact_response import BrowserSessionRetrieveArtifactResponse

__all__ = ["BrowserSessionsResource", "AsyncBrowserSessionsResource"]


class BrowserSessionsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrowserSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrowserSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BrowserSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        policy: browser_session_create_params.Policy,
        idempotency_key: str | Omit = omit,
        limits: browser_session_create_params.Limits | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionCreateResponse:
        """
        Creates an isolated browser session with network access restricted to the
        domains you allow.

        Args:
          idempotency_key: Scoped to the organization. The same key and identical normalized policy,
              limits, and metadata replay the existing session (HTTP 201); a different request
              returns 409 idempotency_conflict. Replays do not restart terminal sessions.

          metadata: Arbitrary key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/browser_sessions",
            body=maybe_transform(
                {
                    "policy": policy,
                    "idempotency_key": idempotency_key,
                    "limits": limits,
                    "metadata": metadata,
                },
                browser_session_create_params.BrowserSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionCreateResponse,
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
    ) -> BrowserSessionRetrieveResponse:
        """
        Returns the current status of a browser session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/browser_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionRetrieveResponse,
        )

    def list(
        self,
        *,
        status: Literal["provisioning", "ready", "closing", "closed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionListResponse:
        """Lists sessions for the authenticated org.

        Optional status filter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/browser_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, browser_session_list_params.BrowserSessionListParams),
            ),
            cast_to=BrowserSessionListResponse,
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
    ) -> BrowserSessionDeleteResponse:
        """Closes a ready session and releases its resources.

        An already closed, failed, or
        expired session is returned unchanged; a provisioning session returns 409
        session_not_ready.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/browser_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionDeleteResponse,
        )

    def retrieve_artifact(
        self,
        artifact_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionRetrieveArtifactResponse:
        """Returns artifact metadata and a signed download URL.

        The download URL requires
        Bearer auth.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return self._get(
            path_template("/browser_sessions/{id}/artifacts/{artifact_id}", id=id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionRetrieveArtifactResponse,
        )


class AsyncBrowserSessionsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrowserSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrowserSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrowserSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBrowserSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        policy: browser_session_create_params.Policy,
        idempotency_key: str | Omit = omit,
        limits: browser_session_create_params.Limits | Omit = omit,
        metadata: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionCreateResponse:
        """
        Creates an isolated browser session with network access restricted to the
        domains you allow.

        Args:
          idempotency_key: Scoped to the organization. The same key and identical normalized policy,
              limits, and metadata replay the existing session (HTTP 201); a different request
              returns 409 idempotency_conflict. Replays do not restart terminal sessions.

          metadata: Arbitrary key-value metadata.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/browser_sessions",
            body=await async_maybe_transform(
                {
                    "policy": policy,
                    "idempotency_key": idempotency_key,
                    "limits": limits,
                    "metadata": metadata,
                },
                browser_session_create_params.BrowserSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionCreateResponse,
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
    ) -> BrowserSessionRetrieveResponse:
        """
        Returns the current status of a browser session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/browser_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionRetrieveResponse,
        )

    async def list(
        self,
        *,
        status: Literal["provisioning", "ready", "closing", "closed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionListResponse:
        """Lists sessions for the authenticated org.

        Optional status filter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/browser_sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status}, browser_session_list_params.BrowserSessionListParams
                ),
            ),
            cast_to=BrowserSessionListResponse,
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
    ) -> BrowserSessionDeleteResponse:
        """Closes a ready session and releases its resources.

        An already closed, failed, or
        expired session is returned unchanged; a provisioning session returns 409
        session_not_ready.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/browser_sessions/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionDeleteResponse,
        )

    async def retrieve_artifact(
        self,
        artifact_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrowserSessionRetrieveArtifactResponse:
        """Returns artifact metadata and a signed download URL.

        The download URL requires
        Bearer auth.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return await self._get(
            path_template("/browser_sessions/{id}/artifacts/{artifact_id}", id=id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrowserSessionRetrieveArtifactResponse,
        )


class BrowserSessionsResourceWithRawResponse:
    def __init__(self, browser_sessions: BrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

        self.create = to_raw_response_wrapper(
            browser_sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            browser_sessions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            browser_sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            browser_sessions.delete,
        )
        self.retrieve_artifact = to_raw_response_wrapper(
            browser_sessions.retrieve_artifact,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return ActionsResourceWithRawResponse(self._browser_sessions.actions)


class AsyncBrowserSessionsResourceWithRawResponse:
    def __init__(self, browser_sessions: AsyncBrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

        self.create = async_to_raw_response_wrapper(
            browser_sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            browser_sessions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            browser_sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            browser_sessions.delete,
        )
        self.retrieve_artifact = async_to_raw_response_wrapper(
            browser_sessions.retrieve_artifact,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return AsyncActionsResourceWithRawResponse(self._browser_sessions.actions)


class BrowserSessionsResourceWithStreamingResponse:
    def __init__(self, browser_sessions: BrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

        self.create = to_streamed_response_wrapper(
            browser_sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            browser_sessions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            browser_sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            browser_sessions.delete,
        )
        self.retrieve_artifact = to_streamed_response_wrapper(
            browser_sessions.retrieve_artifact,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return ActionsResourceWithStreamingResponse(self._browser_sessions.actions)


class AsyncBrowserSessionsResourceWithStreamingResponse:
    def __init__(self, browser_sessions: AsyncBrowserSessionsResource) -> None:
        self._browser_sessions = browser_sessions

        self.create = async_to_streamed_response_wrapper(
            browser_sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            browser_sessions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            browser_sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            browser_sessions.delete,
        )
        self.retrieve_artifact = async_to_streamed_response_wrapper(
            browser_sessions.retrieve_artifact,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Execute browser actions: navigate, observe, click, fill, select, press, scroll, wait_for, screenshot, batch.
        """
        return AsyncActionsResourceWithStreamingResponse(self._browser_sessions.actions)
