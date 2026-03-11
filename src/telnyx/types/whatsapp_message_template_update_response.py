# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WhatsappMessageTemplateUpdateResponse", "Data", "DataWhatsappBusinessAccount"]


class DataWhatsappBusinessAccount(BaseModel):
    id: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    category: Optional[Literal["MARKETING", "UTILITY", "AUTHENTICATION"]] = None

    components: Optional[List[object]] = None
    """Whatsapp template components (header, body, footer, buttons)"""

    created_at: Optional[datetime] = None

    language: Optional[str] = None

    name: Optional[str] = None

    record_type: Optional[str] = None

    rejection_reason: Optional[str] = None

    status: Optional[str] = None

    template_id: Optional[str] = None

    updated_at: Optional[datetime] = None

    whatsapp_business_account: Optional[DataWhatsappBusinessAccount] = None


class WhatsappMessageTemplateUpdateResponse(BaseModel):
    data: Optional[Data] = None
