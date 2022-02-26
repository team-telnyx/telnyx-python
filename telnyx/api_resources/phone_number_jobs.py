from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "update_emergency_settings",
    path="/v2/phone_numbers/jobs/update_emergency_settings",
    operations=["create"],
)
@nested_resource_class_methods(
    "update_phone_numbers",
    path="/v2/phone_numbers/jobs/update_phone_numbers",
    operations=["create"],
)
@nested_resource_class_methods(
    "delete_phone_numbers",
    path="/v2/phone_numbers/jobs/delete_phone_numbers",
    operations=["create"],
)
class PhoneNumberJob(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "phone_number_job"

    @classmethod
    def class_url(cls):
        return "/v2/phone_numbers/jobs"

    @classmethod
    def update_emergency_settings(cls, **params):
        return PhoneNumberJob.create_update_emergency_settings(None, **params)

    @classmethod
    def update_phone_numbers(cls, **params):
        return PhoneNumberJob.create_update_phone_numbers(None, **params)

    @classmethod
    def delete_phone_numbers(cls, **params):
        return PhoneNumberJob.create_delete_phone_numbers(None, **params)
