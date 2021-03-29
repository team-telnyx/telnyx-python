from __future__ import absolute_import, division, print_function

from telnyx import error
from telnyx.api_resources.abstract import ListableAPIResource


class PhoneNumberRegulatoryRequirement(ListableAPIResource):
    OBJECT_NAME = "phone_number_regulatory_requirement"

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise error.InvalidRequestError(
            "%s does not support retrieve()" % cls.class_url()
        )

    @classmethod
    def class_url(cls):
        return "/v2/phone_numbers_regulatory_requirements"
