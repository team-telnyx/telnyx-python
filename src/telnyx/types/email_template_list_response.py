# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel
from .email_template import EmailTemplate
from .email_inboxes.email_pagination_meta import EmailPaginationMeta

__all__ = ["EmailTemplateListResponse"]


class EmailTemplateListResponse(BaseModel):
    data: List[EmailTemplate]

    meta: EmailPaginationMeta
