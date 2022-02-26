from __future__ import absolute_import, division, print_function

from telnyx import error
from telnyx.api_resources.abstract import ListableAPIResource


class InventoryCoverage(ListableAPIResource):
    OBJECT_NAME = "inventory_coverage"

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise error.InvalidRequestError(
            "%s does not support retrieve()" % cls.class_url()
        )

    @classmethod
    def class_url(cls):
        return "/v2/inventory_coverage"
