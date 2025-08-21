# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PhoneNumbersJob",
    "FailedOperation",
    "FailedOperationError",
    "FailedOperationErrorMeta",
    "FailedOperationErrorSource",
    "PendingOperation",
    "PhoneNumber",
    "SuccessfulOperation",
]


class FailedOperationErrorMeta(BaseModel):
    url: Optional[str] = None
    """URL with additional information on the error."""


class FailedOperationErrorSource(BaseModel):
    parameter: Optional[str] = None
    """Indicates which query parameter caused the error."""

    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class FailedOperationError(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[FailedOperationErrorMeta] = None

    source: Optional[FailedOperationErrorSource] = None


class FailedOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    errors: Optional[List[FailedOperationError]] = None

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class PendingOperation(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class PhoneNumber(BaseModel):
    id: Optional[str] = None
    """The phone number's ID"""

    phone_number: Optional[str] = None
    """The phone number in e164 format."""


class SuccessfulOperation(BaseModel):
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
