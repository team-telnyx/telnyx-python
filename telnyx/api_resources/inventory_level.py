from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class InventoryLevel(ListableAPIResource):
    OBJECT_NAME = "inventory_level"
