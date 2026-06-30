# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..._models import BaseModel

if TYPE_CHECKING:
    from ..shared.whatsapp_template_data import WhatsappTemplateData

__all__ = ["TemplateCreateResponse"]


class TemplateCreateResponse(BaseModel):
    data: Optional[WhatsappTemplateData] = None
