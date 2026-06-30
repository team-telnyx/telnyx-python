# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ....._models import BaseModel

if TYPE_CHECKING:
    from ..whatsapp_profile_data import WhatsappProfileData

__all__ = ["PhotoUploadResponse"]


class PhotoUploadResponse(BaseModel):
    data: Optional[WhatsappProfileData] = None
