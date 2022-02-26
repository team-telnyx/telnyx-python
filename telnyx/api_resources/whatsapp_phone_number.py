from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource, UpdateableAPIResource


class WhatsappPhoneNumber(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "whatsapp_phone_number"
