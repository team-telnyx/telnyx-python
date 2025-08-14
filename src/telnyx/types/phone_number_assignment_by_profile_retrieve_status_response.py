# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .task_status import TaskStatus

__all__ = ["PhoneNumberAssignmentByProfileRetrieveStatusResponse"]


class PhoneNumberAssignmentByProfileRetrieveStatusResponse(BaseModel):
    status: TaskStatus
    """An enumeration."""

    task_id: str = FieldInfo(alias="taskId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
