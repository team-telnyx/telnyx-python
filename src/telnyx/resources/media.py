# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import media_list_params, media_update_params, media_upload_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
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
from .._base_client import make_request_options
from ..types.media_list_response import MediaListResponse
from ..types.media_update_response import MediaUpdateResponse
from ..types.media_upload_response import MediaUploadResponse
from ..types.media_retrieve_response import MediaRetrieveResponse

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrieveResponse:
        """
        Returns the information about a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        return self._get(
            f"/media/{media_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRetrieveResponse,
        )

    def update(
        self,
        media_name: str,
        *,
        media_url: str | NotGiven = NOT_GIVEN,
        ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaUpdateResponse:
        """
        Updates a stored media file.

        Args:
          media_url: The URL where the media to be stored in Telnyx network is currently hosted. The
              maximum allowed size is 20 MB.

          ttl_secs: The number of seconds after which the media resource will be deleted, defaults
              to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        body = deepcopy_minimal(
            {
                "media_url": media_url,
                "ttl_secs": ttl_secs,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["media"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/media/{media_name}",
            body=maybe_transform(body, media_update_params.MediaUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUpdateResponse,
        )

    def list(
        self,
        *,
        filter: media_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaListResponse:
        """
        Returns a list of stored media files.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[content_type][]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/media",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"filter": filter}, media_list_params.MediaListParams),
            ),
            cast_to=MediaListResponse,
        )

    def delete(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/media/{media_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def download(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Downloads a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/media/{media_name}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def upload(
        self,
        *,
        media_url: str,
        media_name: str | NotGiven = NOT_GIVEN,
        ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaUploadResponse:
        """
        Upload media file to Telnyx so it can be used with other Telnyx services

        Args:
          media_url: The URL where the media to be stored in Telnyx network is currently hosted. The
              maximum allowed size is 20 MB.

          media_name: The unique identifier of a file.

          ttl_secs: The number of seconds after which the media resource will be deleted, defaults
              to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "media_url": media_url,
                "media_name": media_name,
                "ttl_secs": ttl_secs,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["media"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/media",
            body=maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaRetrieveResponse:
        """
        Returns the information about a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        return await self._get(
            f"/media/{media_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaRetrieveResponse,
        )

    async def update(
        self,
        media_name: str,
        *,
        media_url: str | NotGiven = NOT_GIVEN,
        ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaUpdateResponse:
        """
        Updates a stored media file.

        Args:
          media_url: The URL where the media to be stored in Telnyx network is currently hosted. The
              maximum allowed size is 20 MB.

          ttl_secs: The number of seconds after which the media resource will be deleted, defaults
              to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        body = deepcopy_minimal(
            {
                "media_url": media_url,
                "ttl_secs": ttl_secs,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["media"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/media/{media_name}",
            body=await async_maybe_transform(body, media_update_params.MediaUpdateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: media_list_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaListResponse:
        """
        Returns a list of stored media files.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[content_type][]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/media",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"filter": filter}, media_list_params.MediaListParams),
            ),
            cast_to=MediaListResponse,
        )

    async def delete(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/media/{media_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def download(
        self,
        media_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads a stored media file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_name:
            raise ValueError(f"Expected a non-empty value for `media_name` but received {media_name!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/media/{media_name}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def upload(
        self,
        *,
        media_url: str,
        media_name: str | NotGiven = NOT_GIVEN,
        ttl_secs: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MediaUploadResponse:
        """
        Upload media file to Telnyx so it can be used with other Telnyx services

        Args:
          media_url: The URL where the media to be stored in Telnyx network is currently hosted. The
              maximum allowed size is 20 MB.

          media_name: The unique identifier of a file.

          ttl_secs: The number of seconds after which the media resource will be deleted, defaults
              to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "media_url": media_url,
                "media_name": media_name,
                "ttl_secs": ttl_secs,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["media"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/media",
            body=await async_maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.retrieve = to_raw_response_wrapper(
            media.retrieve,
        )
        self.update = to_raw_response_wrapper(
            media.update,
        )
        self.list = to_raw_response_wrapper(
            media.list,
        )
        self.delete = to_raw_response_wrapper(
            media.delete,
        )
        self.download = to_custom_raw_response_wrapper(
            media.download,
            BinaryAPIResponse,
        )
        self.upload = to_raw_response_wrapper(
            media.upload,
        )


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.retrieve = async_to_raw_response_wrapper(
            media.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            media.update,
        )
        self.list = async_to_raw_response_wrapper(
            media.list,
        )
        self.delete = async_to_raw_response_wrapper(
            media.delete,
        )
        self.download = async_to_custom_raw_response_wrapper(
            media.download,
            AsyncBinaryAPIResponse,
        )
        self.upload = async_to_raw_response_wrapper(
            media.upload,
        )


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.retrieve = to_streamed_response_wrapper(
            media.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            media.update,
        )
        self.list = to_streamed_response_wrapper(
            media.list,
        )
        self.delete = to_streamed_response_wrapper(
            media.delete,
        )
        self.download = to_custom_streamed_response_wrapper(
            media.download,
            StreamedBinaryAPIResponse,
        )
        self.upload = to_streamed_response_wrapper(
            media.upload,
        )


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.retrieve = async_to_streamed_response_wrapper(
            media.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            media.update,
        )
        self.list = async_to_streamed_response_wrapper(
            media.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            media.delete,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            media.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.upload = async_to_streamed_response_wrapper(
            media.upload,
        )
