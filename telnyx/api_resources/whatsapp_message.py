from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods
)


class WhatsappMessage(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource
):
    OBJECT_NAME = "whatsapp_message"
