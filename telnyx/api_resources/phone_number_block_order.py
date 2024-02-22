from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource, ListableAPIResource


class PhoneNumberBlockOrder(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "phone_number_block_order"
