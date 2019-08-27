from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Attempting to perform a available phone number search...")

resp = telnyx.AvailablePhoneNumber.list(filter={"country_code": "US", "limit": 10})

print("Success: %r" % (resp))
