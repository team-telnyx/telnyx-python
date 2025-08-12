# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .notification_setting import NotificationSetting

__all__ = ["NotificationSettingDeleteResponse"]


class NotificationSettingDeleteResponse(BaseModel):
    data: Optional[NotificationSetting] = None
