from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)


class NotificationChannel(
    ListableAPIResource,
    CreateableAPIResource,
    UpdateableAPIResource,
    DeletableAPIResource,
):
    OBJECT_NAME = "notification_channel"
