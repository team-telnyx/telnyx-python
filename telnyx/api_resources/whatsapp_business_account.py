from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("phone_numbers", path="phone_numbers", operations=["list"])
class WhatsappBusinessAccount(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "whatsapp_business_account"

    def phone_numbers(self, **params):
        return WhatsappBusinessAccount.create_enable(self.id, **params)

