from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource


class PhoneNumberPorting(CreateableAPIResource):
    OBJECT_NAME = "phone_number_porting"
