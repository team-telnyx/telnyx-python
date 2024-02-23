from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource, UpdateableAPIResource


class NumberConfiguration(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "number_configuration"
