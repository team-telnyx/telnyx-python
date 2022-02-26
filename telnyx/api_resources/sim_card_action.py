from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class SIMCardAction(ListableAPIResource):
    OBJECT_NAME = "sim_card_action"
