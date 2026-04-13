# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import (
    voice_clone_list_params,
    voice_clone_create_params,
    voice_clone_update_params,
    voice_clone_create_from_upload_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
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
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.voice_clone_data import VoiceCloneData
from ..types.voice_clone_create_response import VoiceCloneCreateResponse
from ..types.voice_clone_update_response import VoiceCloneUpdateResponse
from ..types.voice_clone_create_from_upload_response import VoiceCloneCreateFromUploadResponse

__all__ = ["VoiceClonesResource", "AsyncVoiceClonesResource"]


class VoiceClonesResource(SyncAPIResource):
    """
    Capture and manage voice identities as clones for use in text-to-speech synthesis.
    """

    @cached_property
    def with_raw_response(self) -> VoiceClonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoiceClonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceClonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoiceClonesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        params: voice_clone_create_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneCreateResponse:
        """
        Creates a new voice clone by capturing the voice identity of an existing voice
        design. The clone can then be used for text-to-speech synthesis.

        Args:
          params: Request body for creating a voice clone from an existing voice design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice_clones",
            body=maybe_transform(params, voice_clone_create_params.VoiceCloneCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        name: str,
        gender: Literal["male", "female", "neutral"] | Omit = omit,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneUpdateResponse:
        """
        Updates the name, language, or gender of a voice clone.

        Args:
          name: New name for the voice clone.

          gender: Updated gender for the voice clone.

          language: Updated ISO 639-1 language code or `auto`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/voice_clones/{id}", id=id),
            body=maybe_transform(
                {
                    "name": name,
                    "gender": gender,
                    "language": language,
                },
                voice_clone_update_params.VoiceCloneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneUpdateResponse,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_provider: Literal["telnyx", "minimax"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VoiceCloneData]:
        """
        Returns a paginated list of voice clones belonging to the authenticated account.

        Args:
          filter_name: Case-insensitive substring filter on the name field.

          filter_provider: Filter by voice synthesis provider. Case-insensitive.

          page_number: Page number for pagination (1-based).

          page_size: Number of results per page.

          sort: Sort order. Prefix with `-` for descending. Defaults to `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_clones",
            page=SyncDefaultFlatPagination[VoiceCloneData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_provider": filter_provider,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_clone_list_params.VoiceCloneListParams,
                ),
            ),
            model=VoiceCloneData,
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
    ) -> None:
        """Permanently deletes a voice clone.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/voice_clones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_from_upload(
        self,
        *,
        params: voice_clone_create_from_upload_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneCreateFromUploadResponse:
        """Creates a new voice clone by uploading an audio file directly.

        Supported
        formats: WAV, MP3, FLAC, OGG, M4A. For best results, provide 5–10 seconds of
        clear speech. Maximum file size: 5MB for Telnyx, 20MB for Minimax.

        Args:
          params: Multipart form data for creating a voice clone from a direct audio upload.
              Maximum file size: 5MB for Telnyx, 20MB for Minimax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(params)
        files = extract_files(cast(Mapping[str, object], body), paths=[["audio_file"], ["audio_file"], ["audio_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/voice_clones/from_upload",
            body=maybe_transform(body, voice_clone_create_from_upload_params.VoiceCloneCreateFromUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneCreateFromUploadResponse,
        )

    def download_sample(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Downloads the WAV audio sample that was used to create the voice clone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return self._get(
            path_template("/voice_clones/{id}/sample", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncVoiceClonesResource(AsyncAPIResource):
    """
    Capture and manage voice identities as clones for use in text-to-speech synthesis.
    """

    @cached_property
    def with_raw_response(self) -> AsyncVoiceClonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceClonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceClonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoiceClonesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        params: voice_clone_create_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneCreateResponse:
        """
        Creates a new voice clone by capturing the voice identity of an existing voice
        design. The clone can then be used for text-to-speech synthesis.

        Args:
          params: Request body for creating a voice clone from an existing voice design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice_clones",
            body=await async_maybe_transform(params, voice_clone_create_params.VoiceCloneCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        name: str,
        gender: Literal["male", "female", "neutral"] | Omit = omit,
        language: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneUpdateResponse:
        """
        Updates the name, language, or gender of a voice clone.

        Args:
          name: New name for the voice clone.

          gender: Updated gender for the voice clone.

          language: Updated ISO 639-1 language code or `auto`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/voice_clones/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "gender": gender,
                    "language": language,
                },
                voice_clone_update_params.VoiceCloneUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneUpdateResponse,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_provider: Literal["telnyx", "minimax"] | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VoiceCloneData, AsyncDefaultFlatPagination[VoiceCloneData]]:
        """
        Returns a paginated list of voice clones belonging to the authenticated account.

        Args:
          filter_name: Case-insensitive substring filter on the name field.

          filter_provider: Filter by voice synthesis provider. Case-insensitive.

          page_number: Page number for pagination (1-based).

          page_size: Number of results per page.

          sort: Sort order. Prefix with `-` for descending. Defaults to `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_clones",
            page=AsyncDefaultFlatPagination[VoiceCloneData],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_provider": filter_provider,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_clone_list_params.VoiceCloneListParams,
                ),
            ),
            model=VoiceCloneData,
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
    ) -> None:
        """Permanently deletes a voice clone.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/voice_clones/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_from_upload(
        self,
        *,
        params: voice_clone_create_from_upload_params.Params,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceCloneCreateFromUploadResponse:
        """Creates a new voice clone by uploading an audio file directly.

        Supported
        formats: WAV, MP3, FLAC, OGG, M4A. For best results, provide 5–10 seconds of
        clear speech. Maximum file size: 5MB for Telnyx, 20MB for Minimax.

        Args:
          params: Multipart form data for creating a voice clone from a direct audio upload.
              Maximum file size: 5MB for Telnyx, 20MB for Minimax.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(params)
        files = extract_files(cast(Mapping[str, object], body), paths=[["audio_file"], ["audio_file"], ["audio_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/voice_clones/from_upload",
            body=await async_maybe_transform(
                body, voice_clone_create_from_upload_params.VoiceCloneCreateFromUploadParams
            ),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceCloneCreateFromUploadResponse,
        )

    async def download_sample(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Downloads the WAV audio sample that was used to create the voice clone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return await self._get(
            path_template("/voice_clones/{id}/sample", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class VoiceClonesResourceWithRawResponse:
    def __init__(self, voice_clones: VoiceClonesResource) -> None:
        self._voice_clones = voice_clones

        self.create = to_raw_response_wrapper(
            voice_clones.create,
        )
        self.update = to_raw_response_wrapper(
            voice_clones.update,
        )
        self.list = to_raw_response_wrapper(
            voice_clones.list,
        )
        self.delete = to_raw_response_wrapper(
            voice_clones.delete,
        )
        self.create_from_upload = to_raw_response_wrapper(
            voice_clones.create_from_upload,
        )
        self.download_sample = to_custom_raw_response_wrapper(
            voice_clones.download_sample,
            BinaryAPIResponse,
        )


class AsyncVoiceClonesResourceWithRawResponse:
    def __init__(self, voice_clones: AsyncVoiceClonesResource) -> None:
        self._voice_clones = voice_clones

        self.create = async_to_raw_response_wrapper(
            voice_clones.create,
        )
        self.update = async_to_raw_response_wrapper(
            voice_clones.update,
        )
        self.list = async_to_raw_response_wrapper(
            voice_clones.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voice_clones.delete,
        )
        self.create_from_upload = async_to_raw_response_wrapper(
            voice_clones.create_from_upload,
        )
        self.download_sample = async_to_custom_raw_response_wrapper(
            voice_clones.download_sample,
            AsyncBinaryAPIResponse,
        )


class VoiceClonesResourceWithStreamingResponse:
    def __init__(self, voice_clones: VoiceClonesResource) -> None:
        self._voice_clones = voice_clones

        self.create = to_streamed_response_wrapper(
            voice_clones.create,
        )
        self.update = to_streamed_response_wrapper(
            voice_clones.update,
        )
        self.list = to_streamed_response_wrapper(
            voice_clones.list,
        )
        self.delete = to_streamed_response_wrapper(
            voice_clones.delete,
        )
        self.create_from_upload = to_streamed_response_wrapper(
            voice_clones.create_from_upload,
        )
        self.download_sample = to_custom_streamed_response_wrapper(
            voice_clones.download_sample,
            StreamedBinaryAPIResponse,
        )


class AsyncVoiceClonesResourceWithStreamingResponse:
    def __init__(self, voice_clones: AsyncVoiceClonesResource) -> None:
        self._voice_clones = voice_clones

        self.create = async_to_streamed_response_wrapper(
            voice_clones.create,
        )
        self.update = async_to_streamed_response_wrapper(
            voice_clones.update,
        )
        self.list = async_to_streamed_response_wrapper(
            voice_clones.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voice_clones.delete,
        )
        self.create_from_upload = async_to_streamed_response_wrapper(
            voice_clones.create_from_upload,
        )
        self.download_sample = async_to_custom_streamed_response_wrapper(
            voice_clones.download_sample,
            AsyncStreamedBinaryAPIResponse,
        )
