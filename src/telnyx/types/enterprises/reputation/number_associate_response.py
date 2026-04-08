# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...shared.meta_info import MetaInfo

__all__ = ["NumberAssociateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = None
    """When the number was associated"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    phone_number: Optional[str] = None
    """Phone number in E.164 format"""

    updated_at: Optional[datetime] = None
    """When the record was last updated"""


class NumberAssociateResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[MetaInfo] = None
