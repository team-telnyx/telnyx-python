# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    voice_design_list_params,
    voice_design_create_params,
    voice_design_rename_params,
    voice_design_retrieve_params,
    voice_design_download_sample_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.voice_design_list_response import VoiceDesignListResponse
from ..types.voice_design_create_response import VoiceDesignCreateResponse
from ..types.voice_design_rename_response import VoiceDesignRenameResponse
from ..types.voice_design_retrieve_response import VoiceDesignRetrieveResponse

__all__ = ["VoiceDesignsResource", "AsyncVoiceDesignsResource"]


class VoiceDesignsResource(SyncAPIResource):
    """Create and manage AI-generated voice designs using natural language prompts."""

    @cached_property
    def with_raw_response(self) -> VoiceDesignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VoiceDesignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceDesignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VoiceDesignsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        text: str,
        language: str | Omit = omit,
        max_new_tokens: int | Omit = omit,
        name: str | Omit = omit,
        provider: Literal["telnyx", "minimax"] | Omit = omit,
        repetition_penalty: float | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        voice_design_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignCreateResponse:
        """Creates a new voice design (version 1) when `voice_design_id` is omitted.

        When
        `voice_design_id` is provided, adds a new version to the existing design
        instead. A design can have at most 50 versions.

        Args:
          prompt: Natural language description of the voice style, e.g. 'Speak in a warm, friendly
              tone with a slight British accent'.

          text: Sample text to synthesize for this voice design.

          language: Language for synthesis. Supported values: Auto, Chinese, English, Japanese,
              Korean, German, French, Russian, Portuguese, Spanish, Italian. Defaults to Auto.

          max_new_tokens: Maximum number of tokens to generate. Default: 2048.

          name: Name for the voice design. Required when creating a new design
              (`voice_design_id` is not provided); ignored when adding a version. Cannot be a
              UUID.

          provider: Voice synthesis provider. `telnyx` uses the Qwen3TTS model; `minimax` uses the
              Minimax speech models. Case-insensitive. Defaults to `telnyx`.

          repetition_penalty:
              Repetition penalty to reduce repeated patterns in generated audio. Default:
              1.05.

          temperature: Sampling temperature controlling randomness. Higher values produce more varied
              output. Default: 0.9.

          top_k: Top-k sampling parameter — limits the token vocabulary considered at each step.
              Default: 50.

          top_p: Top-p (nucleus) sampling parameter — cumulative probability cutoff for token
              selection. Default: 1.0.

          voice_design_id: ID of an existing voice design to add a new version to. When provided, a new
              version is created instead of a new design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/voice_designs",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "text": text,
                    "language": language,
                    "max_new_tokens": max_new_tokens,
                    "name": name,
                    "provider": provider,
                    "repetition_penalty": repetition_penalty,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                    "voice_design_id": voice_design_id,
                },
                voice_design_create_params.VoiceDesignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDesignCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignRetrieveResponse:
        """
        Returns the latest version of a voice design, or a specific version when
        `?version=N` is provided. The `id` parameter accepts either a UUID or the design
        name.

        Args:
          version: Specific version number to retrieve. Defaults to the latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/voice_designs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, voice_design_retrieve_params.VoiceDesignRetrieveParams),
            ),
            cast_to=VoiceDesignRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VoiceDesignListResponse]:
        """
        Returns a paginated list of voice designs belonging to the authenticated
        account.

        Args:
          filter_name: Case-insensitive substring filter on the name field.

          page_number: Page number for pagination (1-based).

          page_size: Number of results per page.

          sort: Sort order. Prefix with `-` for descending. Defaults to `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_designs",
            page=SyncDefaultFlatPagination[VoiceDesignListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_design_list_params.VoiceDesignListParams,
                ),
            ),
            model=VoiceDesignListResponse,
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
        """Permanently deletes a voice design and all of its versions.

        This action cannot
        be undone.

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
            path_template("/voice_designs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_version(
        self,
        version: int,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a specific version of a voice design.

        The version number
        must be a positive integer.

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
            path_template("/voice_designs/{id}/versions/{version}", id=id, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def download_sample(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Downloads the WAV audio sample for the voice design.

        Returns the latest
        version's sample by default, or a specific version when `?version=N` is
        provided. The `id` parameter accepts either a UUID or the design name.

        Args:
          version: Specific version number to download the sample for. Defaults to the latest
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return self._get(
            path_template("/voice_designs/{id}/sample", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, voice_design_download_sample_params.VoiceDesignDownloadSampleParams
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def rename(
        self,
        id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignRenameResponse:
        """Updates the name of a voice design.

        All versions retain their other properties.

        Args:
          name: New name for the voice design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/voice_designs/{id}", id=id),
            body=maybe_transform({"name": name}, voice_design_rename_params.VoiceDesignRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDesignRenameResponse,
        )


class AsyncVoiceDesignsResource(AsyncAPIResource):
    """Create and manage AI-generated voice designs using natural language prompts."""

    @cached_property
    def with_raw_response(self) -> AsyncVoiceDesignsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceDesignsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceDesignsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVoiceDesignsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        text: str,
        language: str | Omit = omit,
        max_new_tokens: int | Omit = omit,
        name: str | Omit = omit,
        provider: Literal["telnyx", "minimax"] | Omit = omit,
        repetition_penalty: float | Omit = omit,
        temperature: float | Omit = omit,
        top_k: int | Omit = omit,
        top_p: float | Omit = omit,
        voice_design_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignCreateResponse:
        """Creates a new voice design (version 1) when `voice_design_id` is omitted.

        When
        `voice_design_id` is provided, adds a new version to the existing design
        instead. A design can have at most 50 versions.

        Args:
          prompt: Natural language description of the voice style, e.g. 'Speak in a warm, friendly
              tone with a slight British accent'.

          text: Sample text to synthesize for this voice design.

          language: Language for synthesis. Supported values: Auto, Chinese, English, Japanese,
              Korean, German, French, Russian, Portuguese, Spanish, Italian. Defaults to Auto.

          max_new_tokens: Maximum number of tokens to generate. Default: 2048.

          name: Name for the voice design. Required when creating a new design
              (`voice_design_id` is not provided); ignored when adding a version. Cannot be a
              UUID.

          provider: Voice synthesis provider. `telnyx` uses the Qwen3TTS model; `minimax` uses the
              Minimax speech models. Case-insensitive. Defaults to `telnyx`.

          repetition_penalty:
              Repetition penalty to reduce repeated patterns in generated audio. Default:
              1.05.

          temperature: Sampling temperature controlling randomness. Higher values produce more varied
              output. Default: 0.9.

          top_k: Top-k sampling parameter — limits the token vocabulary considered at each step.
              Default: 50.

          top_p: Top-p (nucleus) sampling parameter — cumulative probability cutoff for token
              selection. Default: 1.0.

          voice_design_id: ID of an existing voice design to add a new version to. When provided, a new
              version is created instead of a new design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/voice_designs",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "text": text,
                    "language": language,
                    "max_new_tokens": max_new_tokens,
                    "name": name,
                    "provider": provider,
                    "repetition_penalty": repetition_penalty,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                    "voice_design_id": voice_design_id,
                },
                voice_design_create_params.VoiceDesignCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDesignCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignRetrieveResponse:
        """
        Returns the latest version of a voice design, or a specific version when
        `?version=N` is provided. The `id` parameter accepts either a UUID or the design
        name.

        Args:
          version: Specific version number to retrieve. Defaults to the latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/voice_designs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, voice_design_retrieve_params.VoiceDesignRetrieveParams
                ),
            ),
            cast_to=VoiceDesignRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["name", "-name", "created_at", "-created_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VoiceDesignListResponse, AsyncDefaultFlatPagination[VoiceDesignListResponse]]:
        """
        Returns a paginated list of voice designs belonging to the authenticated
        account.

        Args:
          filter_name: Case-insensitive substring filter on the name field.

          page_number: Page number for pagination (1-based).

          page_size: Number of results per page.

          sort: Sort order. Prefix with `-` for descending. Defaults to `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/voice_designs",
            page=AsyncDefaultFlatPagination[VoiceDesignListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    voice_design_list_params.VoiceDesignListParams,
                ),
            ),
            model=VoiceDesignListResponse,
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
        """Permanently deletes a voice design and all of its versions.

        This action cannot
        be undone.

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
            path_template("/voice_designs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_version(
        self,
        version: int,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently deletes a specific version of a voice design.

        The version number
        must be a positive integer.

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
            path_template("/voice_designs/{id}/versions/{version}", id=id, version=version),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def download_sample(
        self,
        id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Downloads the WAV audio sample for the voice design.

        Returns the latest
        version's sample by default, or a specific version when `?version=N` is
        provided. The `id` parameter accepts either a UUID or the design name.

        Args:
          version: Specific version number to download the sample for. Defaults to the latest
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "audio/wav", **(extra_headers or {})}
        return await self._get(
            path_template("/voice_designs/{id}/sample", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, voice_design_download_sample_params.VoiceDesignDownloadSampleParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def rename(
        self,
        id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceDesignRenameResponse:
        """Updates the name of a voice design.

        All versions retain their other properties.

        Args:
          name: New name for the voice design.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/voice_designs/{id}", id=id),
            body=await async_maybe_transform({"name": name}, voice_design_rename_params.VoiceDesignRenameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceDesignRenameResponse,
        )


class VoiceDesignsResourceWithRawResponse:
    def __init__(self, voice_designs: VoiceDesignsResource) -> None:
        self._voice_designs = voice_designs

        self.create = to_raw_response_wrapper(
            voice_designs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voice_designs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            voice_designs.list,
        )
        self.delete = to_raw_response_wrapper(
            voice_designs.delete,
        )
        self.delete_version = to_raw_response_wrapper(
            voice_designs.delete_version,
        )
        self.download_sample = to_custom_raw_response_wrapper(
            voice_designs.download_sample,
            BinaryAPIResponse,
        )
        self.rename = to_raw_response_wrapper(
            voice_designs.rename,
        )


class AsyncVoiceDesignsResourceWithRawResponse:
    def __init__(self, voice_designs: AsyncVoiceDesignsResource) -> None:
        self._voice_designs = voice_designs

        self.create = async_to_raw_response_wrapper(
            voice_designs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voice_designs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            voice_designs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            voice_designs.delete,
        )
        self.delete_version = async_to_raw_response_wrapper(
            voice_designs.delete_version,
        )
        self.download_sample = async_to_custom_raw_response_wrapper(
            voice_designs.download_sample,
            AsyncBinaryAPIResponse,
        )
        self.rename = async_to_raw_response_wrapper(
            voice_designs.rename,
        )


class VoiceDesignsResourceWithStreamingResponse:
    def __init__(self, voice_designs: VoiceDesignsResource) -> None:
        self._voice_designs = voice_designs

        self.create = to_streamed_response_wrapper(
            voice_designs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voice_designs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            voice_designs.list,
        )
        self.delete = to_streamed_response_wrapper(
            voice_designs.delete,
        )
        self.delete_version = to_streamed_response_wrapper(
            voice_designs.delete_version,
        )
        self.download_sample = to_custom_streamed_response_wrapper(
            voice_designs.download_sample,
            StreamedBinaryAPIResponse,
        )
        self.rename = to_streamed_response_wrapper(
            voice_designs.rename,
        )


class AsyncVoiceDesignsResourceWithStreamingResponse:
    def __init__(self, voice_designs: AsyncVoiceDesignsResource) -> None:
        self._voice_designs = voice_designs

        self.create = async_to_streamed_response_wrapper(
            voice_designs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voice_designs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            voice_designs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            voice_designs.delete,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            voice_designs.delete_version,
        )
        self.download_sample = async_to_custom_streamed_response_wrapper(
            voice_designs.download_sample,
            AsyncStreamedBinaryAPIResponse,
        )
        self.rename = async_to_streamed_response_wrapper(
            voice_designs.rename,
        )
