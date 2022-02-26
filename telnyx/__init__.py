from __future__ import absolute_import, division, print_function

import os

from telnyx.api_resources import *  # noqa
from telnyx.webhook import Webhook, WebhookSignature  # noqa

# Telnyx Python bindings
# API docs at http://developers.telnyx.com

# Configuration variables

api_key = os.environ.get("TELNYX_API_KEY")
api_base = os.environ.get("TELNYX_API_BASE", "https://api.telnyx.com")
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None
max_network_retries = 0

public_key = os.environ.get("TELNYX_PUBLIC_KEY")

# Set to either 'debug' or 'info', controls console logging
log = None


__version__ = "2.0.0"


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Telnyx.
#
# Takes a name and optional version and plugin URL.
def set_app_info(name, url=None, version=None):
    global app_info
    app_info = {"name": name, "url": url, "version": version}
