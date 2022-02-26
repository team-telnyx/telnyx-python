from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class WhatsappMedia(ListableAPIResource, CreateableAPIResource, DeletableAPIResource):
    OBJECT_NAME = "whatsapp_media"

    @classmethod
    def class_url(cls):
        return "/v2/whatsapp_media"
