# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage.cloudfs_filesystem_response_wrapper import CloudfsFilesystemResponseWrapper

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """
    Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
    """

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def rotate_meta_token(
        self,
        id: str,
        *,
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemResponseWrapper:
        """
        Issues a new metadata access token for the filesystem and returns the full
        filesystem, including the new `meta_token` and credential-bearing `meta_url`.
        The previous token stops authenticating immediately; the metadata database and
        S3 bucket are unchanged. The request takes no body. Allowed while the filesystem
        is `ready` or `needs_format`; otherwise returns a `409`. Retrying with the same
        `Idempotency-Key` within 24 hours replays the original response — including the
        same token — instead of rotating again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            path_template("/storage/cloudfs/{id}/actions/rotate-meta-token", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemResponseWrapper,
        )


class AsyncActionsResource(AsyncAPIResource):
    """
    Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
    """

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def rotate_meta_token(
        self,
        id: str,
        *,
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemResponseWrapper:
        """
        Issues a new metadata access token for the filesystem and returns the full
        filesystem, including the new `meta_token` and credential-bearing `meta_url`.
        The previous token stops authenticating immediately; the metadata database and
        S3 bucket are unchanged. The request takes no body. Allowed while the filesystem
        is `ready` or `needs_format`; otherwise returns a `409`. Retrying with the same
        `Idempotency-Key` within 24 hours replays the original response — including the
        same token — instead of rotating again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            path_template("/storage/cloudfs/{id}/actions/rotate-meta-token", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemResponseWrapper,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.rotate_meta_token = to_raw_response_wrapper(
            actions.rotate_meta_token,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.rotate_meta_token = async_to_raw_response_wrapper(
            actions.rotate_meta_token,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.rotate_meta_token = to_streamed_response_wrapper(
            actions.rotate_meta_token,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.rotate_meta_token = async_to_streamed_response_wrapper(
            actions.rotate_meta_token,
        )
