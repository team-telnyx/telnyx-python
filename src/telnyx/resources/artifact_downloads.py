# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import artifact_download_retrieve_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["ArtifactDownloadsResource", "AsyncArtifactDownloadsResource"]


class ArtifactDownloadsResource(SyncAPIResource):
    """Download screenshots and other artifacts."""

    @cached_property
    def with_raw_response(self) -> ArtifactDownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ArtifactDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactDownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ArtifactDownloadsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        artifact_id: str,
        *,
        expires: str,
        sig: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Downloads the artifact content.

        The signed URL (with expires and sig query
        params) is obtained from the artifact metadata endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/artifact_downloads/{artifact_id}", artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expires": expires,
                        "sig": sig,
                    },
                    artifact_download_retrieve_params.ArtifactDownloadRetrieveParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncArtifactDownloadsResource(AsyncAPIResource):
    """Download screenshots and other artifacts."""

    @cached_property
    def with_raw_response(self) -> AsyncArtifactDownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncArtifactDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactDownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncArtifactDownloadsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        artifact_id: str,
        *,
        expires: str,
        sig: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Downloads the artifact content.

        The signed URL (with expires and sig query
        params) is obtained from the artifact metadata endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/artifact_downloads/{artifact_id}", artifact_id=artifact_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expires": expires,
                        "sig": sig,
                    },
                    artifact_download_retrieve_params.ArtifactDownloadRetrieveParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ArtifactDownloadsResourceWithRawResponse:
    def __init__(self, artifact_downloads: ArtifactDownloadsResource) -> None:
        self._artifact_downloads = artifact_downloads

        self.retrieve = to_custom_raw_response_wrapper(
            artifact_downloads.retrieve,
            BinaryAPIResponse,
        )


class AsyncArtifactDownloadsResourceWithRawResponse:
    def __init__(self, artifact_downloads: AsyncArtifactDownloadsResource) -> None:
        self._artifact_downloads = artifact_downloads

        self.retrieve = async_to_custom_raw_response_wrapper(
            artifact_downloads.retrieve,
            AsyncBinaryAPIResponse,
        )


class ArtifactDownloadsResourceWithStreamingResponse:
    def __init__(self, artifact_downloads: ArtifactDownloadsResource) -> None:
        self._artifact_downloads = artifact_downloads

        self.retrieve = to_custom_streamed_response_wrapper(
            artifact_downloads.retrieve,
            StreamedBinaryAPIResponse,
        )


class AsyncArtifactDownloadsResourceWithStreamingResponse:
    def __init__(self, artifact_downloads: AsyncArtifactDownloadsResource) -> None:
        self._artifact_downloads = artifact_downloads

        self.retrieve = async_to_custom_streamed_response_wrapper(
            artifact_downloads.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
