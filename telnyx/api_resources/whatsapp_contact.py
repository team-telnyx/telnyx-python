from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource


class WhatsappContact(CreateableAPIResource):
    OBJECT_NAME = "whatsapp_contact"
