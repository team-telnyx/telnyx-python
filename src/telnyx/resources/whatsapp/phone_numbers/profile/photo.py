# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ....._types import Body, Query, Headers, NoneType, NotGiven, FileTypes, not_given
from ....._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.whatsapp.phone_numbers.profile import photo_upload_params
from .....types.whatsapp.phone_numbers.profile.photo_upload_response import PhotoUploadResponse

__all__ = ["PhotoResource", "AsyncPhotoResource"]


class PhotoResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> PhotoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhotoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhotoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhotoResourceWithStreamingResponse(self)

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Whatsapp profile photo

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/whatsapp/phone_numbers/{phone_number}/profile/photo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def upload(
        self,
        phone_number: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhotoUploadResponse:
        """
        Upload Whatsapp profile photo

        Args:
          file: Image file (JPEG recommended, max 10 MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v2/whatsapp/phone_numbers/{phone_number}/profile/photo",
            body=maybe_transform(body, photo_upload_params.PhotoUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhotoUploadResponse,
        )


class AsyncPhotoResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> AsyncPhotoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhotoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhotoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhotoResourceWithStreamingResponse(self)

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete Whatsapp profile photo

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/whatsapp/phone_numbers/{phone_number}/profile/photo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def upload(
        self,
        phone_number: str,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhotoUploadResponse:
        """
        Upload Whatsapp profile photo

        Args:
          file: Image file (JPEG recommended, max 10 MB)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v2/whatsapp/phone_numbers/{phone_number}/profile/photo",
            body=await async_maybe_transform(body, photo_upload_params.PhotoUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhotoUploadResponse,
        )


class PhotoResourceWithRawResponse:
    def __init__(self, photo: PhotoResource) -> None:
        self._photo = photo

        self.delete = to_raw_response_wrapper(
            photo.delete,
        )
        self.upload = to_raw_response_wrapper(
            photo.upload,
        )


class AsyncPhotoResourceWithRawResponse:
    def __init__(self, photo: AsyncPhotoResource) -> None:
        self._photo = photo

        self.delete = async_to_raw_response_wrapper(
            photo.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            photo.upload,
        )


class PhotoResourceWithStreamingResponse:
    def __init__(self, photo: PhotoResource) -> None:
        self._photo = photo

        self.delete = to_streamed_response_wrapper(
            photo.delete,
        )
        self.upload = to_streamed_response_wrapper(
            photo.upload,
        )


class AsyncPhotoResourceWithStreamingResponse:
    def __init__(self, photo: AsyncPhotoResource) -> None:
        self._photo = photo

        self.delete = async_to_streamed_response_wrapper(
            photo.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            photo.upload,
        )
