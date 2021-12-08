from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)

class WhatsappMessage(
    CreateableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "whatsapp_message"