"""Run one non-streaming chat completion (a billable request)."""

from __future__ import annotations

import os
import sys
import json
import argparse

import httpx

from telnyx import Telnyx, APIStatusError, APIConnectionError


def main(argv: list[str] | None = None, *, http_client: httpx.Client | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Model ID available to your account")
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args(argv)
    api_key = os.environ.get("TELNYX_API_KEY")
    if not api_key:
        print("Set TELNYX_API_KEY before running this example.", file=sys.stderr)
        return 1
    # Ref: src/telnyx/resources/ai/openai/chat.py; response is a dictionary, not a typed stream.
    try:
        with Telnyx(api_key=api_key, http_client=http_client, timeout=30.0, max_retries=0) as client:
            response = client.ai.openai.chat.create_completion(
                model=args.model,
                messages=[{"role": "user", "content": args.prompt}],
                stream=False,
                max_tokens=128,
            )
    except APIStatusError as exc:
        print(f"Chat request failed (HTTP {exc.status_code}).", file=sys.stderr)
        return 1
    except APIConnectionError:
        print("Chat request failed (connection or timeout).", file=sys.stderr)
        return 1
    print(json.dumps(response))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
