from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource, ListableAPIResource


class BulkPhoneNumberCampaign(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "bulk_phone_number_campaign"
