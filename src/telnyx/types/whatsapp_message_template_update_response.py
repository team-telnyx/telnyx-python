# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.whatsapp_template_data import WhatsappTemplateData

__all__ = ["WhatsappMessageTemplateUpdateResponse"]


class WhatsappMessageTemplateUpdateResponse(BaseModel):
    data: Optional[WhatsappTemplateData] = None
