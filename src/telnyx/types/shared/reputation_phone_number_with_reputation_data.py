# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from . import reputation_data
from ..._models import BaseModel

__all__ = ["ReputationPhoneNumberWithReputationData", "ReputationData"]

ReputationData: TypeAlias = Union[reputation_data.ReputationData, Optional[Dict[str, object]]]


class ReputationPhoneNumberWithReputationData(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = None
    """When the number was associated"""

    enterprise_id: Optional[str] = None
    """ID of the associated enterprise"""

    phone_number: Optional[str] = None
    """Phone number in E.164 format"""

    reputation_data: Optional[ReputationData] = None
    """Reputation metrics (null if not yet fetched)"""

    updated_at: Optional[datetime] = None
    """When the record was last updated"""
