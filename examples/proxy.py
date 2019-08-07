from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Attempting to create Messaging Profile...")

telnyx.proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    telnyx.http_client.RequestsClient(
        verify_ssl_certs=telnyx.verify_ssl_certs, proxy=telnyx.proxy
    ),
    telnyx.http_client.PycurlClient(
        verify_ssl_certs=telnyx.verify_ssl_certs, proxy=telnyx.proxy
    ),
    telnyx.http_client.Urllib2Client(
        verify_ssl_certs=telnyx.verify_ssl_certs, proxy=telnyx.proxy
    ),
)

for c in clients:
    telnyx.default_http_client = c
    resp = telnyx.MessagingProfile.create(name="Campaign Messaging Profile")
    print("Success: %s, %r" % (c.name, resp))
