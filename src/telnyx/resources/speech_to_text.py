# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import time
import random
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Union, Callable, Iterator, Awaitable, cast
from typing_extensions import Literal, AsyncIterator

import httpx
from pydantic import BaseModel

from ..types import speech_to_text_list_providers_params
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
from ..types.websocket_reconnection import ReconnectingEvent, ReconnectingOverrides, is_recoverable_close
from ..types.transcribe_client_event import TranscribeClientEvent
from ..types.transcribe_server_event import SttErrorFrame, TranscribeServerEvent
from ..types.websocket_connection_options import WebSocketConnectionOptions
from ..types.speech_to_text_list_providers_response import SpeechToTextListProvidersResponse

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebSocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebSocketConnection

    from .._client import Telnyx, AsyncTelnyx

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]

log: logging.Logger = logging.getLogger(__name__)


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
            "deepgram", "speechmatics", "assemblyai", "xai", "soniox", "azure", "openai", "google", "telnyx"
        ]
        | Omit = omit,
        service_type: Literal["streaming", "file_transcription", "in_call_transcription"] | Omit = omit,
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
        - `file_transcription` — file-based transcription via
          `/ai/audio/transcriptions`.
        - `in_call_transcription` — live call transcription via Call Control
          `transcription_start`.

        Use this endpoint to discover which (provider, model) combinations are available
        for the surface you need, and which language codes each accepts. `auto` in a
        `languages` array indicates the provider performs language detection.

        Args:
          provider: Filter to entries for a specific STT provider. The enum mirrors the providers
              advertised across the speech-to-text spec (including `google` and `telnyx`,
              which are accepted as WebSocket transcription engines). A provider that has no
              models currently registered for any service type will return an empty `data`
              array rather than an error.

          service_type: Filter to entries that support the given service type.

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

    def transcribe(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> SpeechToTextResourceConnectionManager:
        return SpeechToTextResourceConnectionManager(
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
            "deepgram", "speechmatics", "assemblyai", "xai", "soniox", "azure", "openai", "google", "telnyx"
        ]
        | Omit = omit,
        service_type: Literal["streaming", "file_transcription", "in_call_transcription"] | Omit = omit,
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
        - `file_transcription` — file-based transcription via
          `/ai/audio/transcriptions`.
        - `in_call_transcription` — live call transcription via Call Control
          `transcription_start`.

        Use this endpoint to discover which (provider, model) combinations are available
        for the surface you need, and which language codes each accepts. `auto` in a
        `languages` array indicates the provider performs language detection.

        Args:
          provider: Filter to entries for a specific STT provider. The enum mirrors the providers
              advertised across the speech-to-text spec (including `google` and `telnyx`,
              which are accepted as WebSocket transcription engines). A provider that has no
              models currently registered for any service type will return an empty `data`
              array rather than an error.

          service_type: Filter to entries that support the given service type.

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

    def transcribe(
        self,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> AsyncSpeechToTextResourceConnectionManager:
        return AsyncSpeechToTextResourceConnectionManager(
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


class AsyncSpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API"""

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

    async def __aiter__(self) -> AsyncIterator[TranscribeServerEvent]:
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

    async def recv(self) -> TranscribeServerEvent:
        """
        Receive the next message from the connection and parses it into a `TranscribeServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(await self.recv_bytes())

    async def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `TranscribeServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = await self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    async def send(self, event: TranscribeClientEvent | TranscribeClientEvent) -> None:
        data = (
            event.model_dump_json(by_alias=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(await async_maybe_transform(event, TranscribeClientEvent))
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

    def parse_event(self, data: str | bytes) -> TranscribeServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `TranscribeServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            TranscribeServerEvent,
            construct_type_unchecked(value=json.loads(data), type_=cast(Any, TranscribeServerEvent)),
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
    ) -> Union[AsyncSpeechToTextResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Adds the handler to the end of the handlers list for the given event type.

        No checks are made to see if the handler has already been added. Multiple calls
        passing the same combination of event type and handler will result in the handler
        being added, and called, multiple times.

        Can be used as a method (returns ``self`` for chaining)::

            connection.on("transcript", my_handler)

        Or as a decorator::

            @connection.on("transcript")
            async def my_handler(event): ...
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> AsyncSpeechToTextResourceConnection:
        """Remove a previously registered event handler."""
        self._event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncSpeechToTextResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
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
                if isinstance(event, SttErrorFrame):
                    raise TelnyxError(f"WebSocket error: {event}")

            for handler in specific:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    await result

            for handler in generic:
                result = handler(event)
                if asyncio.iscoroutine(result):
                    await result


class AsyncSpeechToTextResourceConnectionManager:
    """
    Context manager over a `AsyncSpeechToTextResourceConnection` that is returned by `speech_to_text.transcribe()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = await client.speech_to_text.transcribe(...).enter()
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
        self.__connection: AsyncSpeechToTextResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options
        self.__on_reconnecting = on_reconnecting
        self.__max_retries = max_retries
        self.__initial_delay = initial_delay
        self.__max_delay = max_delay
        self.__send_queue = SendQueue(max_bytes=max_queue_size)
        self.__event_handler_registry = EventHandlerRegistry(use_lock=False)

    def send(self, event: TranscribeClientEvent | TranscribeClientEvent) -> None:
        """Queue a message to be sent when the connection is established.

        This can be called before entering the context manager. Queued messages
        are automatically sent once the WebSocket connection opens.
        """
        data = (
            event.model_dump_json(by_alias=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(event)
        )
        self.__send_queue.enqueue(data)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncSpeechToTextResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register an event handler before the connection is established.

        Handlers are transferred to the connection on enter. Supports the
        same method and decorator forms as ``AsyncSpeechToTextResourceConnection.on``.
        """
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> AsyncSpeechToTextResourceConnectionManager:
        """Remove a previously registered event handler."""
        self.__event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[AsyncSpeechToTextResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler before the connection is established."""
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    async def __aenter__(self) -> AsyncSpeechToTextResourceConnection:
        """
        If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.speech_to_text.transcribe(...).enter()
        # ...
        await connection.close()
        ```
        """
        ws = await self._connect_ws(self.__extra_query, self.__extra_headers)

        self.__connection = AsyncSpeechToTextResourceConnection(
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

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path)

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class SpeechToTextResourceConnection:
    """Represents a live WebSocket connection to the SpeechToText API"""

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

    def __iter__(self) -> Iterator[TranscribeServerEvent]:
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

    def recv(self) -> TranscribeServerEvent:
        """
        Receive the next message from the connection and parses it into a `TranscribeServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(self.recv_bytes())

    def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `TranscribeServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    def send(self, event: TranscribeClientEvent | TranscribeClientEvent) -> None:
        data = (
            event.model_dump_json(by_alias=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(maybe_transform(event, TranscribeClientEvent))
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

    def parse_event(self, data: str | bytes) -> TranscribeServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `TranscribeServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            TranscribeServerEvent,
            construct_type_unchecked(value=json.loads(data), type_=cast(Any, TranscribeServerEvent)),
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
    ) -> Union[SpeechToTextResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Adds the handler to the end of the handlers list for the given event type.

        No checks are made to see if the handler has already been added. Multiple calls
        passing the same combination of event type and handler will result in the handler
        being added, and called, multiple times.

        Can be used as a method (returns ``self`` for chaining)::

            connection.on("transcript", my_handler)

        Or as a decorator::

            @connection.on("transcript")
            def my_handler(event): ...
        """
        if handler is not None:
            self._event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self._event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> SpeechToTextResourceConnection:
        """Remove a previously registered event handler."""
        self._event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[SpeechToTextResourceConnection, Callable[[Callable[..., Any]], Callable[..., Any]]]:
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
                if isinstance(event, SttErrorFrame):
                    raise TelnyxError(f"WebSocket error: {event}")

            for handler in specific:
                handler(event)

            for handler in generic:
                handler(event)


class SpeechToTextResourceConnectionManager:
    """
    Context manager over a `SpeechToTextResourceConnection` that is returned by `speech_to_text.transcribe()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = client.speech_to_text.transcribe(...).enter()
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
        self.__connection: SpeechToTextResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options
        self.__on_reconnecting = on_reconnecting
        self.__max_retries = max_retries
        self.__initial_delay = initial_delay
        self.__max_delay = max_delay
        self.__send_queue = SendQueue(max_bytes=max_queue_size)
        self.__event_handler_registry = EventHandlerRegistry(use_lock=True)

    def send(self, event: TranscribeClientEvent | TranscribeClientEvent) -> None:
        """Queue a message to be sent when the connection is established.

        This can be called before entering the context manager. Queued messages
        are automatically sent once the WebSocket connection opens.
        """
        data = (
            event.model_dump_json(by_alias=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(event)
        )
        self.__send_queue.enqueue(data)

    def on(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[SpeechToTextResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register an event handler before the connection is established.

        Handlers are transferred to the connection on enter. Supports the
        same method and decorator forms as ``SpeechToTextResourceConnection.on``.
        """
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn)
            return fn

        return decorator

    def off(self, event_type: str, handler: Callable[..., Any]) -> SpeechToTextResourceConnectionManager:
        """Remove a previously registered event handler."""
        self.__event_handler_registry.remove(event_type, handler)
        return self

    def once(
        self, event_type: str, handler: Callable[..., Any] | None = None
    ) -> Union[SpeechToTextResourceConnectionManager, Callable[[Callable[..., Any]], Callable[..., Any]]]:
        """Register a one-time event handler before the connection is established."""
        if handler is not None:
            self.__event_handler_registry.add(event_type, handler, once=True)
            return self

        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            self.__event_handler_registry.add(event_type, fn, once=True)
            return fn

        return decorator

    def __enter__(self) -> SpeechToTextResourceConnection:
        """
        If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.speech_to_text.transcribe(...).enter()
        # ...
        connection.close()
        ```
        """
        ws = self._connect_ws(self.__extra_query, self.__extra_headers)

        self.__connection = SpeechToTextResourceConnection(
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

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/speech-to-text/transcription"
        return base_url.copy_with(raw_path=merge_raw_path)

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
