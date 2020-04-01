from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import UpdateableAPIResource


class InboundChannel(UpdateableAPIResource):
    OBJECT_NAME = "inbound_channels"

    def instance_url(self):
        return "/v2/phone_numbers/inbound_channels"

    @classmethod
    def modify(cls, **params):
        url = "/v2/phone_numbers/inbound_channels"
        return cls._modify(url, **params)

    @classmethod
    def retrieve(cls, api_key=None, **params):
        return super(InboundChannel, cls).retrieve(None, api_key, **params)

    def save_method(self):
        return "patch"
