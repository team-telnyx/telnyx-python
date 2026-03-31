"""
Custom utilities for the Telnyx SDK.

This package provides additional functionality that extends the core SDK,
including WebSocket support for real-time streaming APIs and ED25519
webhook signature verification.
"""

from telnyx.lib.webhooks_ed25519 import (
    verify_ed25519,
    unwrap_with_ed25519,
)
from telnyx.lib.speech_to_text_ws import (
    SttWord,
    SttEvent,
    SpeechToTextWS,
    AsyncSpeechToTextWS,
    SpeechToTextWSError,
    SpeechToTextStreamParams,
)
from telnyx.lib.webhook_verification import (
    SIGNATURE_HEADER,
    TIMESTAMP_HEADER,
    TIMESTAMP_TOLERANCE_SECONDS,
    WebhookVerificationError,
    verify_webhook_signature,
)

__all__ = [
    # Speech-to-Text WebSocket
    "SpeechToTextStreamParams",
    "SttEvent",
    "SttWord",
    "SpeechToTextWS",
    "AsyncSpeechToTextWS",
    "SpeechToTextWSError",
    # Webhook verification (ED25519)
    "WebhookVerificationError",
    "verify_webhook_signature",
    "verify_ed25519",
    "unwrap_with_ed25519",
    "SIGNATURE_HEADER",
    "TIMESTAMP_HEADER",
    "TIMESTAMP_TOLERANCE_SECONDS",
]
