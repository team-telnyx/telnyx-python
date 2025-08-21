# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Conference", "EndedBy"]


class EndedBy(BaseModel):
    call_control_id: Optional[str] = None
    """Call Control ID which ended the conference"""

    call_session_id: Optional[str] = None
    """Call Session ID which ended the conference"""


class Conference(BaseModel):
    id: str
    """Uniquely identifies the conference"""

    created_at: str
    """ISO 8601 formatted date of when the conference was created"""

    expires_at: str
    """ISO 8601 formatted date of when the conference will expire"""

    name: str
    """Name of the conference"""

    record_type: Literal["conference"]

    connection_id: Optional[str] = None
    """Identifies the connection associated with the conference"""

    end_reason: Optional[Literal["all_left", "ended_via_api", "host_left", "time_exceeded"]] = None
    """Reason why the conference ended"""

    ended_by: Optional[EndedBy] = None
    """IDs related to who ended the conference.

    It is expected for them to all be there or all be null
    """

    region: Optional[str] = None
    """Region where the conference is hosted"""

    status: Optional[Literal["init", "in_progress", "completed"]] = None
    """Status of the conference"""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the conference was last updated"""
