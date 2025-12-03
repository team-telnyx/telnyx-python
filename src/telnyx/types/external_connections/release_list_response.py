# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..external_voice_integrations_pagination_meta import ExternalVoiceIntegrationsPaginationMeta

__all__ = ["ReleaseListResponse", "Data", "DataTelephoneNumber"]


class DataTelephoneNumber(BaseModel):
    number_id: Optional[str] = None
    """Phone number ID from the Telnyx API."""

    phone_number: Optional[str] = None
    """Phone number in E164 format."""


class Data(BaseModel):
    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    error_message: Optional[str] = None
    """A message set if there is an error with the upload process."""

    status: Optional[
        Literal["pending_upload", "pending", "in_progress", "complete", "failed", "expired", "unknown"]
    ] = None
    """Represents the status of the release on Microsoft Teams."""

    telephone_numbers: Optional[List[DataTelephoneNumber]] = None

    tenant_id: Optional[str] = None

    ticket_id: Optional[str] = None
    """Uniquely identifies the resource."""


class ReleaseListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[ExternalVoiceIntegrationsPaginationMeta] = None
