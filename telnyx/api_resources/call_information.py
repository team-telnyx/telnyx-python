from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import ListableAPIResource


class CallInformation(ListableAPIResource):
    OBJECT_NAME = "call_information"
