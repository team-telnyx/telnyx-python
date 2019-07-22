from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

# For this demo you might want to have a valid number to reserve
# You can search for a number using https://portaldev.telnyx.com; OR
# using telnyx.AvailablePhoneNumber
_telephone_number = ""

print("Listing out reservations...")

list_resp = telnyx.NumberReservation.list()

print("Success: {}".format(list_resp))

print("Attempting to create a number reservation...")

create_resp = telnyx.NumberReservation.create(
    phone_numbers=[{"phone_number": _telephone_number}]
)

print("Success: {}".format(create_resp))

print("Attempting to extend recently created reservation...")

extension = create_resp.extend()

print("Success extending reservation: {}".format(extension))
