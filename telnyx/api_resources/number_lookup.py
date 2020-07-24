from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import APIResource


class NumberLookup(APIResource):
    OBJECT_NAME = "number_lookup"

    @classmethod
    def class_url(cls):
        return "/v2/number_lookup"
