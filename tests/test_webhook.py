from __future__ import absolute_import, division, print_function

import base64
import time

from nacl.encoding import Base64Encoder
from nacl.signing import SigningKey

import pytest

import telnyx

DUMMY_WEBHOOK_PAYLOAD = b"""{
    "record_type": "event",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "event_type": "call_initiated",
    "created_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
        "to": "+13129457420",
        "start_time": "2018-02-02T22:25:27.521992Z",
        "occurred_at": "2018-02-02T22:25:27.521992Z",
        "from": "+35319605860",
        "call_control_id": "AgDIxmoRX6QMuaIj_uXRXnPAXP0QlNfXczRrZvZakpWxBlpw48KyZQ==",
        "connection_id": "7267xxxxxxxxxxxxxx",
        "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
        "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
        "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
        "direction": "incoming",
        "state": "parked"
    }
}"""


@pytest.fixture
def signing_key():
    return SigningKey.generate()


@pytest.fixture
def signing_key_base64(signing_key):
    return signing_key.encode(encoder=Base64Encoder)


@pytest.fixture
def verify_key_base64(signing_key):
    return signing_key.verify_key.encode(encoder=Base64Encoder)


@pytest.fixture
def signer(signing_key):
    def _signer(payload, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time())).encode("UTF-8")

        if hasattr(payload, "encode"):
            payload = payload.encode("utf-8")

        if hasattr(timestamp, "encode"):
            timestamp = timestamp.encode("utf-8")

        signed_payload = timestamp + b"|" + payload
        signed_message = signing_key.sign(signed_payload)
        signature = signed_message.signature

        return base64.b64encode(signature)

    return _signer


def test_construct_event(verify_key_base64, signer):
    telnyx.public_key = verify_key_base64

    timestamp = str(int(time.time())).encode("UTF-8")
    signature = signer(DUMMY_WEBHOOK_PAYLOAD, timestamp=timestamp)

    event = telnyx.Webhook.construct_event(DUMMY_WEBHOOK_PAYLOAD, signature, timestamp)
    assert isinstance(event, telnyx.Event)


def test_raise_on_json_error(verify_key_base64, signer):
    payload = b"this is not valid JSON"
    telnyx.public_key = verify_key_base64

    timestamp = str(int(time.time())).encode("UTF-8")
    signature = signer(payload, timestamp=timestamp)
    with pytest.raises(ValueError):
        telnyx.Webhook.construct_event(payload, signature, timestamp)


# def test_raise_on_invalid_header(verify_key_base64, signer):
#     telnyx.public_key = verify_key_base64
#     signature = "FAKEFAKEFAKE"
#     timestamp = str(int(time.time()))
#     with pytest.raises(telnyx.error.SignatureVerificationError):
#         telnyx.Webhook.construct_event(DUMMY_WEBHOOK_PAYLOAD, signature, timestamp)


def test_construct_event_from_strings(verify_key_base64, signer):
    telnyx.public_key = verify_key_base64
    timestamp = str(int(time.time()))
    signature = signer(DUMMY_WEBHOOK_PAYLOAD.decode("UTF-8"), timestamp=timestamp)
    event = telnyx.Webhook.construct_event(
        DUMMY_WEBHOOK_PAYLOAD.decode("UTF-8"), signature, timestamp
    )
    assert isinstance(event, telnyx.Event)


class TestWebhookSignature(object):

    # def test_raise_on_invalid_signature_for_payload(self, verify_key_base64, signer):
    #     telnyx.public_key = verify_key_base64
    #     timestamp = str(int(time.time())).encode('UTF-8')
    #     _signature = signer(DUMMY_WEBHOOK_PAYLOAD, timestamp)
    #     wrong_signature = signer(b"foo", timestamp)
    #     with pytest.raises(
    #         telnyx.error.SignatureVerificationError,
    #         match="Signature is invalid and does not match the payload",
    #     ):
    #         telnyx.WebhookSignature.verify(
    #             DUMMY_WEBHOOK_PAYLOAD, wrong_signature, timestamp
    #         )

    def test_raise_on_timestamp_outside_tolerance(self, verify_key_base64, signer):
        telnyx.public_key = verify_key_base64
        timestamp = str(int(time.time()) - 15).encode("UTF-8")
        signature = signer(DUMMY_WEBHOOK_PAYLOAD, timestamp)
        with pytest.raises(
            telnyx.error.SignatureVerificationError,
            match="Timestamp outside the tolerance zone",
        ):
            telnyx.WebhookSignature.verify(
                DUMMY_WEBHOOK_PAYLOAD, signature, timestamp, tolerance=10
            )

    def test_valid_header_and_signature(self, verify_key_base64, signer):
        telnyx.public_key = verify_key_base64
        timestamp = str(int(time.time())).encode("UTF-8")
        signature = signer(DUMMY_WEBHOOK_PAYLOAD, timestamp)
        assert telnyx.WebhookSignature.verify(
            DUMMY_WEBHOOK_PAYLOAD, signature, timestamp, tolerance=10
        )

    def test_timestamp_off_but_no_tolerance(self, verify_key_base64, signer):
        telnyx.public_key = verify_key_base64
        signature = signer(DUMMY_WEBHOOK_PAYLOAD, b"12345")
        assert telnyx.WebhookSignature.verify(
            DUMMY_WEBHOOK_PAYLOAD, signature, b"12345"
        )
