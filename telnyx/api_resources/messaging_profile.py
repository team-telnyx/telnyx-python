from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource
from telnyx.api_resources.abstract import DeletableAPIResource
from telnyx.api_resources.abstract import UpdateableAPIResource
from telnyx.api_resources.abstract import ListableAPIResource
from telnyx.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("phone_number", operations=["list"])
@nested_resource_class_methods("short_code", operations=["list"])
@nested_resource_class_methods("alphanumeric_sender_id", operations=["list"])
class MessagingProfile(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "messaging_profile"

    def phone_numbers(self):
        return MessagingProfile.list_phone_numbers(self.id)

    def short_codes(self):
        return MessagingProfile.list_short_codes(self.id)

    def alphanumeric_sender_ids(self):
        return MessagingProfile.list_alphanumeric_sender_ids(self.id)
