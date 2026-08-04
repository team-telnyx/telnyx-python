# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_template import EmailTemplate

__all__ = ["EmailTemplateResponse"]


class EmailTemplateResponse(BaseModel):
    data: EmailTemplate
