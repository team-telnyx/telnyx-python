from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class WebhookDeliveries(ListableAPIResource):
    OBJECT_NAME = "webhook_deliveries"

    @classmethod
    def class_url(cls):
        return "/v2/webhook_deliveries"
