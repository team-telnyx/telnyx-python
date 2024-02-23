from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource, UpdateableAPIResource


class Autorechargepreference(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "autorechargepreference"
