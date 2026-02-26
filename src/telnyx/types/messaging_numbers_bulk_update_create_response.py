# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bulk_messaging_settings_update_phone_numbers import BulkMessagingSettingsUpdatePhoneNumbers

__all__ = ["MessagingNumbersBulkUpdateCreateResponse"]


class MessagingNumbersBulkUpdateCreateResponse(BaseModel):
    data: Optional[BulkMessagingSettingsUpdatePhoneNumbers] = None
