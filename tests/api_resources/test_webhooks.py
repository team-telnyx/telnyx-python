# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import time

import pytest

try:
    from nacl.signing import SigningKey
    from nacl.encoding import HexEncoder
except ImportError:
    pytest.skip("pynacl is required for webhook tests", allow_module_level=True)

from telnyx import Telnyx
from telnyx.resources.webhooks import TelnyxWebhook, TelnyxWebhookVerificationError

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: Telnyx) -> None:
        # Generate a test key pair for Telnyx ED25519 verification
        signing_key = SigningKey.generate()
        verify_key_hex = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')

        data = """{"data":{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"call.ai_gather.ended","occurred_at":"2018-02-02T22:25:27.521992Z","payload":{"call_control_id":"v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","connection_id":"7267xxxxxxxxxxxxxx","from":"+35319605860","message_history":[{"content":"Hello, can you tell me your age and where you live?","role":"assistant"},{"content":"Hello, I'm 29 and I live in Paris?","role":"user"}],"result":{"age":29,"city":"Paris"},"status":"valid","to":"+35319605860"},"record_type":"event"}}"""
        
        # Create timestamp and Telnyx-style signature
        timestamp = str(int(time.time()))
        signed_payload = timestamp.encode('utf-8') + data.encode('utf-8')
        signature = signing_key.sign(signed_payload, encoder=HexEncoder).signature.decode('utf-8')
        
        headers = {
            "Telnyx-Signature-Ed25519": signature,
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }

        try:
            result = client.webhooks.unwrap(data, headers=headers, key=verify_key_hex)
            # Verify the result is properly parsed
            assert result.data.event_type == "call.ai_gather.ended"  # type: ignore[reportUnknownMemberType]
            assert result.data.payload.call_control_id == "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ"  # type: ignore[reportUnknownMemberType]
        except TelnyxWebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        # Test invalid signature
        bad_headers = [
            {**headers, "Telnyx-Signature-Ed25519": "invalid_signature"},
            {**headers, "Telnyx-Timestamp": "0"},
            {**headers, "User-Agent": "malicious-bot"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(TelnyxWebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=verify_key_hex)

        # Test missing headers
        incomplete_headers = {
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }
        with pytest.raises(TelnyxWebhookVerificationError):
            _ = client.webhooks.unwrap(data, headers=incomplete_headers, key=verify_key_hex)

        # Test case-insensitive headers
        lowercase_headers = {
            "telnyx-signature-ed25519": signature,
            "telnyx-timestamp": timestamp,
            "user-agent": "telnyx-webhooks"
        }
        try:
            result = client.webhooks.unwrap(data, headers=lowercase_headers, key=verify_key_hex)
            assert result.data.event_type == "call.ai_gather.ended"  # type: ignore[reportUnknownMemberType]
        except TelnyxWebhookVerificationError as e:
            raise AssertionError("Failed to unwrap webhook with lowercase headers") from e


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_unwrap(self, client: Telnyx) -> None:
        # Generate a test key pair for Telnyx ED25519 verification
        signing_key = SigningKey.generate()
        verify_key_hex = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')

        data = """{"data":{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"call.ai_gather.ended","occurred_at":"2018-02-02T22:25:27.521992Z","payload":{"call_control_id":"v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","connection_id":"7267xxxxxxxxxxxxxx","from":"+35319605860","message_history":[{"content":"Hello, can you tell me your age and where you live?","role":"assistant"},{"content":"Hello, I'm 29 and I live in Paris?","role":"user"}],"result":{"age":29,"city":"Paris"},"status":"valid","to":"+35319605860"},"record_type":"event"}}"""
        
        # Create timestamp and Telnyx-style signature
        timestamp = str(int(time.time()))
        signed_payload = timestamp.encode('utf-8') + data.encode('utf-8')
        signature = signing_key.sign(signed_payload, encoder=HexEncoder).signature.decode('utf-8')
        
        headers = {
            "Telnyx-Signature-Ed25519": signature,
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }

        try:
            result = client.webhooks.unwrap(data, headers=headers, key=verify_key_hex)
            # Verify the result is properly parsed
            assert result.data.event_type == "call.ai_gather.ended"  # type: ignore[reportUnknownMemberType]
            assert result.data.payload.call_control_id == "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ"  # type: ignore[reportUnknownMemberType]
        except TelnyxWebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        # Test invalid signature
        bad_headers = [
            {**headers, "Telnyx-Signature-Ed25519": "invalid_signature"},
            {**headers, "Telnyx-Timestamp": "0"},
            {**headers, "User-Agent": "malicious-bot"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(TelnyxWebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=verify_key_hex)

        # Test missing headers
        incomplete_headers = {
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }
        with pytest.raises(TelnyxWebhookVerificationError):
            _ = client.webhooks.unwrap(data, headers=incomplete_headers, key=verify_key_hex)
class TestTelnyxWebhook:
    """Test the TelnyxWebhook class directly to ensure it follows standardwebhooks pattern."""

    def test_webhook_initialization(self) -> None:
        """Test that TelnyxWebhook can be initialized like standardwebhooks.Webhook."""
        signing_key = SigningKey.generate()
        verify_key_hex = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')
        
        # Should initialize like standardwebhooks.Webhook
        webhook = TelnyxWebhook(verify_key_hex)
        assert webhook is not None
        assert hasattr(webhook, 'verify')

    def test_webhook_verification_pattern(self) -> None:
        """Test that TelnyxWebhook.verify follows the same pattern as standardwebhooks.Webhook.verify."""
        signing_key = SigningKey.generate()
        verify_key_hex = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')
        
        data = """{"test": "payload"}"""
        timestamp = str(int(time.time()))
        signed_payload = timestamp.encode('utf-8') + data.encode('utf-8')
        signature = signing_key.sign(signed_payload, encoder=HexEncoder).signature.decode('utf-8')
        
        headers = {
            "Telnyx-Signature-Ed25519": signature,
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }
        
        # Should verify like standardwebhooks.Webhook.verify
        webhook = TelnyxWebhook(verify_key_hex)
        
        # Valid webhook should not raise exception
        webhook.verify(data, headers)
        
        # Invalid webhook should raise TelnyxWebhookVerificationError
        with pytest.raises(TelnyxWebhookVerificationError):
            webhook.verify(data, {**headers, "Telnyx-Signature-Ed25519": "invalid"})

    def test_exception_hierarchy(self) -> None:
        """Test that TelnyxWebhookVerificationError follows the right pattern."""
        # Should be importable like standardwebhooks.WebhookVerificationError
        assert TelnyxWebhookVerificationError is not None
        
        # Should be able to raise and catch it
        with pytest.raises(TelnyxWebhookVerificationError):
            raise TelnyxWebhookVerificationError("Test error")

    def test_key_format_handling(self) -> None:
        """Test that TelnyxWebhook handles different key formats like standardwebhooks."""
        signing_key = SigningKey.generate()
        verify_key_hex = signing_key.verify_key.encode(encoder=HexEncoder).decode('utf-8')
        verify_key_bytes = signing_key.verify_key.encode()
        
        # Should accept hex string (Telnyx format)
        webhook1 = TelnyxWebhook(verify_key_hex)
        assert webhook1 is not None
        
        # Should accept bytes (standardwebhooks format)
        webhook2 = TelnyxWebhook(verify_key_bytes)
        assert webhook2 is not None
        
        # Should reject invalid key format
        with pytest.raises(TelnyxWebhookVerificationError):
            TelnyxWebhook("invalid_key_format")