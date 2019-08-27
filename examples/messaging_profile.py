from __future__ import absolute_import, division, print_function

import os

import telnyx

telnyx.api_key = os.environ.get("TELNYX_SECRET_KEY")

print("Attempting to create messaging profile...")

resp = telnyx.MessagingProfile.create(name="Campaign Messaging Profile")

print("Success: %r" % (resp))
