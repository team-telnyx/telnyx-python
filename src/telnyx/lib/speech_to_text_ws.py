"""
Speech-to-Text WebSocket streaming client for Telnyx.

This module provides WebSocket-based real-time speech transcription
using Telnyx's Speech-to-Text API. It supports both synchronous and
asynchronous usage patterns.

Example (Synchronous):
    from telnyx.lib import SpeechToTextWS, SpeechToTextStreamParams

    params = SpeechToTextStreamParams(
        transcription_engine="Deepgram",
        language="en-US",
        input_format="wav",
    )

    with SpeechToTextWS(api_key="YOUR_API_KEY", params=params) as ws:
        ws.send(audio_bytes)
        for event in ws.events():
            if event.type == "transcript":
                print(f"Transcript: {event.transcript} (final: {event.is_final})")

Example (Async):
    from telnyx.lib import AsyncSpeechToTextWS, SpeechToTextStreamParams

    params = SpeechToTextStreamParams(
        transcription_engine="Deepgram",
        language="en-US",
        input_format="wav",
    )

    async with AsyncSpeechToTextWS(api_key="YOUR_API_KEY", params=params) as ws:
        await ws.send(audio_bytes)
        async for event in ws.events():
            if event.type == "transcript":
                print(f"Transcript: {event.transcript} (final: {event.is_final})")
"""

from __future__ import annotations

import json
import threading
from queue import Empty, Queue
from typing import TYPE_CHECKING, Any, List, Iterator, Optional, cast
from dataclasses import field, dataclass
from urllib.parse import urlparse, urlencode
from typing_extensions import override

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

__all__ = [
    "SpeechToTextStreamParams",
    "SttEvent",
    "SttWord",
    "SpeechToTextWS",
    "AsyncSpeechToTextWS",
    "SpeechToTextWSError",
]


class SpeechToTextWSError(Exception):
    """Exception raised for Speech-to-Text WebSocket errors."""

    def __init__(self, message: str, cause: Optional[Exception] = None) -> None:
        super().__init__(message)
        self.message = message
        self.cause = cause

    @override
    def __str__(self) -> str:
        if self.cause:
            return f"{self.message}: {self.cause}"
        return self.message


@dataclass
class SpeechToTextStreamParams:
    """Parameters for establishing a Speech-to-Text WebSocket connection.

    Attributes:
        transcription_engine: The STT engine to use (e.g., "Deepgram", "Telnyx", "Azure", "Google").
        input_format: The audio format (e.g., "wav", "mp3", "raw").
        language: The language code (e.g., "en-US", "es-ES").
        sample_rate: The audio sample rate in Hz (e.g., 8000, 16000, 44100).
        channels: The number of audio channels (1 for mono, 2 for stereo).
        interim_results: Enable interim (non-final) transcription results.
        model: The transcription model to use.
        encoding: The audio encoding (e.g., "linear16", "mulaw").
        endpointing: Endpointing configuration in milliseconds.
        keywords: Keywords to boost recognition accuracy (comma-separated).
    """

    transcription_engine: Optional[str] = None
    input_format: Optional[str] = None
    language: Optional[str] = None
    sample_rate: Optional[int] = None
    channels: Optional[int] = None
    interim_results: Optional[bool] = None
    model: Optional[str] = None
    encoding: Optional[str] = None
    endpointing: Optional[int] = None
    keywords: Optional[str] = None

    def to_query_params(self) -> dict[str, str]:
        """Convert parameters to URL query parameters."""
        params: dict[str, str] = {}

        if self.transcription_engine is not None:
            params["transcription_engine"] = self.transcription_engine
        if self.input_format is not None:
            params["input_format"] = self.input_format
        if self.language is not None:
            params["language"] = self.language
        if self.sample_rate is not None:
            params["sample_rate"] = str(self.sample_rate)
        if self.channels is not None:
            params["channels"] = str(self.channels)
        if self.interim_results is not None:
            params["interim_results"] = "true" if self.interim_results else "false"
        if self.model is not None:
            params["model"] = self.model
        if self.encoding is not None:
            params["encoding"] = self.encoding
        if self.endpointing is not None:
            params["endpointing"] = str(self.endpointing)
        if self.keywords is not None:
            params["keywords"] = self.keywords

        return params


@dataclass
class SttWord:
    """Word-level timing information.

    Attributes:
        word: The transcribed word.
        start: Start time of the word in seconds.
        end: End time of the word in seconds.
        confidence: Confidence score for this word (0-1).
    """

    word: str
    start: float
    end: float
    confidence: Optional[float] = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SttWord":
        """Create an SttWord from a dictionary."""
        return cls(
            word=str(data.get("word", "")),
            start=float(data.get("start", 0)),
            end=float(data.get("end", 0)),
            confidence=float(data["confidence"]) if data.get("confidence") is not None else None,
        )


@dataclass
class SttEvent:
    """Event received from the STT WebSocket.

    Attributes:
        type: Event type ("transcript" or "error").
        transcript: The transcribed text (for "transcript" events).
        is_final: Whether this is a final transcription result.
        confidence: Confidence score (0-1) for the transcription.
        error: Error message (for "error" events).
        words: Word-level timing information if available.
        channel: Audio channel the transcript is from.
        start_time: Start time of the transcript in seconds.
        duration: Duration of the transcript in seconds.
    """

    type: str
    transcript: Optional[str] = None
    is_final: bool = False
    confidence: Optional[float] = None
    error: Optional[str] = None
    words: List[SttWord] = field(default_factory=lambda: [])
    channel: Optional[int] = None
    start_time: Optional[float] = None
    duration: Optional[float] = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SttEvent":
        """Create an SttEvent from a dictionary."""
        words_data: object = data.get("words")
        words_list: List[SttWord] = []
        if words_data is not None and isinstance(words_data, list):
            for word_item in cast(List[object], words_data):
                if isinstance(word_item, dict):
                    word_dict = cast(dict[str, Any], word_item)
                    words_list.append(SttWord.from_dict(word_dict))

        return cls(
            type=str(data.get("type", "unknown")),
            transcript=str(data["transcript"]) if data.get("transcript") is not None else None,
            is_final=bool(data.get("is_final", False)),
            confidence=float(data["confidence"]) if data.get("confidence") is not None else None,
            error=str(data["error"]) if data.get("error") is not None else None,
            words=words_list,
            channel=int(data["channel"]) if data.get("channel") is not None else None,
            start_time=float(data["start_time"]) if data.get("start_time") is not None else None,
            duration=float(data["duration"]) if data.get("duration") is not None else None,
        )


def _build_websocket_url(base_url: str, params: SpeechToTextStreamParams) -> str:
    """Build the WebSocket URL with query parameters."""
    parsed = urlparse(base_url)

    # Convert HTTP(S) to WS(S)
    if parsed.scheme == "https":
        ws_scheme = "wss"
    elif parsed.scheme == "http":
        ws_scheme = "ws"
    else:
        ws_scheme = parsed.scheme

    # Build the path
    path = parsed.path.rstrip("/") + "/speech-to-text/transcription"

    # Build query string
    query_params = params.to_query_params()
    query_string = urlencode(query_params) if query_params else ""

    # Construct URL
    host = parsed.netloc
    if query_string:
        return f"{ws_scheme}://{host}{path}?{query_string}"
    return f"{ws_scheme}://{host}{path}"


class SpeechToTextWS:
    """Synchronous WebSocket client for Speech-to-Text streaming.

    This class provides a synchronous interface for real-time speech
    transcription using Telnyx's STT API.

    Example:
        from telnyx.lib import SpeechToTextWS, SpeechToTextStreamParams

        params = SpeechToTextStreamParams(
            transcription_engine="Deepgram",
            language="en-US",
            input_format="wav",
        )

        with SpeechToTextWS(api_key="YOUR_API_KEY", params=params) as ws:
            ws.send(audio_bytes)
            for event in ws.events():
                if event.type == "transcript":
                    print(f"Transcript: {event.transcript} (final: {event.is_final})")
    """

    def __init__(
        self,
        api_key: str,
        params: SpeechToTextStreamParams,
        base_url: str = "https://api.telnyx.com/v2",
        event_buffer_size: int = 100,
    ) -> None:
        """Initialize the Speech-to-Text WebSocket client.

        Args:
            api_key: The Telnyx API key for authentication.
            params: Configuration parameters for the STT stream.
            base_url: The base API URL (defaults to "https://api.telnyx.com/v2").
            event_buffer_size: Size of the internal event queue (defaults to 100).
        """
        self._api_key = api_key
        self._params = params
        self._base_url = base_url
        self._event_buffer_size = event_buffer_size

        self._ws: Any = None  # websockets.sync.client.ClientConnection
        self._events_queue: Queue[Optional[SttEvent]] = Queue(maxsize=event_buffer_size)
        self._receiver_thread: Optional[threading.Thread] = None
        self._closed = False
        self._connected = False
        self._lock = threading.Lock()

    def connect(self) -> None:
        """Connect to the Speech-to-Text WebSocket server.

        Raises:
            SpeechToTextWSError: If connection fails or websockets is not installed.
        """
        try:
            from websockets.sync.client import connect as ws_connect
        except ImportError as e:
            raise SpeechToTextWSError(
                "websockets library is required. Install with: pip install 'telnyx[websockets]'",
                cause=e,
            ) from e

        if self._connected:
            return

        url = _build_websocket_url(self._base_url, self._params)
        headers = {"Authorization": f"Bearer {self._api_key}"}

        try:
            self._ws = ws_connect(url, additional_headers=headers)
            self._connected = True
            self._closed = False

            # Start receiver thread
            self._receiver_thread = threading.Thread(target=self._receive_messages, daemon=True)
            self._receiver_thread.start()
        except Exception as e:
            raise SpeechToTextWSError("Failed to connect to WebSocket", cause=e) from e

    def send(self, audio_data: bytes) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            audio_data: Binary audio data to transcribe.

        Raises:
            SpeechToTextWSError: If not connected or send fails.
        """
        if not self._connected or self._ws is None:
            raise SpeechToTextWSError("WebSocket is not connected")

        try:
            self._ws.send(audio_data)
        except Exception as e:
            raise SpeechToTextWSError("Failed to send audio data", cause=e) from e

    def events(self, timeout: Optional[float] = None) -> Iterator[SttEvent]:
        """Iterate over incoming STT events.

        Args:
            timeout: Timeout in seconds for waiting on events. None means wait forever.

        Yields:
            SttEvent objects as they are received.

        Example:
            for event in ws.events():
                if event.type == "transcript":
                    print(event.transcript)
        """
        while not self._closed:
            try:
                event = self._events_queue.get(timeout=timeout or 0.1)
                if event is None:
                    # Sentinel value indicating stream end
                    break
                yield event
            except Empty:
                if timeout is not None:
                    break
                # Continue waiting if no timeout specified
                continue

    def close(self) -> None:
        """Close the WebSocket connection gracefully."""
        with self._lock:
            if self._closed:
                return
            self._closed = True

        if self._ws is not None:
            try:
                self._ws.close()
            except Exception:
                pass

        # Wait for receiver thread to finish
        if self._receiver_thread is not None and self._receiver_thread.is_alive():
            self._receiver_thread.join(timeout=2.0)

        self._connected = False

    def _receive_messages(self) -> None:
        """Background thread that receives messages from the WebSocket."""
        try:
            while not self._closed and self._ws is not None:
                try:
                    message = self._ws.recv()
                    if isinstance(message, str):
                        data: dict[str, Any] = json.loads(message)
                        event = SttEvent.from_dict(data)
                        try:
                            self._events_queue.put(event, timeout=1.0)
                        except Exception:
                            # Queue full, drop event
                            pass
                except Exception:
                    if not self._closed:
                        break
        finally:
            # Signal end of events
            try:
                self._events_queue.put(None, timeout=1.0)
            except Exception:
                pass

    def __enter__(self) -> "SpeechToTextWS":
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Any,
    ) -> None:
        """Context manager exit."""
        self.close()

    @property
    def is_connected(self) -> bool:
        """Return whether the WebSocket is currently connected."""
        return self._connected and not self._closed


class AsyncSpeechToTextWS:
    """Asynchronous WebSocket client for Speech-to-Text streaming.

    This class provides an async interface for real-time speech
    transcription using Telnyx's STT API.

    Example:
        from telnyx.lib import AsyncSpeechToTextWS, SpeechToTextStreamParams
        import asyncio

        async def main():
            params = SpeechToTextStreamParams(
                transcription_engine="Deepgram",
                language="en-US",
                input_format="wav",
            )

            async with AsyncSpeechToTextWS(api_key="YOUR_API_KEY", params=params) as ws:
                await ws.send(audio_bytes)
                async for event in ws.events():
                    if event.type == "transcript":
                        print(f"Transcript: {event.transcript} (final: {event.is_final})")

        asyncio.run(main())
    """

    def __init__(
        self,
        api_key: str,
        params: SpeechToTextStreamParams,
        base_url: str = "https://api.telnyx.com/v2",
    ) -> None:
        """Initialize the async Speech-to-Text WebSocket client.

        Args:
            api_key: The Telnyx API key for authentication.
            params: Configuration parameters for the STT stream.
            base_url: The base API URL (defaults to "https://api.telnyx.com/v2").
        """
        self._api_key = api_key
        self._params = params
        self._base_url = base_url

        self._ws: Any = None  # websockets.asyncio.client.ClientConnection
        self._closed = False
        self._connected = False

    async def connect(self) -> None:
        """Connect to the Speech-to-Text WebSocket server.

        Raises:
            SpeechToTextWSError: If connection fails or websockets is not installed.
        """
        try:
            from websockets.asyncio.client import connect as ws_connect
        except ImportError as e:
            raise SpeechToTextWSError(
                "websockets library is required. Install with: pip install 'telnyx[websockets]'",
                cause=e,
            ) from e

        if self._connected:
            return

        url = _build_websocket_url(self._base_url, self._params)
        headers = {"Authorization": f"Bearer {self._api_key}"}

        try:
            self._ws = await ws_connect(url, additional_headers=headers)
            self._connected = True
            self._closed = False
        except Exception as e:
            raise SpeechToTextWSError("Failed to connect to WebSocket", cause=e) from e

    async def send(self, audio_data: bytes) -> None:
        """Send binary audio data to the server for transcription.

        Args:
            audio_data: Binary audio data to transcribe.

        Raises:
            SpeechToTextWSError: If not connected or send fails.
        """
        if not self._connected or self._ws is None:
            raise SpeechToTextWSError("WebSocket is not connected")

        try:
            await self._ws.send(audio_data)
        except Exception as e:
            raise SpeechToTextWSError("Failed to send audio data", cause=e) from e

    async def events(self) -> "AsyncIterator[SttEvent]":
        """Iterate over incoming STT events asynchronously.

        Yields:
            SttEvent objects as they are received.

        Example:
            async for event in ws.events():
                if event.type == "transcript":
                    print(event.transcript)
        """
        if self._ws is None:
            raise SpeechToTextWSError("WebSocket is not connected")

        try:
            async for message in self._ws:
                if self._closed:
                    break
                if isinstance(message, str):
                    data: dict[str, Any] = json.loads(message)
                    yield SttEvent.from_dict(data)
        except Exception:
            if not self._closed:
                raise

    async def close(self) -> None:
        """Close the WebSocket connection gracefully."""
        if self._closed:
            return

        self._closed = True

        if self._ws is not None:
            try:
                await self._ws.close()
            except Exception:
                pass

        self._connected = False

    async def __aenter__(self) -> "AsyncSpeechToTextWS":
        """Async context manager entry."""
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Any,
    ) -> None:
        """Async context manager exit."""
        await self.close()

    @property
    def is_connected(self) -> bool:
        """Return whether the WebSocket is currently connected."""
        return self._connected and not self._closed
