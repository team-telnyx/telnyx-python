from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("extend", path="actions/extend", operations=["create"])
class NumberReservation(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "number_reservation"

    def extend(self, **params):
        return NumberReservation.create_extend(self.id, **params)
