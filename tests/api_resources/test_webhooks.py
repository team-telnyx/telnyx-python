# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import time

import pytest

try:
    from nacl.signing import SigningKey
    from nacl.encoding import Base64Encoder
except ImportError:
    pytest.skip("pynacl is required for webhook tests", allow_module_level=True)

from telnyx import Telnyx
from telnyx.resources.webhooks import TelnyxWebhookVerificationError

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: Telnyx) -> None:
        # Generate a test key pair for Telnyx ED25519 verification
        signing_key = SigningKey.generate()
        verify_key_b64 = signing_key.verify_key.encode(encoder=Base64Encoder).decode('utf-8')

        data = """{"data":{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"call.ai_gather.ended","occurred_at":"2018-02-02T22:25:27.521992Z","payload":{"call_control_id":"v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","connection_id":"7267xxxxxxxxxxxxxx","from":"+35319605860","message_history":[{"content":"Hello, can you tell me your age and where you live?","role":"assistant"},{"content":"Hello, I'm 29 and I live in Paris?","role":"user"}],"result":{"age":"bar","city":"bar"},"status":"valid","to":"+35319605860"},"record_type":"event"}}"""
        
        # Create timestamp and Telnyx-style signature (using base64)
        timestamp = str(int(time.time()))
        signed_payload = f"{timestamp}|{data}".encode('utf-8')
        signature = signing_key.sign(signed_payload, encoder=Base64Encoder).signature.decode('utf-8')
        
        headers = {
            "Telnyx-Signature-Ed25519": signature,
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }

        try:
            result = client.webhooks.unwrap(data, headers=headers, key=verify_key_b64)
            # Verify the result is properly parsed
            assert result.data.event_type == "call.ai_gather.ended"  # type: ignore[reportUnknownMemberType]
            assert result.data.payload.call_control_id == "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ"  # type: ignore[reportUnknownMemberType]
        except TelnyxWebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        # Test invalid signature
        bad_headers = [
            {**headers, "Telnyx-Signature-Ed25519": "invalid_signature"},
            {**headers, "Telnyx-Timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(TelnyxWebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=verify_key_b64)

        # Test missing headers
        incomplete_headers = {
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }
        with pytest.raises(TelnyxWebhookVerificationError):
            _ = client.webhooks.unwrap(data, headers=incomplete_headers, key=verify_key_b64)

        # Test case-insensitive headers
        lowercase_headers = {
            "telnyx-signature-ed25519": signature,
            "telnyx-timestamp": timestamp,
            "user-agent": "telnyx-webhooks"
        }
        try:
            result = client.webhooks.unwrap(data, headers=lowercase_headers, key=verify_key_b64)
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
        verify_key_b64 = signing_key.verify_key.encode(encoder=Base64Encoder).decode('utf-8')

        data = """{"data":{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"call.ai_gather.ended","occurred_at":"2018-02-02T22:25:27.521992Z","payload":{"call_control_id":"v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","connection_id":"7267xxxxxxxxxxxxxx","from":"+35319605860","message_history":[{"content":"Hello, can you tell me your age and where you live?","role":"assistant"},{"content":"Hello, I'm 29 and I live in Paris?","role":"user"}],"result":{"age":"bar","city":"bar"},"status":"valid","to":"+35319605860"},"record_type":"event"}}"""
        
        # Create timestamp and Telnyx-style signature (using base64)
        timestamp = str(int(time.time()))
        signed_payload = f"{timestamp}|{data}".encode('utf-8')
        signature = signing_key.sign(signed_payload, encoder=Base64Encoder).signature.decode('utf-8')
        
        headers = {
            "Telnyx-Signature-Ed25519": signature,
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }

        try:
            result = client.webhooks.unwrap(data, headers=headers, key=verify_key_b64)
            # Verify the result is properly parsed
            assert result.data.event_type == "call.ai_gather.ended"  # type: ignore[reportUnknownMemberType]
            assert result.data.payload.call_control_id == "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ"  # type: ignore[reportUnknownMemberType]
        except TelnyxWebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        # Test invalid signature
        bad_headers = [
            {**headers, "Telnyx-Signature-Ed25519": "invalid_signature"},
            {**headers, "Telnyx-Timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(TelnyxWebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=verify_key_b64)

        # Test missing headers
        incomplete_headers = {
            "Telnyx-Timestamp": timestamp,
            "User-Agent": "telnyx-webhooks"
        }
        with pytest.raises(TelnyxWebhookVerificationError):
            _ = client.webhooks.unwrap(data, headers=incomplete_headers, key=verify_key_b64)
