from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Listing out reservations...")

list_resp = telnyx.NumberReservation.list()

print("Success: %r" % list_resp)

print("Attempting to create a number reservation...")

create_resp = telnyx.NumberReservation.create(
    phone_numbers=[{"phone_number": "+13122708615"}]
)

print("Success: %r" % create_resp)
