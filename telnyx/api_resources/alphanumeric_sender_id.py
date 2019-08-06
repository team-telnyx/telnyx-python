from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource
from telnyx.api_resources.abstract import DeletableAPIResource
from telnyx.api_resources.abstract import UpdateableAPIResource
from telnyx.api_resources.abstract import ListableAPIResource


class AlphanumericSenderId(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "alphanumeric_sender_id"
