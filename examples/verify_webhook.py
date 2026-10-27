"""Verify a saved raw Telnyx webhook locally, without an API request."""

from __future__ import annotations

import os
import sys
import json
import argparse
from typing import Dict, cast
from pathlib import Path

from telnyx.lib.webhook_verification import WebhookVerificationError, verify_webhook_signature


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("body", type=Path, help="File containing unchanged raw HTTP request bytes")
    parser.add_argument("--headers", required=True, type=Path, help="JSON object containing the original HTTP headers")
    args = parser.parse_args(argv)
    public_key = os.environ.get("TELNYX_PUBLIC_KEY")
    if not public_key:
        print("Set TELNYX_PUBLIC_KEY to your base64 Ed25519 public key.", file=sys.stderr)
        return 1
    try:
        body = Path(args.body).read_bytes()
        headers = json.loads(Path(args.headers).read_text(encoding="utf-8"))
        if not isinstance(headers, dict):
            raise ValueError("Expected a header object")
        # JSON object keys are strings; validate every value before passing to the SDK.
        header_values = cast(Dict[str, object], headers)
        if not all(isinstance(value, str) for value in header_values.values()):
            raise ValueError("Expected string header values")
        # Ref: src/telnyx/lib/webhook_verification.py. Verify BEFORE parsing the body.
        verify_webhook_signature(body, cast(Dict[str, str], header_values), public_key)
        json.loads(body)
    except WebhookVerificationError:
        print("Webhook signature verification failed; do not process this event.", file=sys.stderr)
        return 1
    except (OSError, ValueError):
        print("Cannot read webhook input or parse its UTF-8 JSON; event not processed.", file=sys.stderr)
        return 1
    print("Webhook signature verified; JSON parsed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
