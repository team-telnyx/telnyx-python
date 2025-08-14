# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from datetime import datetime

from .._models import BaseModel

__all__ = ["PushCredential"]


class PushCredential(BaseModel):
    id: str
    """Unique identifier of a push credential"""

    alias: str
    """Alias to uniquely identify a credential"""

    certificate: str
    """Apple certificate for sending push notifications. For iOS only"""

    created_at: datetime
    """ISO 8601 timestamp when the room was created"""

    private_key: str
    """Apple private key for a given certificate for sending push notifications.

    For iOS only
    """

    project_account_json_file: Dict[str, object]
    """Google server key for sending push notifications. For Android only"""

    record_type: str

    type: str
    """Type of mobile push credential. Either <code>ios</code> or <code>android</code>"""

    updated_at: datetime
    """ISO 8601 timestamp when the room was updated."""
