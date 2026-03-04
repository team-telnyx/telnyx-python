# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Dict, Iterator, cast
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
from .._exceptions import TelnyxError
from .._base_client import _merge_mappings, make_request_options
from ..types.stream_client_event import StreamClientEvent
from ..types.stream_server_event import StreamServerEvent
from ..types.stream_client_event_param import StreamClientEventParam
from ..types.websocket_connection_options import WebsocketConnectionOptions
from ..types.text_to_speech_generate_response import TextToSpeechGenerateResponse
from ..types.text_to_speech_list_voices_response import TextToSpeechListVoicesResponse

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebsocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebsocketConnection

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
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebsocketConnectionOptions = {},
    ) -> TextToSpeechResourceConnectionManager:
        return TextToSpeechResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
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

    def stream(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebsocketConnectionOptions = {},
    ) -> AsyncTextToSpeechResourceConnectionManager:
        return AsyncTextToSpeechResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
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

    _connection: AsyncWebsocketConnection

    def __init__(self, connection: AsyncWebsocketConnection) -> None:
        self._connection = connection

    async def __aiter__(self) -> AsyncIterator[StreamServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK

        try:
            while True:
                yield await self.recv()
        except ConnectionClosedOK:
            return

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
        log.debug(f"Received websocket message: %s", message)
        return message

    async def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(await async_maybe_transform(event, StreamClientEventParam))
        )
        await self._connection.send(data)

    async def close(self, *, code: int = 1000, reason: str = "") -> None:
        await self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> StreamServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `StreamServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            StreamServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, StreamServerEvent))
        )


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
        websocket_connection_options: WebsocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: AsyncTextToSpeechResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    async def __aenter__(self) -> AsyncTextToSpeechResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.text_to_speech.stream(...).enter()
        # ...
        await connection.close()
        ```
        """
        try:
            from websockets.asyncio.client import connect
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **self.__extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        self.__connection = AsyncTextToSpeechResourceConnection(
            await connect(
                str(url),
                user_agent_header=self.__client.user_agent,
                additional_headers=_merge_mappings(
                    {
                        **self.__client.auth_headers,
                    },
                    self.__extra_headers,
                ),
                **self.__websocket_connection_options,
            )
        )

        return self.__connection

    enter = __aenter__

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            base_url = self.__client._base_url.copy_with(scheme="wss")

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/text-to-speech/speech"
        return base_url.copy_with(raw_path=merge_raw_path)

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class TextToSpeechResourceConnection:
    """Represents a live WebSocket connection to the TextToSpeech API"""

    _connection: WebsocketConnection

    def __init__(self, connection: WebsocketConnection) -> None:
        self._connection = connection

    def __iter__(self) -> Iterator[StreamServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK

        try:
            while True:
                yield self.recv()
        except ConnectionClosedOK:
            return

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
        log.debug(f"Received websocket message: %s", message)
        return message

    def send(self, event: StreamClientEvent | StreamClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(maybe_transform(event, StreamClientEventParam))
        )
        self._connection.send(data)

    def close(self, *, code: int = 1000, reason: str = "") -> None:
        self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> StreamServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `StreamServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            StreamServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, StreamServerEvent))
        )


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
        websocket_connection_options: WebsocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: TextToSpeechResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    def __enter__(self) -> TextToSpeechResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.text_to_speech.stream(...).enter()
        # ...
        connection.close()
        ```
        """
        try:
            from websockets.sync.client import connect
        except ImportError as exc:
            raise TelnyxError("You need to install `telnyx[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **self.__extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        self.__connection = TextToSpeechResourceConnection(
            connect(
                str(url),
                user_agent_header=self.__client.user_agent,
                additional_headers=_merge_mappings(
                    {
                        **self.__client.auth_headers,
                    },
                    self.__extra_headers,
                ),
                **self.__websocket_connection_options,
            )
        )

        return self.__connection

    enter = __enter__

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            base_url = self.__client._base_url.copy_with(scheme="wss")

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/text-to-speech/speech"
        return base_url.copy_with(raw_path=merge_raw_path)

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
