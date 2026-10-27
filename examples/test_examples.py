from __future__ import annotations

import os
import json
import time
import base64
import socket
from pathlib import Path

import httpx
import pytest
from nacl.signing import SigningKey


@pytest.fixture(autouse=True)
def no_network(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in tuple(os.environ):
        if name.startswith("TELNYX_"):
            monkeypatch.delenv(name)

    def deny(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("Examples tests must not access the network")

    monkeypatch.setattr(socket.socket, "connect", deny)


def test_chat_success(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    from examples.chat_completion import main

    monkeypatch.setenv("TELNYX_API_KEY", "test-only-key")

    def respond(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://api.telnyx.com/v2/ai/openai/chat/completions"
        assert request.method == "POST"
        assert request.headers["authorization"] == "Bearer test-only-key"
        assert json.loads(request.content) == {
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hello"}],
            "stream": False,
            "max_tokens": 128,
        }
        return httpx.Response(200, json={"choices": [{"message": {"content": "Hi"}}]})

    with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
        assert main(["--model", "test-model", "--prompt", "Hello"], http_client=transport) == 0
    assert json.loads(capsys.readouterr().out) == {"choices": [{"message": {"content": "Hi"}}]}


@pytest.mark.parametrize("failure", ["unauthorized", "rate_limit", "timeout", "connection"])
def test_chat_errors_are_safe(
    failure: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from examples.chat_completion import main

    monkeypatch.setenv("TELNYX_API_KEY", "test-only-key")

    def respond(request: httpx.Request) -> httpx.Response:
        if failure == "timeout":
            raise httpx.ReadTimeout("private detail", request=request)
        if failure == "connection":
            raise httpx.ConnectError("private detail", request=request)
        return httpx.Response(401 if failure == "unauthorized" else 429, json={"error": "private detail"})

    with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
        assert main(["--model", "test-model", "--prompt", "private prompt"], http_client=transport) == 1
    output = capsys.readouterr()
    assert output.out == ""
    assert "Chat request failed" in output.err
    assert "private" not in output.err
    assert "test-only-key" not in output.err


def test_chat_requires_key(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    from examples.chat_completion import main

    monkeypatch.delenv("TELNYX_API_KEY", raising=False)
    assert main(["--model", "test-model", "--prompt", "Hello"]) == 1
    assert "Set TELNYX_API_KEY" in capsys.readouterr().err


def signed_files(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, body: bytes, age: int = 0) -> list[str]:
    key = SigningKey.generate()
    timestamp = str(int(time.time()) - age)
    signature = key.sign(timestamp.encode() + b"|" + body).signature
    monkeypatch.setenv("TELNYX_PUBLIC_KEY", base64.b64encode(bytes(key.verify_key)).decode())
    (tmp_path / "body.json").write_bytes(body)
    (tmp_path / "headers.json").write_text(
        json.dumps(
            {
                "Telnyx-Timestamp": timestamp,
                "Telnyx-Signature-Ed25519": base64.b64encode(signature).decode(),
            }
        )
    )
    return [str(tmp_path / "body.json"), "--headers", str(tmp_path / "headers.json")]


def test_webhook_success(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    from examples.verify_webhook import main

    args = signed_files(tmp_path, monkeypatch, '{ "data": {"id": "event-test", "text": "héllo"}}\n'.encode())
    assert main(args) == 0
    assert capsys.readouterr().out == "Webhook signature verified; JSON parsed.\n"


@pytest.mark.parametrize(
    "failure",
    [
        "tampered",
        "stale",
        "future",
        "missing_signature",
        "missing_key",
        "bad_key",
        "bad_json",
        "bad_headers",
        "non_string_header",
        "missing_file",
        "invalid_utf8",
    ],
)
def test_webhook_rejects_invalid_input(
    failure: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from examples.verify_webhook import main

    body = b"private-invalid-json" if failure == "bad_json" else b'{"private": "payload"}'
    if failure == "invalid_utf8":
        body = b"\xff"
    age = 600 if failure == "stale" else -600 if failure == "future" else 0
    args = signed_files(tmp_path, monkeypatch, body, age)
    if failure == "tampered":
        (tmp_path / "body.json").write_bytes(b"not even JSON")
    elif failure == "missing_signature":
        (tmp_path / "headers.json").write_text("{}")
    elif failure == "missing_key":
        monkeypatch.delenv("TELNYX_PUBLIC_KEY")
    elif failure == "bad_key":
        monkeypatch.setenv("TELNYX_PUBLIC_KEY", "invalid")
    elif failure == "bad_headers":
        (tmp_path / "headers.json").write_text("[]")
    elif failure == "non_string_header":
        (tmp_path / "headers.json").write_text('{"telnyx-timestamp": 123}')
    elif failure == "missing_file":
        args[0] = str(tmp_path / "nonexistent.json")
    assert main(args) == 1
    output = capsys.readouterr()
    assert output.out == ""
    assert output.err
    assert "private" not in output.err
    if failure == "tampered":
        assert "signature verification failed" in output.err
