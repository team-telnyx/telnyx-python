from __future__ import absolute_import, division, print_function

import os

from flask import Flask, request

import telnyx

telnyx.api_key = os.environ.get("TELNYX_API_KEY")
public_key = os.environ.get("TELNYX_PUBLIC_KEY")

app = Flask(__name__)


@app.route("/webhooks", methods=["POST"])
def webhooks():
    body = request.data.decode("utf-8")
    signature = request.headers.get("Telnyx-Signature-PKCS1-15", None)
    timestamp = request.headers.get("Telnyx-Timestamp", None)

    try:
        event = telnyx.Webhook.construct_event(body, signature, timestamp, public_key)
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except telnyx.error.SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    print("Received event: id={id}, type={type}".format(id=event.id, type=event.type))

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
