from __future__ import absolute_import, division, print_function

import base64
import time

from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import pytest

try:
    from unittest import mock
except ImportError:
    # Python 2.7
    import mock

import telnyx
from telnyx import six


DUMMY_WEBHOOK_PAYLOAD = """{
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

PUBLIC_KEY = """\
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwy/jPkkgBo7oQermYujj
AmSqN+aHNg+D4K85lKn6T3khJ8O2t/FrgN5qSGqg+0U5hoIHZflEon28lbLdf6gZ
jPeKQ2a24w5zroR6e4MM00RyJWA6MWXdo6Tn6xqKMYuT8LffEJGnXCH4yTIkxAVD
yK0dfewhtrlpmW5ojXcDCrZ3Oo1o588PLNwSIuQwU7wHZwOLglWxFt6LZ9Ps8zYf
QNH/pXNczf1E4rGZ1QxrzqFbndvjCE5VDRhULhycT/X0H2EMvNgHsDQk4OhENnzo
Cal3vO5+P9MgC7NSZCR8Ubebq0tanL5dj5GGYyjWmeq3QhfDLX2mTpIv/B0e8+hg
8QIDAQAB
-----END PUBLIC KEY-----"""

PRIVATE_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwy/jPkkgBo7oQermYujjAmSqN+aHNg+D4K85lKn6T3khJ8O2
t/FrgN5qSGqg+0U5hoIHZflEon28lbLdf6gZjPeKQ2a24w5zroR6e4MM00RyJWA6
MWXdo6Tn6xqKMYuT8LffEJGnXCH4yTIkxAVDyK0dfewhtrlpmW5ojXcDCrZ3Oo1o
588PLNwSIuQwU7wHZwOLglWxFt6LZ9Ps8zYfQNH/pXNczf1E4rGZ1QxrzqFbndvj
CE5VDRhULhycT/X0H2EMvNgHsDQk4OhENnzoCal3vO5+P9MgC7NSZCR8Ubebq0ta
nL5dj5GGYyjWmeq3QhfDLX2mTpIv/B0e8+hg8QIDAQABAoIBAQCNwoP6wsVdvgD1
jxNQlu/41v/Bpc5h9xbC4sChNmqzubfY144nPlHjwKXUfoz4sag8Bsg0ybuNgGCt
IME6a+5SsZ5boYgGlIJ0J4eFmQKBll6IwsDBC8jTh3thB1+C6GrEE+cQc5jnk0zL
Y33MWD6IyyJ2SD+cJEGLy+JnjB5LckGCQXWPQXwvpIKgGmFoLQzHCKfeKHZ3olB8
C1+YKrQzLtyuuH9obDWxRSrqI5gOI/76PWmo+weNa4OrfFtBf5O9bo5OD17ilIT/
uNpxb/7rOkpwU9x6D00/D/S7ecCdVoL2yBB5L635TNQKXxhvdSmBg1ceLlztwsUL
OHIlglTZAoGBAOY3wyincm8iAUxLE+Z3AeTD94pjND4g2JXFF9E7UDxgRD6E3n38
ubNRdAMkxDmDYgyIOZsebykMadQ2vNiWqTjOBr6hxyQMFutHWrIJOU+peFCepn8u
NX3Xg44l7KcwwqX5svoqgFl1FKwNpBOSo50oGX4lAgqtjYqEeMInfjZ7AoGBANkL
z0wBNAr9oXsc0BN2WkQXB34RU/WcrymhxHfc+ZRzRShk9LOdBTuMYnj4rtjdG849
JDDWlMk7UlzGjI07G5aT+n8Aq69BhV0IARC9PafTncE6G3sHswAQudHiurLflP9C
oj6kTakunrq8Kgj3Q1p6Ie+Hv7E01A3D0Difr4CDAoGAXORrLuBB4G3MMEirAvdK
IFCidYiJ7/e47NXWQmq4eWQupTtfu15aX+yh7xLKypok2gGtnNWu7NVBbouXr507
MtyPBCSrAfSO2uizw9rM8UPkdENP00mF8/0d7CGJV/zozafve9niaDZB3Rqz9eHZ
evRPNQMhy8Uzs4y4XT8qQjkCgYBNuLjmkpe8R86Hc23fSkZQk56POk1CanUfB1p/
QZXt3skpCd3GY7f39vFcOFEEP0kxtRs8kdp9pMx9hGvYNw5OAXd1+xt/iorjIXag
M+PcMR8QjmpAyCUFJPglfHc2jnGgZpAKtnNI3fThEXhL9Z8cyxdT2tx97FjzBOeP
Hz+NWQKBgQCU0bSxTp2rbOCxHosQ/GDDTY0JkQ2z5q1SkibSiEnyAZ3yCHpXZRD7
sa5BWs4qlasSKmxdmT9xgRDAL6CJH6kJizF3UIaIPOvPjIroOa7Mk1OFNbOi6Cao
0LcWp5w1I2r5g7sOIRM/AcS3yVT5RJO4KB8WyDOvxCfP8cFsTacZmQ==
-----END RSA PRIVATE KEY-----"""


def generate_signature(**kwargs):
    timestamp = kwargs.get("timestamp", str(int(time.time())))
    payload = kwargs.get("payload", DUMMY_WEBHOOK_PAYLOAD)
    private_key = kwargs.get("private_key", PRIVATE_KEY)
    private_key = RSA.importKey(private_key)

    digest = SHA256.new()
    digest.update(("%s|%s" % (timestamp, payload)).encode("utf-8"))

    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    return base64.b64encode(sig)


class TestWebhook(object):
    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_construct_event(self):
        timestamp = str(int(time.time()))
        signature = generate_signature(timestamp=timestamp)
        event = telnyx.Webhook.construct_event(
            DUMMY_WEBHOOK_PAYLOAD, signature, timestamp
        )
        assert isinstance(event, telnyx.Event)

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_raise_on_json_error(self):
        payload = "this is not valid JSON"
        timestamp = str(int(time.time()))
        signature = generate_signature(payload=payload, timestamp=timestamp)
        with pytest.raises(ValueError):
            telnyx.Webhook.construct_event(payload, signature, timestamp)

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_raise_on_invalid_header(self):
        signature = "FAKEFAKEFAKE"
        timestamp = str(int(time.time()))
        with pytest.raises(telnyx.error.SignatureVerificationError):
            telnyx.Webhook.construct_event(DUMMY_WEBHOOK_PAYLOAD, signature, timestamp)

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_construct_event_from_bytearray(self):
        timestamp = str(int(time.time()))
        signature = generate_signature(timestamp=timestamp)
        payload = bytearray(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = telnyx.Webhook.construct_event(payload, signature, timestamp)
        assert isinstance(event, telnyx.Event)

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_construct_event_from_bytes(self):
        # This test is only applicable to Python 3 as `bytes` is not a symbol
        # in Python 2.
        if six.PY2:
            return

        timestamp = str(int(time.time()))
        payload = bytes(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        signature = generate_signature(timestamp=timestamp)
        event = telnyx.Webhook.construct_event(payload, signature, timestamp)
        assert isinstance(event, telnyx.Event)


class TestWebhookSignature(object):
    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_raise_on_invalid_signature_for_payload(self):
        timestamp = str(int(time.time()))
        _signature = generate_signature(timestamp=timestamp)  # noqa: F841
        wrong_signature = generate_signature(payload="foo", timestamp=timestamp)
        with pytest.raises(
            telnyx.error.SignatureVerificationError,
            match="Signature is invalid and does not match the payload",
        ):
            telnyx.WebhookSignature.verify(
                DUMMY_WEBHOOK_PAYLOAD, wrong_signature, timestamp
            )

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_raise_on_timestamp_outside_tolerance(self):
        timestamp = str(int(time.time()) - 15)
        signature = generate_signature(timestamp=str(timestamp))
        with pytest.raises(
            telnyx.error.SignatureVerificationError,
            match="Timestamp outside the tolerance zone",
        ):
            telnyx.WebhookSignature.verify(
                DUMMY_WEBHOOK_PAYLOAD, signature, str(timestamp), tolerance=10
            )

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_valid_header_and_signature(self):
        timestamp = str(int(time.time()))
        signature = generate_signature(timestamp=timestamp)
        assert telnyx.WebhookSignature.verify(
            DUMMY_WEBHOOK_PAYLOAD, signature, timestamp, tolerance=10
        )

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_header_contains_valid_signature(self):
        timestamp = str(int(time.time()))
        signature = generate_signature(timestamp=timestamp)
        assert telnyx.WebhookSignature.verify(
            DUMMY_WEBHOOK_PAYLOAD, signature, timestamp, tolerance=10
        )

    @mock.patch.object(telnyx, "public_key", PUBLIC_KEY)
    def test_timestamp_off_but_no_tolerance(self):
        signature = generate_signature(timestamp="12345")
        assert telnyx.WebhookSignature.verify(DUMMY_WEBHOOK_PAYLOAD, signature, "12345")
