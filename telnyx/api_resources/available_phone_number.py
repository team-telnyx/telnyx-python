from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class AvailablePhoneNumber(ListableAPIResource):
    OBJECT_NAME = "available_phone_number"
