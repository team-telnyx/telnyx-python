from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("confirm", path="actions/confirm", operations=["create"])
@nested_resource_class_methods("cancel", path="actions/cancel", operations=["create"])
@nested_resource_class_methods(
    "loa_template", path="loa_template", operations=["retrieve"]
)
@nested_resource_class_methods(
    "allowed_foc_windows", path="allowed_foc_windows", operations=["list"]
)
@nested_resource_class_methods(
    "activation_jobs", path="activation_jobs", operations=["list"]
)
class PortingOrder(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "porting_order"

    def confirm(self, **params):
        return PortingOrder.create_confirm(self.id, **params)

    def loaTemplate(self, **params):
        return PortingOrder.retrieve_loa_template(self.id, **params)

    def cancel(self, **params):
        return PortingOrder.create_cancel(self.id, **params)

    def allowed_foc_windows(self, **params):
        return PortingOrder.list_allowed_foc_windows(self.id, **params)

    def activation_jobs(self, **params):
        return PortingOrder.list_activation_jobs(self.id, **params)


class PortingPhoneNumber(ListableAPIResource):
    OBJECT_NAME = "porting_phone_number"
