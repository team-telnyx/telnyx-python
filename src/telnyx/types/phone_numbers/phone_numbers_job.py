# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..phone_number_blocks.job_error import JobError

__all__ = ["PhoneNumbersJob", "FailedOperation", "PendingOperation", "PhoneNumber", "SuccessfulOperation"]


class FailedOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    errors: Optional[List[JobError]] = None

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class PendingOperation(BaseModel):
    """The phone numbers pending confirmation on update results.

    Entries in this list are transient, and will be moved to either successful_operations or failed_operations once the processing is done.
    """

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class PhoneNumber(BaseModel):
    """The unique phone numbers given as arguments in the job creation."""

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class SuccessfulOperation(BaseModel):
    """The phone numbers successfully updated."""

    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class PhoneNumbersJob(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    etc: Optional[datetime] = None
    """
    ISO 8601 formatted date indicating when the estimated time of completion of the
    background job.
    """

    failed_operations: Optional[List[FailedOperation]] = None

    pending_operations: Optional[List[PendingOperation]] = None

    phone_numbers: Optional[List[PhoneNumber]] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["pending", "in_progress", "completed", "failed", "expired"]] = None
    """Indicates the completion status of the background update."""

    successful_operations: Optional[List[SuccessfulOperation]] = None

    type: Optional[Literal["update_emergency_settings", "delete_phone_numbers", "update_phone_numbers"]] = None
    """Identifies the type of the background job."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was updated."""
