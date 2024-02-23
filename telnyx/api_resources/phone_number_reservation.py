from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("extend", path="actions/extend", operations=["create"])
class PhoneNumberReservation(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "phone_number_reservation"

    def extend(self, **params):
        return self.create_extend(**params)
