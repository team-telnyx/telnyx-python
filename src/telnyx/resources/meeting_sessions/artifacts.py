# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.meeting_sessions import artifact_create_params
from ...types.meeting_sessions.artifact_list_response import ArtifactListResponse
from ...types.meeting_sessions.meeting_session_artifact_response import MeetingSessionArtifactResponse

__all__ = ["ArtifactsResource", "AsyncArtifactsResource"]


class ArtifactsResource(SyncAPIResource):
    """Create and retrieve asynchronous summaries and action-item artifacts."""

    @cached_property
    def with_raw_response(self) -> ArtifactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ArtifactsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        type: Literal["summary", "action_items"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionArtifactResponse:
        """
        Requests asynchronous generation of one `summary` or `action_items` artifact.
        Each type requires its own request. Generation requires transcript content and
        configured inference and currently reads at most the first 10,000 segments, so
        exceptionally long transcripts may produce incomplete artifacts or fail model
        limits.

        Args:
          type: Type of artifact to generate from the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/meeting_sessions/{id}/artifacts", id=id),
            body=maybe_transform({"type": type}, artifact_create_params.ArtifactCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionArtifactResponse,
        )

    def retrieve(
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
    ) -> MeetingSessionArtifactResponse:
        """
        Retrieves a single meeting session artifact by ID.

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
            path_template("/meeting_sessions/{id}/artifacts/{artifact_id}", id=id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionArtifactResponse,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        Returns a list of artifacts for a meeting session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/meeting_sessions/{id}/artifacts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactListResponse,
        )


class AsyncArtifactsResource(AsyncAPIResource):
    """Create and retrieve asynchronous summaries and action-item artifacts."""

    @cached_property
    def with_raw_response(self) -> AsyncArtifactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncArtifactsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        type: Literal["summary", "action_items"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeetingSessionArtifactResponse:
        """
        Requests asynchronous generation of one `summary` or `action_items` artifact.
        Each type requires its own request. Generation requires transcript content and
        configured inference and currently reads at most the first 10,000 segments, so
        exceptionally long transcripts may produce incomplete artifacts or fail model
        limits.

        Args:
          type: Type of artifact to generate from the session.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/meeting_sessions/{id}/artifacts", id=id),
            body=await async_maybe_transform({"type": type}, artifact_create_params.ArtifactCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionArtifactResponse,
        )

    async def retrieve(
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
    ) -> MeetingSessionArtifactResponse:
        """
        Retrieves a single meeting session artifact by ID.

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
            path_template("/meeting_sessions/{id}/artifacts/{artifact_id}", id=id, artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeetingSessionArtifactResponse,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactListResponse:
        """
        Returns a list of artifacts for a meeting session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/meeting_sessions/{id}/artifacts", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArtifactListResponse,
        )


class ArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.create = to_raw_response_wrapper(
            artifacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            artifacts.list,
        )


class AsyncArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.create = async_to_raw_response_wrapper(
            artifacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            artifacts.list,
        )


class ArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.create = to_streamed_response_wrapper(
            artifacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            artifacts.list,
        )


class AsyncArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.create = async_to_streamed_response_wrapper(
            artifacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            artifacts.list,
        )
