from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import DeletableAPIResource


class MessagingHostedNumber(DeletableAPIResource):
    OBJECT_NAME = "messaging_hosted_number"
