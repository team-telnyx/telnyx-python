# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .tn_upload_entry import TnUploadEntry

__all__ = ["Upload"]


class Upload(BaseModel):
    available_usages: Optional[List[Literal["calling_user_assignment", "first_party_app_assignment"]]] = None

    error_code: Optional[str] = None
    """
    A code returned by Microsoft Teams if there is an error with the upload process.
    """

    error_message: Optional[str] = None
    """A message set if there is an error with the upload process."""

    location_id: Optional[str] = None

    status: Optional[Literal["pending_upload", "pending", "in_progress", "partial_success", "success", "error"]] = None
    """Represents the status of the upload on Microsoft Teams."""

    tenant_id: Optional[str] = None

    ticket_id: Optional[str] = None
    """Uniquely identifies the resource."""

    tn_upload_entries: Optional[List[TnUploadEntry]] = None
