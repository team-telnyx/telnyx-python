# Runnable Python examples

These are two minimal examples using the SDK in this checkout, not a complete
scenario catalog. Run commands from the repository root with Python 3.9+ and
[uv](https://docs.astral.sh/uv/):

```sh
uv sync --all-extras
uv run python -m examples.chat_completion --help
uv run python -m examples.verify_webhook --help
```

`uv sync` installs this checkout in editable mode. Webhook verification needs the
`webhooks` extra (PyNaCl); `--all-extras` includes it. For a standalone copy of the
scripts, install `telnyx[webhooks]` into a virtual environment first, then execute
`python chat_completion.py` or `python verify_webhook.py`.

## AI chat completion

Supply `TELNYX_API_KEY` through your secret manager or a private shell environment;
do not put it in source, command-line flags, committed `.env` files or logs.
Select a model ID currently available to your account (see the
[SDK API reference](../api.md)).

```sh
uv run python -m examples.chat_completion --model 'YOUR_MODEL_ID' --prompt 'Say hello briefly.'
```

**This command makes a real, potentially billable request.** It uses
`client.ai.openai.chat.create_completion`, explicitly sets `stream=False`, limits
output to 128 tokens, sets a 30-second timeout and disables automatic retries.
It prints the response dictionary as JSON. This is not a typed streaming example;
`with_streaming_response` is not a typed chat-event iterator.

Missing credentials, HTTP errors (including authentication/rate limits), connection
errors and timeouts produce exit status 1 without printing response bodies or
credentials. Usage errors exit 2. On success the response may contain sensitive
content: keep stdout private. Prompts passed on the command line may appear in
shell history/process listings; use only non-sensitive prompts with this demo.
Do not enable SDK debug logging when handling sensitive inputs.

## Local webhook signature verification

Set `TELNYX_PUBLIC_KEY` to the base64 Ed25519 **public** key from Telnyx Mission
Control, not your API key and never a signing/private key. Save the original raw
request body as `body.json`, and its HTTP headers as a JSON string-to-string map
in `headers.json`. The required header names are case-insensitive:

```json
{
  "telnyx-signature-ed25519": "BASE64_SIGNATURE_FROM_REQUEST",
  "telnyx-timestamp": "UNIX_SECONDS_FROM_REQUEST"
}
```

```sh
uv run python -m examples.verify_webhook body.json --headers headers.json
```

This command makes **no network requests**. It calls the existing public
`telnyx.lib.webhook_verification.verify_webhook_signature` helper on raw bytes
**before** parsing JSON. It prints only a confirmation, never the payload.
Do not pretty-print, reserialize, trim whitespace, normalize newlines, or decode
and re-encode the body before verification. Framework receivers should pass the
original request bytes and headers to that same helper before processing events.

The SDK checks Ed25519 signatures and enforces its five-minute timestamp window.
Old saved deliveries will fail; do not weaken the tolerance to replay them. A
valid signature does not prevent repeated deliveries within the window: production
handlers must also deduplicate event IDs, enforce request size limits, handle
business failures, and return appropriate HTTP responses. This file-based example
is not a web server or a production webhook handler. Keep request captures private
and out of git. Invalid signatures, missing keys, malformed inputs and file errors
exit 1; nothing is processed.

## Offline regression tests

```sh
uv run --all-extras pytest examples/test_examples.py -n 0
# Repository-supported Python/Pydantic matrix:
./scripts/test examples/test_examples.py -n 0
```

Tests exercise the actual editable candidate SDK with `httpx.MockTransport`, not
mock SDK methods. Socket connections are blocked. Webhook tests generate ephemeral
Ed25519 keys, sign actual timestamp/body bytes and cover tampering, timestamp
rejection, invalid inputs and safe failures. No real API key or billed operation
is needed. Staging CI explicitly runs this test file because the default pytest
configuration discovers only `tests/`. Examples and their tests live together in
the repository-owned, generation-preserved `examples/` directory.
