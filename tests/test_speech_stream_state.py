from __future__ import annotations

from typing import AsyncIterator, AsyncGenerator, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from telnyx.lib import SttEvent, SpeechToTextWS, AsyncSpeechToTextWS, SpeechToTextStreamParams


def test_sync_remote_close_reports_disconnected() -> None:
    socket = MagicMock()
    socket.recv.side_effect = ConnectionError("remote closed")
    with patch("websockets.sync.client.connect", return_value=socket):
        client = SpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            client.connect()
            assert client._receiver_thread is not None
            client._receiver_thread.join(timeout=2)
            assert not client._receiver_thread.is_alive()
            assert not client.is_connected
        finally:
            client.close()


def test_sync_explicit_close_reports_disconnected() -> None:
    with patch("websockets.sync.client.connect"), patch("telnyx.lib.speech_to_text_ws.threading.Thread"):
        client = SpeechToTextWS("local-test", SpeechToTextStreamParams())
        client.connect()
        assert client.is_connected
        client.close()
        assert not client.is_connected


@pytest.mark.asyncio
async def test_async_remote_close_reports_disconnected() -> None:
    socket = MagicMock()
    socket.__aiter__.return_value = []
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            await client.connect()
            assert [event async for event in client.events()] == []
            assert not client.is_connected
        finally:
            await client.close()


@pytest.mark.asyncio
async def test_async_receive_error_reports_disconnected() -> None:
    async def messages() -> AsyncIterator[str]:
        yield '{"type":"transcript","transcript":"example"}'
        raise ConnectionError("remote closed")

    socket = MagicMock()
    socket.__aiter__.side_effect = messages
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        received: list[str | None] = []
        try:
            await client.connect()
            with pytest.raises(ConnectionError, match="remote closed"):
                async for event in client.events():
                    received.append(event.transcript)
            assert received == ["example"]
            assert not client.is_connected
        finally:
            await client.close()


@pytest.mark.asyncio
async def test_async_consumer_exit_keeps_open_connection_state() -> None:
    socket = MagicMock()
    socket.__aiter__.return_value = ['{"type":"transcript","transcript":"example"}']
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            await client.connect()
            events = cast(AsyncGenerator[SttEvent, None], client.events())
            assert (await events.__anext__()).transcript == "example"
            await events.aclose()
            assert client.is_connected
            socket.close.assert_not_called()
        finally:
            await client.close()


@pytest.mark.asyncio
async def test_async_explicit_close_reports_disconnected() -> None:
    socket = MagicMock()
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        await client.connect()
        assert client.is_connected
        await client.close()
        assert not client.is_connected
