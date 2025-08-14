# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(BaseModel):
    success: Optional[bool] = None
    """Describes wether or not the operation was successful"""

    ticket_id: Optional[str] = None
    """Ticket id of the upload request"""
