from __future__ import annotations

import asyncio
from typing import AsyncIterator, AsyncGenerator, cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from telnyx.lib import SttEvent, SpeechToTextWS, AsyncSpeechToTextWS, SpeechToTextWSError, SpeechToTextStreamParams


def test_sync_remote_close_reports_disconnected() -> None:
    socket = MagicMock()
    socket.recv.side_effect = ['{"type":"transcript","transcript":"example"}', ConnectionError("remote closed")]
    with patch("websockets.sync.client.connect", return_value=socket):
        client = SpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            client.connect()
            assert client._receiver_thread is not None
            client._receiver_thread.join(timeout=2)
            assert not client._receiver_thread.is_alive()
            assert [event.transcript for event in client.events(timeout=0.1)] == ["example"]
            assert not client.is_connected
            with pytest.raises(SpeechToTextWSError, match="WebSocket is not connected"):
                client.send(b"audio")
            socket.send.assert_not_called()
        finally:
            client.close()
        socket.close.assert_called_once()


@pytest.mark.asyncio
async def test_async_remote_close_reports_disconnected() -> None:
    socket = MagicMock()
    socket.__aiter__.return_value = ['{"type":"transcript","transcript":"example"}']
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            await client.connect()
            assert [event.transcript async for event in client.events()] == ["example"]
            assert not client.is_connected
            with pytest.raises(SpeechToTextWSError, match="WebSocket is not connected"):
                await client.send(b"audio")
            socket.send.assert_not_called()
        finally:
            await client.close()
        socket.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_async_receive_error_reports_disconnected() -> None:
    error = ConnectionError("remote closed")

    async def messages() -> AsyncIterator[str]:
        yield '{"type":"transcript","transcript":"example"}'
        raise error

    socket = MagicMock()
    socket.__aiter__.side_effect = messages
    socket.close = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        client = AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams())
        try:
            await client.connect()
            received: list[str | None] = []
            with pytest.raises(ConnectionError) as caught:
                async for event in client.events():
                    received.append(event.transcript)
            assert caught.value is error
            assert received == ["example"]
            assert not client.is_connected
            with pytest.raises(SpeechToTextWSError, match="WebSocket is not connected"):
                await client.send(b"audio")
            socket.send.assert_not_called()
        finally:
            await client.close()


@pytest.mark.asyncio
async def test_async_consumer_exit_preserves_live_connection() -> None:
    socket = MagicMock()
    socket.__aiter__.return_value = ['{"type":"transcript","transcript":"example"}']
    socket.close = AsyncMock()
    socket.send = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        async with AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams()) as client:
            events = cast(AsyncGenerator[SttEvent, None], client.events())
            assert (await events.__anext__()).transcript == "example"
            await events.aclose()
            assert client.is_connected
            await client.send(b"audio")
            socket.send.assert_awaited_once_with(b"audio")
            socket.close.assert_not_called()
        assert not client.is_connected
        await client.close()
        socket.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_async_cancelled_receive_preserves_live_connection() -> None:
    receiving = asyncio.Event()

    async def messages() -> AsyncIterator[str]:
        receiving.set()
        await asyncio.Event().wait()
        yield "unreachable"

    socket = MagicMock()
    socket.__aiter__.side_effect = messages
    socket.close = AsyncMock()
    socket.send = AsyncMock()
    with patch("websockets.asyncio.client.connect", new_callable=AsyncMock, return_value=socket):
        async with AsyncSpeechToTextWS("local-test", SpeechToTextStreamParams()) as client:
            events = cast(AsyncGenerator[SttEvent, None], client.events())
            task = asyncio.create_task(events.__anext__())
            await asyncio.wait_for(receiving.wait(), timeout=2)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task
            assert client.is_connected
            await client.send(b"audio")
            socket.send.assert_awaited_once_with(b"audio")
            socket.close.assert_not_called()
        assert not client.is_connected
        socket.close.assert_awaited_once()


def test_sync_context_close_joins_receiver_and_is_idempotent() -> None:
    import threading

    receiving = threading.Event()
    closed = threading.Event()

    def recv() -> str:
        receiving.set()
        assert closed.wait(timeout=2)
        raise ConnectionError("closed")

    socket = MagicMock()
    socket.recv.side_effect = recv
    socket.close.side_effect = closed.set
    with patch("websockets.sync.client.connect", return_value=socket):
        with SpeechToTextWS("local-test", SpeechToTextStreamParams()) as client:
            assert receiving.wait(timeout=2)
            assert client.is_connected
            client.send(b"audio")
            socket.send.assert_called_once_with(b"audio")
        assert not client.is_connected
        assert client._receiver_thread is not None
        assert not client._receiver_thread.is_alive()
        client.close()
        socket.close.assert_called_once()
