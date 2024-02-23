from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "enable_emergency", path="actions/enable_emergency", operations=["create"]
)
class PhoneNumberConfiguration(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "phone_number_configuration"

    def enable_emergency(self, **params):
        return self.create_enable_emergency(**params)
