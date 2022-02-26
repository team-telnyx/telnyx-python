from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    nested_resource_class_methods
)


class WhatsappContact(
    CreateableAPIResource
):
    OBJECT_NAME = "whatsapp_contact"
