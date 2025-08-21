# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import text_to_speech_list_voices_params, text_to_speech_generate_speech_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.text_to_speech_list_voices_response import TextToSpeechListVoicesResponse

__all__ = ["TextToSpeechResource", "AsyncTextToSpeechResource"]


class TextToSpeechResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TextToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TextToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TextToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TextToSpeechResourceWithStreamingResponse(self)

    def generate_speech(
        self,
        *,
        text: str,
        voice: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Converts the provided text to speech using the specified voice and returns audio
        data

        Args:
          text: The text to convert to speech

          voice: The voice ID in the format Provider.ModelId.VoiceId.

              Examples:

              - AWS.Polly.Joanna-Neural
              - Azure.en-US-AvaMultilingualNeural
              - ElevenLabs.eleven_multilingual_v2.Rachel
              - Telnyx.KokoroTTS.af

              Use the `GET /text-to-speech/voices` endpoint to get a complete list of
              available voices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "audio/mpeg", **(extra_headers or {})}
        return self._post(
            "/text-to-speech/speech",
            body=maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                },
                text_to_speech_generate_speech_params.TextToSpeechGenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_voices(
        self,
        *,
        elevenlabs_api_key_ref: str | NotGiven = NOT_GIVEN,
        provider: Literal["aws", "azure", "elevenlabs", "telnyx"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextToSpeechListVoicesResponse:
        """
        Returns a list of voices that can be used with the text to speech commands.

        Args:
          elevenlabs_api_key_ref: Reference to your ElevenLabs API key stored in the Telnyx Portal

          provider: Filter voices by provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/text-to-speech/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "elevenlabs_api_key_ref": elevenlabs_api_key_ref,
                        "provider": provider,
                    },
                    text_to_speech_list_voices_params.TextToSpeechListVoicesParams,
                ),
            ),
            cast_to=TextToSpeechListVoicesResponse,
        )


class AsyncTextToSpeechResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTextToSpeechResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTextToSpeechResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTextToSpeechResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTextToSpeechResourceWithStreamingResponse(self)

    async def generate_speech(
        self,
        *,
        text: str,
        voice: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Converts the provided text to speech using the specified voice and returns audio
        data

        Args:
          text: The text to convert to speech

          voice: The voice ID in the format Provider.ModelId.VoiceId.

              Examples:

              - AWS.Polly.Joanna-Neural
              - Azure.en-US-AvaMultilingualNeural
              - ElevenLabs.eleven_multilingual_v2.Rachel
              - Telnyx.KokoroTTS.af

              Use the `GET /text-to-speech/voices` endpoint to get a complete list of
              available voices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "audio/mpeg", **(extra_headers or {})}
        return await self._post(
            "/text-to-speech/speech",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "voice": voice,
                },
                text_to_speech_generate_speech_params.TextToSpeechGenerateSpeechParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_voices(
        self,
        *,
        elevenlabs_api_key_ref: str | NotGiven = NOT_GIVEN,
        provider: Literal["aws", "azure", "elevenlabs", "telnyx"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TextToSpeechListVoicesResponse:
        """
        Returns a list of voices that can be used with the text to speech commands.

        Args:
          elevenlabs_api_key_ref: Reference to your ElevenLabs API key stored in the Telnyx Portal

          provider: Filter voices by provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/text-to-speech/voices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "elevenlabs_api_key_ref": elevenlabs_api_key_ref,
                        "provider": provider,
                    },
                    text_to_speech_list_voices_params.TextToSpeechListVoicesParams,
                ),
            ),
            cast_to=TextToSpeechListVoicesResponse,
        )


class TextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate_speech = to_custom_raw_response_wrapper(
            text_to_speech.generate_speech,
            BinaryAPIResponse,
        )
        self.list_voices = to_raw_response_wrapper(
            text_to_speech.list_voices,
        )


class AsyncTextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate_speech = async_to_custom_raw_response_wrapper(
            text_to_speech.generate_speech,
            AsyncBinaryAPIResponse,
        )
        self.list_voices = async_to_raw_response_wrapper(
            text_to_speech.list_voices,
        )


class TextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate_speech = to_custom_streamed_response_wrapper(
            text_to_speech.generate_speech,
            StreamedBinaryAPIResponse,
        )
        self.list_voices = to_streamed_response_wrapper(
            text_to_speech.list_voices,
        )


class AsyncTextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate_speech = async_to_custom_streamed_response_wrapper(
            text_to_speech.generate_speech,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            text_to_speech.list_voices,
        )
