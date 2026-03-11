# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Union, Iterator, cast
from typing_extensions import Literal, AsyncIterator

import httpx

from .._types import Query, Headers
from .._compat import cached_property
from .._models import construct_type_unchecked
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import TelnyxError
from .._base_client import _merge_mappings
from ..types.stt_server_event import SttServerEvent
from ..types.websocket_connection_options import WebsocketConnectionOptions

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebsocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebsocketConnection

    from .._client import Telnyx, AsyncTelnyx

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]

log: logging.Logger = logging.getLogger(__name__)

# Type alias for binary audio data
SttClientEvent = Union[bytes, bytearray, memoryview]


class SpeechToTextResource(SyncAPIResource):
    """Speech to text streaming command operations via WebSocket"""

    @cached_property
    def with_raw_response(self) -> SpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SpeechToTextResourceWithRawResponse(self)

    def stream(
        self,
        *,
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        input_format: Literal["mp3", "wav", "raw"] | None = None,
        language: str | None = None,
        interim_results: bool | None = None,
        model: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        websocket_connection_options: WebsocketConnectionOptions = {},
    ) -> SpeechToTextResourceConnectionManager:
        """
        Create a WebSocket connection for real-time speech-to-text transcription.

        Args:
          transcription_engine: The transcription engine to use for processing the audio stream.
              Supported engines: `Azure`, `Deepgram`, `Google`, `Telnyx`.

          input_format: The format of the input audio stream. Defaults to `wav`.

          language: The language code for transcription (e.g., 'en-US', 'es-ES').

          interim_results: Whether to return interim (partial) transcription results.

          model: The model to use for transcription (engine-specific).

          extra_headers: Additional headers to send with the request.

          extra_query: Additional query parameters to send with the request.

          websocket_connection_options: Additional options for the WebSocket connection.

        Returns:
          A context manager that yields a `SpeechToTextResourceConnection` when entered.

        Example:
            ```python
            with client.speech_to_text.stream(transcription_engine="Telnyx") as connection:
                connection.send(audio_data)
                for event in connection:
                    if event.type == "transcript":
                        print(event.transcript)
            ```
        """
        return SpeechToTextResourceConnectionManager(
            client=self._client,
            transcription_engine=transcription_engine,
            input_format=input_format,
            language=language,
            interim_results=interim_results,
            model=model,
            extra_query=extra_query or {},
            extra_headers=extra_headers or {},
            websocket_connection_options=websocket_connection_options,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
    """Speech to text streaming command operations via WebSocket"""

    @cached_property
    def with_raw_response(self) -> AsyncSpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechToTextResourceWithRawResponse(self)

    def stream(
        self,
        *,
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        input_format: Literal["mp3", "wav", "raw"] | None = None,
        language: str | None = None,
        interim_results: bool | None = None,
        model: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        websocket_connection_options: WebsocketConnectionOptions = {},
    ) -> AsyncSpeechToTextResourceConnectionManager:
        """
        Create a WebSocket connection for real-time speech-to-text transcription.

        Args:
          transcription_engine: The transcription engine to use for processing the audio stream.
              Supported engines: `Azure`, `Deepgram`, `Google`, `Telnyx`.

          input_format: The format of the input audio stream. Defaults to `wav`.

          language: The language code for transcription (e.g., 'en-US', 'es-ES').

          interim_results: Whether to return interim (partial) transcription results.

          model: The model to use for transcription (engine-specific).

          extra_headers: Additional headers to send with the request.

          extra_query: Additional query parameters to send with the request.

          websocket_connection_options: Additional options for the WebSocket connection.

        Returns:
          A context manager that yields an `AsyncSpeechToTextResourceConnection` when entered.

        Example:
            ```python
            async with client.speech_to_text.stream(transcription_engine="Telnyx") as connection:
                await connection.send(audio_data)
                async for event in connection:
                    if event.type == "transcript":
                        print(event.transcript)
            ```
        """
        return AsyncSpeechToTextResourceConnectionManager(
            client=self._client,
            transcription_engine=transcription_engine,
            input_format=input_format,
            language=language,
            interim_results=interim_results,
            model=model,
            extra_query=extra_query or {},
            extra_headers=extra_headers or {},
            websocket_connection_options=websocket_connection_options,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class AsyncSpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API"""

    _connection: AsyncWebsocketConnection

    def __init__(self, connection: AsyncWebsocketConnection) -> None:
        self._connection = connection

    async def __aiter__(self) -> AsyncIterator[SttServerEvent]:
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

    async def recv(self) -> SttServerEvent:
        """
        Receive the next message from the connection and parses it into a `SttServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(await self.recv_bytes())

    async def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `SttServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = await self._connection.recv(decode=False)
        log.debug(f"Received websocket message: %s", message)
        return message

    async def send(self, data: SttClientEvent) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            data: Raw audio bytes (mp3, wav, or raw format depending on input_format parameter).
        """
        await self._connection.send(data)

    async def close(self, *, code: int = 1000, reason: str = "") -> None:
        await self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> SttServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `SttServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            SttServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, SttServerEvent))
        )


class AsyncSpeechToTextResourceConnectionManager:
    """
    Context manager over a `AsyncSpeechToTextResourceConnection` that is returned by `speech_to_text.stream()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = await client.speech_to_text.stream(...).enter()
    # ...
    await connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: AsyncTelnyx,
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        input_format: Literal["mp3", "wav", "raw"] | None,
        language: str | None,
        interim_results: bool | None,
        model: str | None,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebsocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: AsyncSpeechToTextResourceConnection | None = None
        self.__transcription_engine = transcription_engine
        self.__input_format = input_format
        self.__language = language
        self.__interim_results = interim_results
        self.__model = model
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    async def __aenter__(self) -> AsyncSpeechToTextResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.speech_to_text.stream(...).enter()
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

        self.__connection = AsyncSpeechToTextResourceConnection(
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

        # Build query parameters
        params = {"transcription_engine": self.__transcription_engine}
        if self.__input_format is not None:
            params["input_format"] = self.__input_format
        if self.__language is not None:
            params["language"] = self.__language
        if self.__interim_results is not None:
            params["interim_results"] = str(self.__interim_results).lower()
        if self.__model is not None:
            params["model"] = self.__model

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path, params=params)

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class SpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API"""

    _connection: WebsocketConnection

    def __init__(self, connection: WebsocketConnection) -> None:
        self._connection = connection

    def __iter__(self) -> Iterator[SttServerEvent]:
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

    def recv(self) -> SttServerEvent:
        """
        Receive the next message from the connection and parses it into a `SttServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(self.recv_bytes())

    def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `SttServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = self._connection.recv(decode=False)
        log.debug(f"Received websocket message: %s", message)
        return message

    def send(self, data: SttClientEvent) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            data: Raw audio bytes (mp3, wav, or raw format depending on input_format parameter).
        """
        self._connection.send(data)

    def close(self, *, code: int = 1000, reason: str = "") -> None:
        self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> SttServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `SttServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            SttServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, SttServerEvent))
        )


class SpeechToTextResourceConnectionManager:
    """
    Context manager over a `SpeechToTextResourceConnection` that is returned by `speech_to_text.stream()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = client.speech_to_text.stream(...).enter()
    # ...
    connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: Telnyx,
        transcription_engine: Literal["Azure", "Deepgram", "Google", "Telnyx"],
        input_format: Literal["mp3", "wav", "raw"] | None,
        language: str | None,
        interim_results: bool | None,
        model: str | None,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebsocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: SpeechToTextResourceConnection | None = None
        self.__transcription_engine = transcription_engine
        self.__input_format = input_format
        self.__language = language
        self.__interim_results = interim_results
        self.__model = model
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    def __enter__(self) -> SpeechToTextResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.speech_to_text.stream(...).enter()
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

        self.__connection = SpeechToTextResourceConnection(
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

        # Build query parameters
        params = {"transcription_engine": self.__transcription_engine}
        if self.__input_format is not None:
            params["input_format"] = self.__input_format
        if self.__language is not None:
            params["language"] = self.__language
        if self.__interim_results is not None:
            params["interim_results"] = str(self.__interim_results).lower()
        if self.__model is not None:
            params["model"] = self.__model

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path, params=params)

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
