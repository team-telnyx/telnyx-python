# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import speech_to_text_list_providers_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.speech_to_text_list_providers_response import SpeechToTextListProvidersResponse

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]


class SpeechToTextResource(SyncAPIResource):
    """Discover available speech-to-text providers, models, and supported languages."""

    @cached_property
    def with_raw_response(self) -> SpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SpeechToTextResourceWithStreamingResponse(self)

    def list_providers(
        self,
        *,
        provider: Literal[
            "deepgram", "speechmatics", "assemblyai", "xai", "soniox", "parakeet", "azure", "openai", "google", "telnyx"
        ]
        | Omit = omit,
        service_type: Literal["streaming", "file_based", "in_call", "ai_assistant"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextListProvidersResponse:
        """
        Retrieve the canonical list of supported speech-to-text providers, models,
        accepted language codes, and the service types each model supports.

        Service types:

        - `streaming` — standalone WebSocket transcription via
          `/speech-to-text/transcription`.
        - `file_based` — file-based transcription via `/ai/audio/transcriptions`.
        - `in_call` — live call transcription via Call Control `transcription_start`.
        - `ai_assistant` — STT configured on a Call Control AI Assistant via
          voice-assistant `TranscriptionConfig` (covers both live-streaming and
          non-streaming/batch models).

        Use this endpoint to discover which (provider, model) combinations are available
        for the surface you need, and which language codes each accepts. `auto` in a
        `languages` array indicates the provider performs language detection.

        Args:
          provider: Filter to entries for a specific STT provider. The enum mirrors the providers
              advertised across the speech-to-text spec (including `google` and `telnyx`,
              which are accepted as WebSocket transcription engines). A provider that has no
              models currently registered for any service type will return an empty `data`
              array rather than an error.

          service_type: Filter to entries that support the given service type. For backward
              compatibility with the values that briefly shipped before the product-aligned
              rename, the legacy aliases `file_transcription`, `in_call_transcription`, and
              `ai_assistant_transcription` are silently accepted and normalized to
              `file_based`, `in_call`, and `ai_assistant` respectively. The response always
              emits the canonical (post-rename) values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/speech-to-text/providers"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/v2/speech-to-text/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "provider": provider,
                        "service_type": service_type,
                    },
                    speech_to_text_list_providers_params.SpeechToTextListProvidersParams,
                ),
            ),
            cast_to=SpeechToTextListProvidersResponse,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
    """Discover available speech-to-text providers, models, and supported languages."""

    @cached_property
    def with_raw_response(self) -> AsyncSpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSpeechToTextResourceWithStreamingResponse(self)

    async def list_providers(
        self,
        *,
        provider: Literal[
            "deepgram", "speechmatics", "assemblyai", "xai", "soniox", "parakeet", "azure", "openai", "google", "telnyx"
        ]
        | Omit = omit,
        service_type: Literal["streaming", "file_based", "in_call", "ai_assistant"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextListProvidersResponse:
        """
        Retrieve the canonical list of supported speech-to-text providers, models,
        accepted language codes, and the service types each model supports.

        Service types:

        - `streaming` — standalone WebSocket transcription via
          `/speech-to-text/transcription`.
        - `file_based` — file-based transcription via `/ai/audio/transcriptions`.
        - `in_call` — live call transcription via Call Control `transcription_start`.
        - `ai_assistant` — STT configured on a Call Control AI Assistant via
          voice-assistant `TranscriptionConfig` (covers both live-streaming and
          non-streaming/batch models).

        Use this endpoint to discover which (provider, model) combinations are available
        for the surface you need, and which language codes each accepts. `auto` in a
        `languages` array indicates the provider performs language detection.

        Args:
          provider: Filter to entries for a specific STT provider. The enum mirrors the providers
              advertised across the speech-to-text spec (including `google` and `telnyx`,
              which are accepted as WebSocket transcription engines). A provider that has no
              models currently registered for any service type will return an empty `data`
              array rather than an error.

          service_type: Filter to entries that support the given service type. For backward
              compatibility with the values that briefly shipped before the product-aligned
              rename, the legacy aliases `file_transcription`, `in_call_transcription`, and
              `ai_assistant_transcription` are silently accepted and normalized to
              `file_based`, `in_call`, and `ai_assistant` respectively. The response always
              emits the canonical (post-rename) values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/speech-to-text/providers"
            if self._client._base_url_overridden
            else "https://api.telnyx.com/v2/speech-to-text/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "provider": provider,
                        "service_type": service_type,
                    },
                    speech_to_text_list_providers_params.SpeechToTextListProvidersParams,
                ),
            ),
            cast_to=SpeechToTextListProvidersResponse,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.list_providers = to_raw_response_wrapper(
            speech_to_text.list_providers,
        )


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.list_providers = async_to_raw_response_wrapper(
            speech_to_text.list_providers,
        )


class SpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.list_providers = to_streamed_response_wrapper(
            speech_to_text.list_providers,
        )


class AsyncSpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.list_providers = async_to_streamed_response_wrapper(
            speech_to_text.list_providers,
        )
