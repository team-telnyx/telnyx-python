# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import speech_to_text_transcribe_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]


class SpeechToTextResource(SyncAPIResource):
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

    def transcribe(
        self,
        *,
        input_format: Literal["mp3", "wav"],
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        interim_results: bool | Omit = omit,
        language: str | Omit = omit,
        model: Literal[
            "fast",
            "deepgram/nova-2",
            "deepgram/nova-3",
            "latest_long",
            "latest_short",
            "command_and_search",
            "phone_call",
            "video",
            "default",
            "medical_conversation",
            "medical_dictation",
            "openai/whisper-tiny",
            "openai/whisper-large-v3-turbo",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Transcribe audio streams to text over WebSocket.

        Args:
          input_format: The format of input audio stream.

          transcription_engine: The transcription engine to use for processing the audio stream.

          interim_results: Whether to receive interim transcription results.

          language: The language spoken in the audio stream.

          model: The specific model to use within the selected transcription engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/speech-to-text/transcription",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "input_format": input_format,
                        "transcription_engine": transcription_engine,
                        "interim_results": interim_results,
                        "language": language,
                        "model": model,
                    },
                    speech_to_text_transcribe_params.SpeechToTextTranscribeParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
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

    async def transcribe(
        self,
        *,
        input_format: Literal["mp3", "wav"],
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        interim_results: bool | Omit = omit,
        language: str | Omit = omit,
        model: Literal[
            "fast",
            "deepgram/nova-2",
            "deepgram/nova-3",
            "latest_long",
            "latest_short",
            "command_and_search",
            "phone_call",
            "video",
            "default",
            "medical_conversation",
            "medical_dictation",
            "openai/whisper-tiny",
            "openai/whisper-large-v3-turbo",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Transcribe audio streams to text over WebSocket.

        Args:
          input_format: The format of input audio stream.

          transcription_engine: The transcription engine to use for processing the audio stream.

          interim_results: Whether to receive interim transcription results.

          language: The language spoken in the audio stream.

          model: The specific model to use within the selected transcription engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/speech-to-text/transcription",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "input_format": input_format,
                        "transcription_engine": transcription_engine,
                        "interim_results": interim_results,
                        "language": language,
                        "model": model,
                    },
                    speech_to_text_transcribe_params.SpeechToTextTranscribeParams,
                ),
            ),
            cast_to=NoneType,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = to_raw_response_wrapper(
            speech_to_text.transcribe,
        )


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = async_to_raw_response_wrapper(
            speech_to_text.transcribe,
        )


class SpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = to_streamed_response_wrapper(
            speech_to_text.transcribe,
        )


class AsyncSpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.transcribe = async_to_streamed_response_wrapper(
            speech_to_text.transcribe,
        )
