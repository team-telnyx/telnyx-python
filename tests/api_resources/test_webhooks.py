# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os

import pytest

from telnyx import Telnyx, AsyncTelnyx

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: Telnyx) -> None:
        import time
        import base64

        from nacl.signing import SigningKey

        data = """{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"conference.floor.changed","payload":{"call_control_id":"v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","conference_id":"428c31b6-abf3-3bc1-b7f4-5013ef9657c1","connection_id":"7267xxxxxxxxxxxxxx","occurred_at":"2018-02-02T22:25:27.521Z"},"record_type":"event"}"""
        data = " " + data + " "
        signing_key = SigningKey.generate()
        public_key = base64.b64encode(bytes(signing_key.verify_key)).decode("ascii")

        def signed_headers(
            payload: str = data,
            timestamp: str | None = None,
            mixed_case: bool = False,
        ) -> dict[str, str]:
            timestamp = timestamp or str(int(time.time()))
            message = f"{timestamp}|{payload}".encode("utf-8")
            signature = base64.b64encode(signing_key.sign(message).signature).decode("ascii")
            if mixed_case:
                return {
                    "tElNyX-sIgNaTuRe-Ed25519": signature,
                    "TeLnYx-TiMeStAmP": timestamp,
                }
            return {
                "telnyx-signature-ed25519": signature,
                "telnyx-timestamp": timestamp,
            }

        configured = client.with_options(public_key=public_key)
        _ = configured.webhooks.unwrap(data, headers=signed_headers(mixed_case=True))

        # A method key takes precedence and accepts either raw bytes or base64.
        configured = client.with_options(public_key="not-the-right-key")
        _ = configured.webhooks.unwrap(
            data,
            headers=signed_headers(),
            key=bytes(signing_key.verify_key),
        )
        _ = configured.webhooks.unwrap(data, headers=signed_headers(), key=public_key)

        with pytest.raises(ValueError, match="Cannot verify a webhook without a key"):
            _ = client.with_options(public_key=None).webhooks.unwrap(data, headers=signed_headers())

        for missing_header in ("telnyx-signature-ed25519", "telnyx-timestamp"):
            headers = signed_headers()
            del headers[missing_header]
            with pytest.raises(ValueError, match="Missing required header"):
                _ = client.webhooks.unwrap(data, headers=headers, key=public_key)

        for bad_timestamp in ("not-an-integer", "0", "9999999999"):
            with pytest.raises(ValueError):
                _ = client.webhooks.unwrap(
                    data,
                    headers=signed_headers(timestamp=bad_timestamp),
                    key=public_key,
                )

        for bad_key in ("%%%", b"short"):
            with pytest.raises(ValueError):
                _ = client.webhooks.unwrap(data, headers=signed_headers(), key=bad_key)

        for bad_signature in ("%%%", base64.b64encode(b"short").decode("ascii")):
            headers = signed_headers()
            headers["telnyx-signature-ed25519"] = bad_signature
            with pytest.raises(ValueError):
                _ = client.webhooks.unwrap(data, headers=headers, key=public_key)

        with pytest.raises(ValueError, match="Signature verification failed"):
            _ = client.webhooks.unwrap(
                data,
                headers=signed_headers(),
                key=base64.b64encode(bytes(SigningKey.generate().verify_key)).decode("ascii"),
            )

        with pytest.raises(ValueError, match="Signature verification failed"):
            _ = client.webhooks.unwrap(data + " ", headers=signed_headers(), key=public_key)

        _ = client.webhooks.unsafe_unwrap(data)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_unwrap(self, async_client: AsyncTelnyx) -> None:
        import time
        import base64

        from nacl.signing import SigningKey

        data = """{"id":"0ccc7b54-4df3-4bca-a65a-3da1ecc777f0","event_type":"conference.floor.changed","payload":{"call_control_id":"v3:MdI91X4lWFEs7IgbBEOT9M4AigoY08M0WWZFISt1Yw2axZ_IiE4pqg","call_leg_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","call_session_id":"428c31b6-7af4-4bcb-b7f5-5013ef9657c1","client_state":"aGF2ZSBhIG5pY2UgZGF5ID1d","conference_id":"428c31b6-abf3-3bc1-b7f4-5013ef9657c1","connection_id":"7267xxxxxxxxxxxxxx","occurred_at":"2018-02-02T22:25:27.521Z"},"record_type":"event"}"""
        data = " " + data + " "
        signing_key = SigningKey.generate()
        public_key = base64.b64encode(bytes(signing_key.verify_key)).decode("ascii")

        def signed_headers(
            payload: str = data,
            timestamp: str | None = None,
            mixed_case: bool = False,
        ) -> dict[str, str]:
            timestamp = timestamp or str(int(time.time()))
            message = f"{timestamp}|{payload}".encode("utf-8")
            signature = base64.b64encode(signing_key.sign(message).signature).decode("ascii")
            if mixed_case:
                return {
                    "tElNyX-sIgNaTuRe-Ed25519": signature,
                    "TeLnYx-TiMeStAmP": timestamp,
                }
            return {
                "telnyx-signature-ed25519": signature,
                "telnyx-timestamp": timestamp,
            }

        configured = async_client.with_options(public_key=public_key)
        _ = configured.webhooks.unwrap(data, headers=signed_headers(mixed_case=True))

        # A method key takes precedence and accepts either raw bytes or base64.
        configured = async_client.with_options(public_key="not-the-right-key")
        _ = configured.webhooks.unwrap(
            data,
            headers=signed_headers(),
            key=bytes(signing_key.verify_key),
        )
        _ = configured.webhooks.unwrap(data, headers=signed_headers(), key=public_key)

        with pytest.raises(ValueError, match="Cannot verify a webhook without a key"):
            _ = async_client.with_options(public_key=None).webhooks.unwrap(data, headers=signed_headers())

        for missing_header in ("telnyx-signature-ed25519", "telnyx-timestamp"):
            headers = signed_headers()
            del headers[missing_header]
            with pytest.raises(ValueError, match="Missing required header"):
                _ = async_client.webhooks.unwrap(data, headers=headers, key=public_key)

        for bad_timestamp in ("not-an-integer", "0", "9999999999"):
            with pytest.raises(ValueError):
                _ = async_client.webhooks.unwrap(
                    data,
                    headers=signed_headers(timestamp=bad_timestamp),
                    key=public_key,
                )

        for bad_key in ("%%%", b"short"):
            with pytest.raises(ValueError):
                _ = async_client.webhooks.unwrap(data, headers=signed_headers(), key=bad_key)

        for bad_signature in ("%%%", base64.b64encode(b"short").decode("ascii")):
            headers = signed_headers()
            headers["telnyx-signature-ed25519"] = bad_signature
            with pytest.raises(ValueError):
                _ = async_client.webhooks.unwrap(data, headers=headers, key=public_key)

        with pytest.raises(ValueError, match="Signature verification failed"):
            _ = async_client.webhooks.unwrap(
                data,
                headers=signed_headers(),
                key=base64.b64encode(bytes(SigningKey.generate().verify_key)).decode("ascii"),
            )

        with pytest.raises(ValueError, match="Signature verification failed"):
            _ = async_client.webhooks.unwrap(data + " ", headers=signed_headers(), key=public_key)

        _ = async_client.webhooks.unsafe_unwrap(data)
