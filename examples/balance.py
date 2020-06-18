from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Getting User Balance")

resp = telnyx.Balance.retrieve()

print("Your available credit: {} {}".format(resp.available_credit, resp.currency))
print(resp)
