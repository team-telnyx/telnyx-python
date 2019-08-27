from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource, UpdateableAPIResource


class MessagingPhoneNumber(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "messaging_phone_number"
