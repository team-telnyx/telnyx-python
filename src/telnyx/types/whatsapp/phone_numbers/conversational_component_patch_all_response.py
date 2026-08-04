# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConversationalComponentPatchAllResponse", "Data", "DataCommand"]


class DataCommand(BaseModel):
    command: Optional[str] = None

    description: Optional[str] = None


class Data(BaseModel):
    commands: Optional[List[DataCommand]] = None
    """List of commands"""

    ice_breakers: Optional[List[str]] = None
    """List of ice breakers"""

    phone_number: Optional[str] = None
    """Phone number in E164 format"""

    record_type: Optional[str] = None


class ConversationalComponentPatchAllResponse(BaseModel):
    data: Optional[Data] = None
