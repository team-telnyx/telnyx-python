# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KvDeleteResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    record_type: Optional[str] = None

    status: Optional[Literal["pending", "provision_ok", "provision_failed", "deleting", "delete_failed"]] = None
    """Provisioning status.

    A namespace is usable once `status` is `provision_ok`. Once deletion completes,
    the namespace no longer appears in the API.
    """

    updated_at: Optional[datetime] = None


class KvDeleteResponse(BaseModel):
    data: Optional[Data] = None
