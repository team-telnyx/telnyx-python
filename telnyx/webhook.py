from __future__ import absolute_import, division, print_function

import json
import time
import base64

from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

import telnyx
from telnyx import error


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload, signature_header, timestamp, tolerance=DEFAULT_TOLERANCE, api_key=None
    ):
        if hasattr(payload, "decode"):
            payload = payload.decode("utf-8")

        if WebhookSignature.verify(payload, signature_header, timestamp, tolerance):

            if api_key is None:
                api_key = telnyx.api_key
            data = json.loads(payload)
            event = telnyx.Event.construct_from(data, api_key)

            return event


class WebhookSignature(object):
    @classmethod
    def verify(cls, payload, signature_header, timestamp, tolerance=None):
        signed_payload = ("%s|%s" % (timestamp, payload)).encode("utf-8")
        public_key = telnyx.public_key
        signature = base64.b64decode(signature_header)

        # verify the data
        key = RSA.importKey(public_key)
        digest = SHA256.new()
        digest.update(signed_payload)
        verifier = PKCS1_v1_5.new(key)

        if not verifier.verify(digest, signature):
            raise error.SignatureVerificationError(
                "Signature is invalid and does not match the payload",
                signature_header,
                payload,
            )

        if tolerance and int(timestamp) < time.time() - tolerance:
            raise error.SignatureVerificationError(
                "Timestamp outside the tolerance zone (%s)" % timestamp,
                signature_header,
                payload,
            )

        return True
