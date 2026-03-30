# Custom code for WebSocket streaming support - persists across codegen runs.

from __future__ import annotations

import json
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Iterator, cast
from typing_extensions import AsyncIterator
from urllib.parse import urlencode

import httpx

from .._types import Query, Headers
from .._compat import cached_property
from .._models import construct_type_unchecked
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import TelnyxError
from .._base_client import _merge_mappings
from ..types.stt_server_event import SttServerEvent
from ..types.speech_to_text_stream_params import SpeechToTextStreamParams
from ..types.websocket_connection_options import WebSocketConnectionOptions

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebSocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebSocketConnection

    from .._client import Telnyx, AsyncTelnyx

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]

log: logging.Logger = logging.getLogger(__name__)


class SpeechToTextResource(SyncAPIResource):
    """Speech to text streaming operations via WebSocket.

    Connect to `wss://api.telnyx.com/v2/speech-to-text/transcription` with query
    parameters specifying the transcription engine, input format, and language.
    Send binary audio frames and receive JSON transcription events.
    """

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

    def stream(
        self,
        params: SpeechToTextStreamParams,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
    ) -> SpeechToTextResourceConnectionManager:
        """Open a WebSocket connection to stream audio and receive transcriptions.

        Authentication is provided via the standard `Authorization: Bearer <API_KEY>` header.

        Supported engines: Azure, Deepgram, Google, Telnyx.

        **Connection flow:**

        1. Open WebSocket with query parameters specifying engine, input format, and language.
        2. Send binary audio frames (mp3/wav/raw format) using `.send(audio_bytes)`.
        3. Receive JSON transcript frames with `transcript`, `is_final`, and `confidence` fields.
        4. Close connection when done.

        Example:

            ```python
            from telnyx import Telnyx

            client = Telnyx()

            with client.speech_to_text.stream({
                "transcription_engine": "Deepgram",
                "input_format": "wav",
                "language": "en-US",
                "interim_results": True,
            }) as connection:
                # Send audio data
                connection.send(audio_bytes)

                # Receive transcripts
                for event in connection:
                    if hasattr(event, 'transcript'):
                        print(f"Transcript: {event.transcript}")
                        if event.is_final:
                            print("(final)")
            ```

        Args:
            params: Parameters for the STT connection (transcription_engine, input_format, etc.)
            extra_query: Additional query parameters to include in the WebSocket URL
            extra_headers: Additional headers to include in the WebSocket connection
            websocket_connection_options: Additional WebSocket connection options

        Returns:
            A connection manager that can be used as a context manager
        """
        return SpeechToTextResourceConnectionManager(
            client=self._client,
            params=params,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
    """Speech to text streaming operations via WebSocket (async).

    Connect to `wss://api.telnyx.com/v2/speech-to-text/transcription` with query
    parameters specifying the transcription engine, input format, and language.
    Send binary audio frames and receive JSON transcription events.
    """

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

    def stream(
        self,
        params: SpeechToTextStreamParams,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
    ) -> AsyncSpeechToTextResourceConnectionManager:
        """Open a WebSocket connection to stream audio and receive transcriptions (async).

        Authentication is provided via the standard `Authorization: Bearer <API_KEY>` header.

        Supported engines: Azure, Deepgram, Google, Telnyx.

        **Connection flow:**

        1. Open WebSocket with query parameters specifying engine, input format, and language.
        2. Send binary audio frames (mp3/wav/raw format) using `await .send(audio_bytes)`.
        3. Receive JSON transcript frames with `transcript`, `is_final`, and `confidence` fields.
        4. Close connection when done.

        Example:

            ```python
            import asyncio
            from telnyx import AsyncTelnyx

            async def main():
                client = AsyncTelnyx()

                async with client.speech_to_text.stream({
                    "transcription_engine": "Deepgram",
                    "input_format": "wav",
                    "language": "en-US",
                    "interim_results": True,
                }) as connection:
                    # Send audio data
                    await connection.send(audio_bytes)

                    # Receive transcripts
                    async for event in connection:
                        if hasattr(event, 'transcript'):
                            print(f"Transcript: {event.transcript}")
                            if event.is_final:
                                print("(final)")

            asyncio.run(main())
            ```

        Args:
            params: Parameters for the STT connection (transcription_engine, input_format, etc.)
            extra_query: Additional query parameters to include in the WebSocket URL
            extra_headers: Additional headers to include in the WebSocket connection
            websocket_connection_options: Additional WebSocket connection options

        Returns:
            A connection manager that can be used as an async context manager
        """
        return AsyncSpeechToTextResourceConnectionManager(
            client=self._client,
            params=params,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class SpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class AsyncSpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text


class AsyncSpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API (async)."""

    _connection: AsyncWebSocketConnection

    def __init__(self, connection: AsyncWebSocketConnection) -> None:
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
        log.debug(f"Received WebSocket message: %s", message)
        return message

    async def send(self, data: bytes) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            data: Raw audio bytes (mp3, wav, or raw format depending on input_format parameter)
        """
        await self._connection.send(data)

    async def close(self, *, code: int = 1000, reason: str = "") -> None:
        """Close the WebSocket connection."""
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
    connection = await client.speech_to_text.stream({...}).enter()
    # ...
    await connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: AsyncTelnyx,
        params: SpeechToTextStreamParams,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__params = params
        self.__connection: AsyncSpeechToTextResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    async def __aenter__(self) -> AsyncSpeechToTextResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.speech_to_text.stream({...}).enter()
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
                **self._params_to_query(),
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
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path)

    def _params_to_query(self) -> dict[str, Any]:
        """Convert SpeechToTextStreamParams to query parameters."""
        query: dict[str, Any] = {}
        for key, value in self.__params.items():
            if value is not None:
                # Convert boolean to lowercase string
                if isinstance(value, bool):
                    query[key] = str(value).lower()
                else:
                    query[key] = value
        return query

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class SpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API (sync)."""

    _connection: WebSocketConnection

    def __init__(self, connection: WebSocketConnection) -> None:
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
        log.debug(f"Received WebSocket message: %s", message)
        return message

    def send(self, data: bytes) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            data: Raw audio bytes (mp3, wav, or raw format depending on input_format parameter)
        """
        self._connection.send(data)

    def close(self, *, code: int = 1000, reason: str = "") -> None:
        """Close the WebSocket connection."""
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
    connection = client.speech_to_text.stream({...}).enter()
    # ...
    connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: Telnyx,
        params: SpeechToTextStreamParams,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__params = params
        self.__connection: SpeechToTextResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    def __enter__(self) -> SpeechToTextResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.speech_to_text.stream({...}).enter()
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
                **self._params_to_query(),
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
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path)

    def _params_to_query(self) -> dict[str, Any]:
        """Convert SpeechToTextStreamParams to query parameters."""
        query: dict[str, Any] = {}
        for key, value in self.__params.items():
            if value is not None:
                # Convert boolean to lowercase string
                if isinstance(value, bool):
                    query[key] = str(value).lower()
                else:
                    query[key] = value
        return query

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
