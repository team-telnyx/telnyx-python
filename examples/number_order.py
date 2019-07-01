from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Attempting to list number orders...")

list_resp = telnyx.NumberOrder.list()

print("Success: %r" % (list_resp))

print("Attempting to create a number order...")

create_resp = telnyx.NumberOrder.create(
    phone_numbers=[{"phone_number": "+13122708619"}], customer_reference="MY REF 001"
)

print("Success: %r" % (create_resp))
