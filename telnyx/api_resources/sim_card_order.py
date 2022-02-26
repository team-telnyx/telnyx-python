from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource, ListableAPIResource


class SIMCardOrder(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "sim_card_order"


class SIMCardOrderPreview(CreateableAPIResource):
    OBJECT_NAME = "sim_card_order_preview"

    @classmethod
    def class_url(cls):
        return "/v2/sim_card_order_preview"
