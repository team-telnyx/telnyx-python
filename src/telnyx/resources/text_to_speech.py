# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import time
import random
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Dict, Union, Callable, Iterator, Awaitable, cast
from typing_extensions import Literal, AsyncIterator

import httpx
from pydantic import BaseModel

from ..types import text_to_speech_generate_params, text_to_speech_list_voices_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._models import construct_type_unchecked
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._exceptions import TelnyxError, WebSocketConnectionClosedError
from .._send_queue import SendQueue
from .._base_client import _merge_mappings, make_request_options
from .._event_handler import EventHandlerRegistry
from ..types.stream_client_event import StreamClientEvent
from ..types.stream_server_event import ErrorFrame, StreamServerEvent
from ..types.websocket_reconnection import ReconnectingEvent, ReconnectingOverrides, is_recoverable_close
from ..types.stream_client_event_param import StreamClientEventParam
from ..types.websocket_connection_options import WebSocketConnectionOptions
from ..types.text_to_speech_generate_response import TextToSpeechGenerateResponse
from ..types.text_to_speech_list_voices_response import TextToSpeechListVoicesResponse

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebSocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebSocketConnection

    from .._client import Telnyx, AsyncTelnyx

__all__ = ["TextToSpeechResource", "AsyncTextToSpeechResource"]

log: logging.Logger = logging.getLogger(__name__)


class TextToSpeechResource(SyncAPIResource):
    """Text to speech streaming command operations"""

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
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble", "xai"] | Omit = omit,
        resemble: text_to_speech_generate_params.Resemble | Omit = omit,
        rime: text_to_speech_generate_params.Rime | Omit = omit,
        telnyx: text_to_speech_generate_params.Telnyx | Omit = omit,
        text: str | Omit = omit,
        text_type: Literal["text", "ssml"] | Omit = omit,
        voice: str | Omit = omit,
        voice_settings: Dict[str, object] | Omit = omit,
        xai: text_to_speech_generate_params.Xai | Omit = omit,
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
        model, and voice in a single string (e.g. `telnyx.NaturalHD.Alloy` or
        `Telnyx.Ultra.<voice_id>`). Alternatively, specify `provider` explicitly along
        with provider-specific parameters.

        Supported providers: `aws`, `telnyx`, `azure`, `elevenlabs`, `minimax`, `rime`,
        `resemble`, `xai`.

        The Telnyx `Ultra` model supports 44 languages with emotion control, speed
        adjustment, and volume control. Use the `telnyx` provider-specific parameters to
        configure these features.

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

          telnyx: Telnyx provider-specific parameters. Use `voice_speed` and `temperature` for
              `Natural` and `NaturalHD` models. For the `Ultra` model, use `voice_speed`,
              `volume`, and `emotion`.

          text: The text to convert to speech.

          text_type: Text type. Use `ssml` for SSML-formatted input (supported by AWS and Azure).

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id`. Examples: `telnyx.NaturalHD.Alloy`,
              `Telnyx.Ultra.<voice_id>`, `azure.en-US-AvaMultilingualNeural`,
              `aws.Polly.Generative.Lucia`. When provided, `provider`, `model_id`, and
              `voice_id` are extracted automatically and take precedence over individual
              parameters.

          voice_settings: Provider-specific voice settings. Contents vary by provider — see
              provider-specific parameter objects below.

          xai: xAI provider-specific parameters.

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
                    "xai": xai,
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
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble", "xai"] | Omit = omit,
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
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> TextToSpeechResourceConnectionManager:
        return TextToSpeechResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
        )


class AsyncTextToSpeechResource(AsyncAPIResource):
    """Text to speech streaming command operations"""

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
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble", "xai"] | Omit = omit,
        resemble: text_to_speech_generate_params.Resemble | Omit = omit,
        rime: text_to_speech_generate_params.Rime | Omit = omit,
        telnyx: text_to_speech_generate_params.Telnyx | Omit = omit,
        text: str | Omit = omit,
        text_type: Literal["text", "ssml"] | Omit = omit,
        voice: str | Omit = omit,
        voice_settings: Dict[str, object] | Omit = omit,
        xai: text_to_speech_generate_params.Xai | Omit = omit,
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
        model, and voice in a single string (e.g. `telnyx.NaturalHD.Alloy` or
        `Telnyx.Ultra.<voice_id>`). Alternatively, specify `provider` explicitly along
        with provider-specific parameters.

        Supported providers: `aws`, `telnyx`, `azure`, `elevenlabs`, `minimax`, `rime`,
        `resemble`, `xai`.

        The Telnyx `Ultra` model supports 44 languages with emotion control, speed
        adjustment, and volume control. Use the `telnyx` provider-specific parameters to
        configure these features.

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

          telnyx: Telnyx provider-specific parameters. Use `voice_speed` and `temperature` for
              `Natural` and `NaturalHD` models. For the `Ultra` model, use `voice_speed`,
              `volume`, and `emotion`.

          text: The text to convert to speech.

          text_type: Text type. Use `ssml` for SSML-formatted input (supported by AWS and Azure).

          voice: Voice identifier in the format `provider.model_id.voice_id` or
              `provider.voice_id`. Examples: `telnyx.NaturalHD.Alloy`,
              `Telnyx.Ultra.<voice_id>`, `azure.en-US-AvaMultilingualNeural`,
              `aws.Polly.Generative.Lucia`. When provided, `provider`, `model_id`, and
              `voice_id` are extracted automatically and take precedence over individual
              parameters.

          voice_settings: Provider-specific voice settings. Contents vary by provider — see
              provider-specific parameter objects below.

          xai: xAI provider-specific parameters.

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
                    "xai": xai,
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
        provider: Literal["aws", "telnyx", "azure", "elevenlabs", "minimax", "rime", "resemble", "xai"] | Omit = omit,
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

    def stream(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> AsyncTextToSpeechResourceConnectionManager:
        return AsyncTextToSpeechResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
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


class AsyncTextToSpeechResourceWithRawResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = async_to_raw_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = async_to_raw_response_wrapper(
            text_to_speech.list_voices,
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


class AsyncTextToSpeechResourceWithStreamingResponse:
    def __init__(self, text_to_speech: AsyncTextToSpeechResource) -> None:
        self._text_to_speech = text_to_speech

        self.generate = async_to_streamed_response_wrapper(
            text_to_speech.generate,
        )
        self.list_voices = async_to_streamed_response_wrapper(
            text_to_speech.list_voices,
        )


class AsyncTextToSpeechResourceConnection:
    """Represents a live WebSocket connection to the TextToSpeech API"""

    _connection: AsyncWebSocketConnection

    def __init__(
        self,
        connection: AsyncWebSocketConnection,
        *,
        make_ws: Callable[[Query, Headers], Awaitable[AsyncWebSocketConnection]] | None = None,
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        extra_query: Query = {},
        extra_headers: Headers = {},
        send_queue: SendQueue | None = None,
    ) -> None:
        self._connection = connection
        self._make_ws = make_ws
        self._on_reconnecting = on_reconnecting
        self._max_retries = max_retries
        self._initial_delay = initial_delay
        self._max_delay = max_delay
        self._extra_query = extra_query
        self._extra_headers = extra_headers
        self._intentionally_closed = False
        self._is_reconnecting = False
        self._send_queue = send_queue or SendQueue()
        self._event_handler_registry = EventHandlerRegistry(use_lock=False)

    async def __aiter__(self) -> AsyncIterator[StreamServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

        while True:
            try:
                yield await self.recv()
            except ConnectionClosedOK:
                return
            except ConnectionClosedError as exc:
                if not await self._reconnect(exc):
                    unsent = self._send_queue.drain()
                    if unsent:
                        raise WebSocketConnectionClosedError(
                            "WebSocket connection closed with unsent messages",
                            unsent_messages=unsent,
                        ) from exc
                    raise

    async def recv(self) -> StreamServerEvent:
        """
        Receive the next message from the connection and parses it into a `StreamServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(await self.recv_bytes())

    async def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `StreamServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = await self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    async def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(await async_maybe_transform(event, StreamClientEventParam))
        )
        if self._is_reconnecting:
            self._send_queue.enqueue(data)
            return
        try:
            await self._connection.send(data)
        except Exception:
            self._send_queue.enqueue(data)
            raise

    async def send_raw(self, data: bytes | str) -> None:
        if self._is_reconnecting:
            raw = data if isinstance(data, str) else data.decode("utf-8")
            self._send_queue.enqueue(raw)
            return
        await self._connection.send(data)

    async def close(self, *, code: int = 1000, reason: str = "") -> None:
        self._intentionally_closed = True
        await self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> StreamServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `StreamServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            StreamServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, StreamServerEvent))
        )

    async def _reconnect(self, exc: Exception) -> bool:
        """Attempt to reconnect after a connection failure.

        Returns ``True`` if a new connection was established, ``False`` if the
        caller should re-raise the original exception.
        """
        import asyncio

        if self._on_reconnecting is None or self._make_ws is None:
            return False

        from websockets.exceptions import ConnectionClosedError

        close_code = 1006
        if isinstance(exc, ConnectionClosedError) and exc.rcvd is not None:
            close_code = exc.rcvd.code

        if not is_recoverable_close(close_code):
            return False

        self._is_reconnecting = True

        for attempt in range(1, self._max_retries + 1):
            base_delay = min(self._initial_delay * (2 ** (attempt - 1)), self._max_delay)
            jitter = 0.75 + random.random() * 0.25
            delay = base_delay * jitter

            event = ReconnectingEvent(
                attempt=attempt,
                max_attempts=self._max_retries,
                delay=delay,
                close_code=close_code,
                extra_query=self._extra_query,
                extra_headers=self._extra_headers,
            )

            try:
                result = self._on_reconnecting(event)
            except Exception:
                self._is_reconnecting = False
                return False

            if result is not None and result.get("abort"):
                self._is_reconnecting = False
                return False

            if result is not None:
                if "extra_query" in result:
                    self._extra_query = result["extra_query"]
                if "extra_headers" in result:
                    self._extra_headers = result["extra_headers"]

            log.info(
                "Reconnecting to WebSocket API (attempt %d/%d) after %.1fs delay",
                attempt,
                self._max_retries,
                delay,
            )
            await asyncio.sleep(delay)

            if self._intentionally_closed:
                self._is_reconnecting = False
                return False

            try:
                self._connection = await self._make_ws(self._extra_query, self._extra_headers)
                log.info("Reconnected to WebSocket API")
                self._is_reconnecting = False
                await self._flush_send_queue()
                return True
            except Exception:
                pass

        self._is_reconnecting = False
        return False

    async def _flush_send_queue(self) -> None:
        """Send all queued messages over the current connection."""

        async def _send(data: str) -> None:
            await self._connection.send(data)

        try:
            await self._send_queue.flush_async(_send)
        except Exception:
            log.warning("Failed to flush send queue after reconnect", exc_info=True)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncTextToSpeechResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Adds the handler to the end of the handlers list for the given event type.

        No checks are made to see if the handler has already been added. Multiple calls
        passing the same combination of event type and handler will result in the handler
        being added, and called, multiple times.

        Can be used as a method (returns ``self`` for chaining)::

            connection.on("audio_chunk", my_handler)

        Or as a decorator::

            @connection.on("audio_chunk")
            async def my_handler(event): ...
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> AsyncTextToSpeechResourceConnection:
        """Remove a previously registered event handler."""
        self._event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncTextToSpeechResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler.

        Automatically removed after first invocation.
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    async def dispatch_events(self) -> None:
        """Run the event loop, dispatching received events to registered handlers.

        Blocks until the connection is closed. This is the push-based
        alternative to iterating with ``async for event in connection``.

        If an ``"error"`` event arrives and no handler is registered for
        ``"error"`` or ``"event"``, an ``TelnyxError`` is raised.
        """
        import asyncio

        async for event in self:
            event_type = event.type
            specific = self._event_handler_registry.get_handlers(event_type)
            generic = self._event_handler_registry.get_handlers("event")

            if event_type == "error" and not specific and not generic:
                if isinstance(event, ErrorFrame):
                    raise TelnyxError(f"WebSocket error: {event}")

            for handler in specific:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    await result

            for handler in generic:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    await result


class AsyncTextToSpeechResourceConnectionManager:
    """
    Context manager over a `AsyncTextToSpeechResourceConnection` that is returned by `text_to_speech.stream()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = await client.text_to_speech.stream(...).enter()
    # ...
    await connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: AsyncTelnyx,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> None:
        self.__client = client
        self.__connection: AsyncTextToSpeechResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options
        self.__on_reconnecting = on_reconnecting
        self.__max_retries = max_retries
        self.__initial_delay = initial_delay
        self.__max_delay = max_delay
        self.__send_queue = SendQueue(max_bytes=max_queue_size)
        self.__event_handler_registry = EventHandlerRegistry(use_lock=False)

    def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        """Queue a message to be sent when the connection is established.

        This can be called before entering the context manager. Queued messages
        are automatically sent once the WebSocket connection opens.
        """
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(event)
        )
        self.__send_queue.enqueue(data)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncTextToSpeechResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register an event handler before the connection is established.

        Handlers are transferred to the connection on enter. Supports the
        same method and decorator forms as ``AsyncTextToSpeechResourceConnection.on``.
        """
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> AsyncTextToSpeechResourceConnectionManager:
        """Remove a previously registered event handler."""
        self.__event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncTextToSpeechResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler before the connection is established."""
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    async def __aenter__(self) -> AsyncTextToSpeechResourceConnection:
        """
        If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.text_to_speech.stream(...).enter()
        # ...
        await connection.close()
        ```
        """
        ws = await self._connect_ws(self.__extra_query, self.__extra_headers)

        self.__connection = AsyncTextToSpeechResourceConnection(
            ws,
            make_ws=self._connect_ws if self.__on_reconnecting is not None else None,
            on_reconnecting=self.__on_reconnecting,
            max_retries=self.__max_retries,
            initial_delay=self.__initial_delay,
            max_delay=self.__max_delay,
            extra_query=self.__extra_query,
            extra_headers=self.__extra_headers,
            send_queue=self.__send_queue,
        )

        self.__event_handler_registry.merge_into(self.__connection._event_handler_registry)
        await self.__connection._flush_send_queue()

        return self.__connection

    enter = __aenter__

    async def _connect_ws(self, extra_query: Query, extra_headers: Headers) -> AsyncWebSocketConnection:
        try:
            from websockets.asyncio.client import connect
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        return await connect(
            str(url),
            user_agent_header=self.__client.user_agent,
            additional_headers=_merge_mappings(
                {
                    **self.__client.auth_headers,
                },
                extra_headers,
            ),
            **self.__websocket_connection_options,
        )

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/text-to-speech/speech"
        return base_url.copy_with(raw_path=merge_raw_path)

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class TextToSpeechResourceConnection:
    """Represents a live WebSocket connection to the TextToSpeech API"""

    _connection: WebSocketConnection

    def __init__(
        self,
        connection: WebSocketConnection,
        *,
        make_ws: Callable[[Query, Headers], WebSocketConnection] | None = None,
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        extra_query: Query = {},
        extra_headers: Headers = {},
        send_queue: SendQueue | None = None,
    ) -> None:
        self._connection = connection
        self._make_ws = make_ws
        self._on_reconnecting = on_reconnecting
        self._max_retries = max_retries
        self._initial_delay = initial_delay
        self._max_delay = max_delay
        self._extra_query = extra_query
        self._extra_headers = extra_headers
        self._intentionally_closed = False
        self._is_reconnecting = False
        self._send_queue = send_queue or SendQueue()
        self._event_handler_registry = EventHandlerRegistry(use_lock=True)

    def __iter__(self) -> Iterator[StreamServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK, ConnectionClosedError

        while True:
            try:
                yield self.recv()
            except ConnectionClosedOK:
                return
            except ConnectionClosedError as exc:
                if not self._reconnect(exc):
                    unsent = self._send_queue.drain()
                    if unsent:
                        raise WebSocketConnectionClosedError(
                            "WebSocket connection closed with unsent messages",
                            unsent_messages=unsent,
                        ) from exc
                    raise

    def recv(self) -> StreamServerEvent:
        """
        Receive the next message from the connection and parses it into a `StreamServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(self.recv_bytes())

    def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `StreamServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(maybe_transform(event, StreamClientEventParam))
        )
        if self._is_reconnecting:
            self._send_queue.enqueue(data)
            return
        try:
            self._connection.send(data)
        except Exception:
            self._send_queue.enqueue(data)
            raise

    def send_raw(self, data: bytes | str) -> None:
        if self._is_reconnecting:
            raw = data if isinstance(data, str) else data.decode("utf-8")
            self._send_queue.enqueue(raw)
            return
        self._connection.send(data)

    def close(self, *, code: int = 1000, reason: str = "") -> None:
        self._intentionally_closed = True
        self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> StreamServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `StreamServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            StreamServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, StreamServerEvent))
        )

    def _reconnect(self, exc: Exception) -> bool:
        """Attempt to reconnect after a connection failure.

        Returns ``True`` if a new connection was established, ``False`` if the
        caller should re-raise the original exception.
        """
        if self._on_reconnecting is None or self._make_ws is None:
            return False

        from websockets.exceptions import ConnectionClosedError

        close_code = 1006
        if isinstance(exc, ConnectionClosedError) and exc.rcvd is not None:
            close_code = exc.rcvd.code

        if not is_recoverable_close(close_code):
            return False

        self._is_reconnecting = True

        for attempt in range(1, self._max_retries + 1):
            base_delay = min(self._initial_delay * (2 ** (attempt - 1)), self._max_delay)
            jitter = 0.75 + random.random() * 0.25
            delay = base_delay * jitter

            event = ReconnectingEvent(
                attempt=attempt,
                max_attempts=self._max_retries,
                delay=delay,
                close_code=close_code,
                extra_query=self._extra_query,
                extra_headers=self._extra_headers,
            )

            try:
                result = self._on_reconnecting(event)
            except Exception:
                self._is_reconnecting = False
                return False

            if result is not None and result.get("abort"):
                self._is_reconnecting = False
                return False

            if result is not None:
                if "extra_query" in result:
                    self._extra_query = result["extra_query"]
                if "extra_headers" in result:
                    self._extra_headers = result["extra_headers"]

            log.info(
                "Reconnecting to WebSocket API (attempt %d/%d) after %.1fs delay",
                attempt,
                self._max_retries,
                delay,
            )
            time.sleep(delay)

            if self._intentionally_closed:
                self._is_reconnecting = False
                return False

            try:
                self._connection = self._make_ws(self._extra_query, self._extra_headers)
                log.info("Reconnected to WebSocket API")
                self._is_reconnecting = False
                self._flush_send_queue()
                return True
            except Exception:
                pass

        self._is_reconnecting = False
        return False

    def _flush_send_queue(self) -> None:
        """Send all queued messages over the current connection."""
        try:
            self._send_queue.flush_sync(lambda data: self._connection.send(data))
        except Exception:
            log.warning("Failed to flush send queue after reconnect", exc_info=True)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[TextToSpeechResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Adds the handler to the end of the handlers list for the given event type.

        No checks are made to see if the handler has already been added. Multiple calls
        passing the same combination of event type and handler will result in the handler
        being added, and called, multiple times.

        Can be used as a method (returns ``self`` for chaining)::

            connection.on("audio_chunk", my_handler)

        Or as a decorator::

            @connection.on("audio_chunk")
            def my_handler(event): ...
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> TextToSpeechResourceConnection:
        """Remove a previously registered event handler."""
        self._event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[TextToSpeechResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler.

        Automatically removed after first invocation.
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    def dispatch_events(self) -> None:
        """Run the event loop, dispatching received events to registered handlers.

        Blocks the current thread until the connection is closed. This is the push-based
        alternative to iterating with ``for event in connection``.

        If an ``"error"`` event arrives and no handler is registered for
        ``"error"`` or ``"event"``, an ``TelnyxError`` is raised.
        """
        for event in self:
            event_type = event.type
            specific = self._event_handler_registry.get_handlers(event_type)
            generic = self._event_handler_registry.get_handlers("event")

            if event_type == "error" and not specific and not generic:
                if isinstance(event, ErrorFrame):
                    raise TelnyxError(f"WebSocket error: {event}")

            for handler in specific:
                handler(event)

            for handler in generic:
                handler(event)


class TextToSpeechResourceConnectionManager:
    """
    Context manager over a `TextToSpeechResourceConnection` that is returned by `text_to_speech.stream()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = client.text_to_speech.stream(...).enter()
    # ...
    connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: Telnyx,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> None:
        self.__client = client
        self.__connection: TextToSpeechResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options
        self.__on_reconnecting = on_reconnecting
        self.__max_retries = max_retries
        self.__initial_delay = initial_delay
        self.__max_delay = max_delay
        self.__send_queue = SendQueue(max_bytes=max_queue_size)
        self.__event_handler_registry = EventHandlerRegistry(use_lock=True)

    def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        """Queue a message to be sent when the connection is established.

        This can be called before entering the context manager. Queued messages
        are automatically sent once the WebSocket connection opens.
        """
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(event)
        )
        self.__send_queue.enqueue(data)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[TextToSpeechResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register an event handler before the connection is established.

        Handlers are transferred to the connection on enter. Supports the
        same method and decorator forms as ``TextToSpeechResourceConnection.on``.
        """
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> TextToSpeechResourceConnectionManager:
        """Remove a previously registered event handler."""
        self.__event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[TextToSpeechResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler before the connection is established."""
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    def __enter__(self) -> TextToSpeechResourceConnection:
        """
        If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.text_to_speech.stream(...).enter()
        # ...
        connection.close()
        ```
        """
        ws = self._connect_ws(self.__extra_query, self.__extra_headers)

        self.__connection = TextToSpeechResourceConnection(
            ws,
            make_ws=self._connect_ws if self.__on_reconnecting is not None else None,
            on_reconnecting=self.__on_reconnecting,
            max_retries=self.__max_retries,
            initial_delay=self.__initial_delay,
            max_delay=self.__max_delay,
            extra_query=self.__extra_query,
            extra_headers=self.__extra_headers,
            send_queue=self.__send_queue,
        )

        self.__event_handler_registry.merge_into(self.__connection._event_handler_registry)
        self.__connection._flush_send_queue()

        return self.__connection

    enter = __enter__

    def _connect_ws(self, extra_query: Query, extra_headers: Headers) -> WebSocketConnection:
        try:
            from websockets.sync.client import connect
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        return connect(
            str(url),
            user_agent_header=self.__client.user_agent,
            additional_headers=_merge_mappings(
                {
                    **self.__client.auth_headers,
                },
                extra_headers,
            ),
            **self.__websocket_connection_options,
        )

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/text-to-speech/speech"
        return base_url.copy_with(raw_path=merge_raw_path)

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
