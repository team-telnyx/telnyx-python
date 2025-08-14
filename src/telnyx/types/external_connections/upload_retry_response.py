# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UploadRetryResponse", "Data", "DataTnUploadEntry"]


class DataTnUploadEntry(BaseModel):
    civic_address_id: Optional[str] = None
    """Identifies the civic address assigned to the phone number entry."""

    error_code: Optional[
        Literal[
            "internal_error",
            "unable_to_retrieve_default_location",
            "unknown_country_code",
            "unable_to_retrieve_location",
            "unable_to_retrieve_partner_info",
            "unable_to_match_geography_entry",
        ]
    ] = None
    """
    A code returned by Microsoft Teams if there is an error with the phone number
    entry upload.
    """

    error_message: Optional[str] = None
    """
    A message returned by Microsoft Teams if there is an error with the upload
    process.
    """

    internal_status: Optional[
        Literal[
            "pending_assignment",
            "in_progress",
            "all_internal_jobs_completed",
            "release_requested",
            "release_completed",
            "error",
        ]
    ] = None
    """Represents the status of the phone number entry upload on Telnyx."""

    location_id: Optional[str] = None
    """Identifies the location assigned to the phone number entry."""

    number_id: Optional[str] = None
    """Uniquely identifies the resource."""

    phone_number: Optional[str] = None
    """Phone number in E164 format."""

    status: Optional[Literal["pending_upload", "pending", "in_progress", "success", "error"]] = None
    """Represents the status of the phone number entry upload on Microsoft Teams."""


class Data(BaseModel):
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

    tn_upload_entries: Optional[List[DataTnUploadEntry]] = None


class UploadRetryResponse(BaseModel):
    data: Optional[Data] = None
