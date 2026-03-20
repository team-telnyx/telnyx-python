# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WhatsappTemplateData", "WhatsappBusinessAccount"]


class WhatsappBusinessAccount(BaseModel):
    id: Optional[str] = None


class WhatsappTemplateData(BaseModel):
    id: Optional[str] = None

    category: Optional[Literal["MARKETING", "UTILITY", "AUTHENTICATION"]] = None

    components: Optional[List[Dict[str, object]]] = None
    """
    Template components (header, body, footer, buttons) as submitted, including
    example values.
    """

    created_at: Optional[datetime] = None

    language: Optional[str] = None

    name: Optional[str] = None

    record_type: Optional[str] = None

    rejection_reason: Optional[str] = None

    status: Optional[str] = None
    """Current template status from Meta (e.g.

    PENDING, APPROVED, REJECTED, PAUSED, DISABLED). Additional statuses may be
    returned as Meta evolves the template lifecycle.
    """

    template_id: Optional[str] = None

    updated_at: Optional[datetime] = None

    whatsapp_business_account: Optional[WhatsappBusinessAccount] = None
