from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "phone_numbers", path="phoneNumbers", operations=["list"]
)
class PhoneNumberByProfile(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "phone_number_assignment_by_profile"

    @classmethod
    def class_url(cls):
        return "/10dlc/phoneNumberAssignmentByProfile"

    def phone_numbers(self, **params):
        return PhoneNumberByProfile.list_mno_metadata(self.name, **params)
