# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .rcs_agent_message import RcsAgentMessage

__all__ = ["MesssageRcsResponse", "Data", "DataFrom", "DataTo"]


class DataFrom(BaseModel):
    agent_id: Optional[str] = None
    """agent ID"""

    agent_name: Optional[str] = None

    carrier: Optional[str] = None


class DataTo(BaseModel):
    carrier: Optional[str] = None

    line_type: Optional[str] = None

    phone_number: Optional[str] = None

    status: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None
    """message ID"""

    body: Optional[RcsAgentMessage] = None

    direction: Optional[str] = None

    encoding: Optional[str] = None

    from_: Optional[DataFrom] = FieldInfo(alias="from", default=None)

    messaging_profile_id: Optional[str] = None

    organization_id: Optional[str] = None

    received_at: Optional[datetime] = None

    record_type: Optional[str] = None

    to: Optional[List[DataTo]] = None

    type: Optional[str] = None


class MesssageRcsResponse(BaseModel):
    data: Optional[Data] = None
