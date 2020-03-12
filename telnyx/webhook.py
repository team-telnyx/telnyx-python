from __future__ import absolute_import, division, print_function

import base64
import json
import time

from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey

import telnyx
from telnyx import error


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload, signature_header, timestamp, tolerance=DEFAULT_TOLERANCE, api_key=None
    ):

        if WebhookSignature.verify(payload, signature_header, timestamp, tolerance):

            if api_key is None:
                api_key = telnyx.api_key

            if hasattr(payload, "decode"):
                payload = payload.decode("utf-8")

            data = json.loads(payload)
            event = telnyx.Event.construct_from(data, api_key)

            return event


class WebhookSignature(object):
    @classmethod
    def verify(cls, payload, signature, timestamp, tolerance=None):
        if hasattr(timestamp, "encode"):
            timestamp = timestamp.encode("utf-8")

        if hasattr(payload, "encode"):
            payload = payload.encode("utf-8")

        signed_payload = timestamp + b"|" + payload
        public_key = telnyx.public_key

        if not public_key:
            raise error.SignatureVerificationError(
                "Public key not set", signature, payload
            )

        # verify the data
        key = VerifyKey(public_key, encoder=Base64Encoder)

        if not key.verify(signed_payload, signature=base64.b64decode(signature)):
            raise error.SignatureVerificationError(
                "Signature is invalid and does not match the payload",
                signature,
                payload,
            )

        if tolerance and int(timestamp) < time.time() - tolerance:
            raise error.SignatureVerificationError(
                "Timestamp outside the tolerance zone (%s)" % timestamp,
                signature,
                payload,
            )

        return True
