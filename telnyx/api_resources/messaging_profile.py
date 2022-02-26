from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("phone_number", operations=["list"])
@nested_resource_class_methods("short_code", operations=["list"])
@nested_resource_class_methods("metrics", operations=["list"])
class MessagingProfile(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "messaging_profile"

    def phone_numbers(self, **params):
        return MessagingProfile.list_phone_numbers(self.id, **params)

    def short_codes(self, **params):
        return MessagingProfile.list_short_codes(self.id, **params)

    def metrics(self, **params):
        return MessagingProfile.list_metrics(self.id, **params)
