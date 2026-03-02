# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import text_to_speech_stream_params, text_to_speech_generate_params, text_to_speech_list_voices_params
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
from ..types.text_to_speech_generate_response import TextToSpeechGenerateResponse
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

    def generate(
        self,
        *,
        aws: text_to_speech_generate_params.Aws | Omit = omit,
        azure: text_to_speech_generate_params.Azure | Omit = omit,
        disable_cache: bool | Omit = omit,
        elevenlabs: text_to_speech_generate_params.Elevenlabs | Omit = omit,
        language: str | Omit = omit,
        minimax: text_to_speech_generate_params.Minimax | Omit = omit,
        output_type: Literal["binary_output", "base64_output"] | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble"] | Omit = omit,
        resemble: text_to_speech_generate_params.Resemble | Omit = omit,
        rime: text_to_speech_generate_params.Rime | Omit = omit,
        telnyx: text_to_speech_generate_params.Telnyx | Omit = omit,
        text: str | Omit = omit,
        text_type: Literal["text", "ssml"] | Omit = omit,
        voice: str | Omit = omit,
        voice_settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToSpeechGenerateResponse:
        """Generate synthesized speech audio from text input.

        Returns audio in the
        requested format (binary audio stream, base64-encoded JSON, or an audio URL for
        later retrieval).

        Authentication is provided via the standard `Authorization: Bearer <API_KEY>`
        header.

        The `voice` parameter provides a convenient shorthand to specify provider,
        model, and voice in a single string (e.g. `telnyx.NaturalHD.Alloy`).
        Alternatively, specify `provider` explicitly along with provider-specific
        parameters.

        Supported providers: `aws`, `telnyx`, `azure`, `elevenlabs`, `minimax`, `rime`,
        `resemble`.

        Args:
          aws: AWS Polly provider-specific parameters.

          azure: Azure Cognitive Services provider-specific parameters.

          disable_cache: When `true`, bypass the audio cache and generate fresh audio.

          elevenlabs: ElevenLabs provider-specific parameters.

          language: Language code (e.g. `en-US`). Usage varies by provider.

          minimax: Minimax provider-specific parameters.

          output_type: Determines the response format. `binary_output` returns raw audio bytes,
              `base64_output` returns base64-encoded audio in JSON.

          provider: TTS provider. Required unless `voice` is provided.

          resemble: Resemble AI provider-specific parameters.

          rime: Rime provider-specific parameters.

          telnyx: Telnyx provider-specific parameters.

          text: The text to convert to speech.

          text_type: Text type. Use `ssml` for SSML-formatted input (supported by AWS and Azure).

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id`. Examples: `telnyx.NaturalHD.Alloy`,
              `azure.en-US-AvaMultilingualNeural`, `aws.Polly.Generative.Lucia`. When
              provided, `provider`, `model_id`, and `voice_id` are extracted automatically and
              take precedence over individual parameters.

          voice_settings: Provider-specific voice settings. Contents vary by provider — see
              provider-specific parameter objects below.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/text-to-speech/speech",
            body=maybe_transform(
                {
                    "aws": aws,
                    "azure": azure,
                    "disable_cache": disable_cache,
                    "elevenlabs": elevenlabs,
                    "language": language,
                    "minimax": minimax,
                    "output_type": output_type,
                    "provider": provider,
                    "resemble": resemble,
                    "rime": rime,
                    "telnyx": telnyx,
                    "text": text,
                    "text_type": text_type,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                text_to_speech_generate_params.TextToSpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextToSpeechGenerateResponse,
        )

    def list_voices(
        self,
        *,
        api_key: str | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToSpeechListVoicesResponse:
        """Retrieve a list of available voices from one or all TTS providers.

        When
        `provider` is specified, returns voices for that provider only. Otherwise,
        returns voices from all providers.

        Some providers (ElevenLabs, Resemble) require an API key to list voices.

        Args:
          api_key: API key for providers that require one to list voices (e.g. ElevenLabs).

          provider: Filter voices by provider. If omitted, voices from all providers are returned.

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
                        "api_key": api_key,
                        "provider": provider,
                    },
                    text_to_speech_list_voices_params.TextToSpeechListVoicesParams,
                ),
            ),
            cast_to=TextToSpeechListVoicesResponse,
        )

    def stream(
        self,
        *,
        audio_format: Literal["pcm", "wav"] | Omit = omit,
        disable_cache: bool | Omit = omit,
        model_id: str | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "murfai", "rime", "resemble"]
        | Omit = omit,
        socket_id: str | Omit = omit,
        voice: str | Omit = omit,
        voice_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Open a WebSocket connection to stream text and receive synthesized audio in real
        time. Authentication is provided via the standard
        `Authorization: Bearer <API_KEY>` header. Send JSON frames with text to
        synthesize; receive JSON frames containing base64-encoded audio chunks.

        Supported providers: `aws`, `telnyx`, `azure`, `murfai`, `minimax`, `rime`,
        `resemble`, `elevenlabs`.

        **Connection flow:**

        1. Open WebSocket with query parameters specifying provider, voice, and model.
        2. Send an initial handshake message `{"text": " "}` (single space) with
           optional `voice_settings` to initialize the session.
        3. Send text messages as `{"text": "Hello world"}`.
        4. Receive audio chunks as JSON frames with base64-encoded audio.
        5. A final frame with `isFinal: true` indicates the end of audio for the current
           text.

        To interrupt and restart synthesis mid-stream, send `{"force": true}` — the
        current worker is stopped and a new one is started.

        Args:
          audio_format: Audio output format override. Supported for Telnyx `Natural`/`NaturalHD` models
              only. Accepted values: `pcm`, `wav`.

          disable_cache: When `true`, bypass the audio cache and generate fresh audio.

          model_id: Model identifier for the chosen provider. Examples: `Natural`, `NaturalHD`
              (Telnyx); `Polly.Generative` (AWS).

          provider: TTS provider. Defaults to `telnyx` if not specified. Ignored when `voice` is
              provided.

          socket_id: Client-provided socket identifier for tracking. If not provided, one is
              generated server-side.

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id` (e.g. `telnyx.NaturalHD.Telnyx_Alloy` or
              `azure.en-US-AvaMultilingualNeural`). When provided, the `provider`, `model_id`,
              and `voice_id` are extracted automatically. Takes precedence over individual
              `provider`/`model_id`/`voice_id` parameters.

          voice_id: Voice identifier for the chosen provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/text-to-speech/speech",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "audio_format": audio_format,
                        "disable_cache": disable_cache,
                        "model_id": model_id,
                        "provider": provider,
                        "socket_id": socket_id,
                        "voice": voice,
                        "voice_id": voice_id,
                    },
                    text_to_speech_stream_params.TextToSpeechStreamParams,
                ),
            ),
            cast_to=NoneType,
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

    async def generate(
        self,
        *,
        aws: text_to_speech_generate_params.Aws | Omit = omit,
        azure: text_to_speech_generate_params.Azure | Omit = omit,
        disable_cache: bool | Omit = omit,
        elevenlabs: text_to_speech_generate_params.Elevenlabs | Omit = omit,
        language: str | Omit = omit,
        minimax: text_to_speech_generate_params.Minimax | Omit = omit,
        output_type: Literal["binary_output", "base64_output"] | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble"] | Omit = omit,
        resemble: text_to_speech_generate_params.Resemble | Omit = omit,
        rime: text_to_speech_generate_params.Rime | Omit = omit,
        telnyx: text_to_speech_generate_params.Telnyx | Omit = omit,
        text: str | Omit = omit,
        text_type: Literal["text", "ssml"] | Omit = omit,
        voice: str | Omit = omit,
        voice_settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToSpeechGenerateResponse:
        """Generate synthesized speech audio from text input.

        Returns audio in the
        requested format (binary audio stream, base64-encoded JSON, or an audio URL for
        later retrieval).

        Authentication is provided via the standard `Authorization: Bearer <API_KEY>`
        header.

        The `voice` parameter provides a convenient shorthand to specify provider,
        model, and voice in a single string (e.g. `telnyx.NaturalHD.Alloy`).
        Alternatively, specify `provider` explicitly along with provider-specific
        parameters.

        Supported providers: `aws`, `telnyx`, `azure`, `elevenlabs`, `minimax`, `rime`,
        `resemble`.

        Args:
          aws: AWS Polly provider-specific parameters.

          azure: Azure Cognitive Services provider-specific parameters.

          disable_cache: When `true`, bypass the audio cache and generate fresh audio.

          elevenlabs: ElevenLabs provider-specific parameters.

          language: Language code (e.g. `en-US`). Usage varies by provider.

          minimax: Minimax provider-specific parameters.

          output_type: Determines the response format. `binary_output` returns raw audio bytes,
              `base64_output` returns base64-encoded audio in JSON.

          provider: TTS provider. Required unless `voice` is provided.

          resemble: Resemble AI provider-specific parameters.

          rime: Rime provider-specific parameters.

          telnyx: Telnyx provider-specific parameters.

          text: The text to convert to speech.

          text_type: Text type. Use `ssml` for SSML-formatted input (supported by AWS and Azure).

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id`. Examples: `telnyx.NaturalHD.Alloy`,
              `azure.en-US-AvaMultilingualNeural`, `aws.Polly.Generative.Lucia`. When
              provided, `provider`, `model_id`, and `voice_id` are extracted automatically and
              take precedence over individual parameters.

          voice_settings: Provider-specific voice settings. Contents vary by provider — see
              provider-specific parameter objects below.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/text-to-speech/speech",
            body=await async_maybe_transform(
                {
                    "aws": aws,
                    "azure": azure,
                    "disable_cache": disable_cache,
                    "elevenlabs": elevenlabs,
                    "language": language,
                    "minimax": minimax,
                    "output_type": output_type,
                    "provider": provider,
                    "resemble": resemble,
                    "rime": rime,
                    "telnyx": telnyx,
                    "text": text,
                    "text_type": text_type,
                    "voice": voice,
                    "voice_settings": voice_settings,
                },
                text_to_speech_generate_params.TextToSpeechGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TextToSpeechGenerateResponse,
        )

    async def list_voices(
        self,
        *,
        api_key: str | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TextToSpeechListVoicesResponse:
        """Retrieve a list of available voices from one or all TTS providers.

        When
        `provider` is specified, returns voices for that provider only. Otherwise,
        returns voices from all providers.

        Some providers (ElevenLabs, Resemble) require an API key to list voices.

        Args:
          api_key: API key for providers that require one to list voices (e.g. ElevenLabs).

          provider: Filter voices by provider. If omitted, voices from all providers are returned.

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
                        "api_key": api_key,
                        "provider": provider,
                    },
                    text_to_speech_list_voices_params.TextToSpeechListVoicesParams,
                ),
            ),
            cast_to=TextToSpeechListVoicesResponse,
        )

    async def stream(
        self,
        *,
        audio_format: Literal["pcm", "wav"] | Omit = omit,
        disable_cache: bool | Omit = omit,
        model_id: str | Omit = omit,
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "murfai", "rime", "resemble"]
        | Omit = omit,
        socket_id: str | Omit = omit,
        voice: str | Omit = omit,
        voice_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Open a WebSocket connection to stream text and receive synthesized audio in real
        time. Authentication is provided via the standard
        `Authorization: Bearer <API_KEY>` header. Send JSON frames with text to
        synthesize; receive JSON frames containing base64-encoded audio chunks.

        Supported providers: `aws`, `telnyx`, `azure`, `murfai`, `minimax`, `rime`,
        `resemble`, `elevenlabs`.

        **Connection flow:**

        1. Open WebSocket with query parameters specifying provider, voice, and model.
        2. Send an initial handshake message `{"text": " "}` (single space) with
           optional `voice_settings` to initialize the session.
        3. Send text messages as `{"text": "Hello world"}`.
        4. Receive audio chunks as JSON frames with base64-encoded audio.
        5. A final frame with `isFinal: true` indicates the end of audio for the current
           text.

        To interrupt and restart synthesis mid-stream, send `{"force": true}` — the
        current worker is stopped and a new one is started.

        Args:
          audio_format: Audio output format override. Supported for Telnyx `Natural`/`NaturalHD` models
              only. Accepted values: `pcm`, `wav`.

          disable_cache: When `true`, bypass the audio cache and generate fresh audio.

          model_id: Model identifier for the chosen provider. Examples: `Natural`, `NaturalHD`
              (Telnyx); `Polly.Generative` (AWS).

          provider: TTS provider. Defaults to `telnyx` if not specified. Ignored when `voice` is
              provided.

          socket_id: Client-provided socket identifier for tracking. If not provided, one is
              generated server-side.

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id` (e.g. `telnyx.NaturalHD.Telnyx_Alloy` or
              `azure.en-US-AvaMultilingualNeural`). When provided, the `provider`, `model_id`,
              and `voice_id` are extracted automatically. Takes precedence over individual
              `provider`/`model_id`/`voice_id` parameters.

          voice_id: Voice identifier for the chosen provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/text-to-speech/speech",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "audio_format": audio_format,
                        "disable_cache": disable_cache,
                        "model_id": model_id,
                        "provider": provider,
                        "socket_id": socket_id,
                        "voice": voice,
                        "voice_id": voice_id,
                    },
                    text_to_speech_stream_params.TextToSpeechStreamParams,
                ),
            ),
            cast_to=NoneType,
        )


class TextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = to_raw_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = to_raw_response_wrapper(
            text_to_speech.list_voices,
        )
        self.stream = to_raw_response_wrapper(
            text_to_speech.stream,
        )


class AsyncTextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = async_to_raw_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = async_to_raw_response_wrapper(
            text_to_speech.list_voices,
        )
        self.stream = async_to_raw_response_wrapper(
            text_to_speech.stream,
        )


class TextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: TextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = to_streamed_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = to_streamed_response_wrapper(
            text_to_speech.list_voices,
        )
        self.stream = to_streamed_response_wrapper(
            text_to_speech.stream,
        )


class AsyncTextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = async_to_streamed_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            text_to_speech.list_voices,
        )
        self.stream = async_to_streamed_response_wrapper(
            text_to_speech.stream,
        )
