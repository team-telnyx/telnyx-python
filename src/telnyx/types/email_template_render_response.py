# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .email_template_common import EmailTemplateCommon

__all__ = ["EmailTemplateRenderResponse", "Data"]


class Data(EmailTemplateCommon):
    """
    Template object with `subject`, `html_body`, and `text_body` replaced by their Liquid-rendered values. Rendered content is not limited by the stored template-field lengths. All other template fields remain unchanged.
    """

    subject: Optional[str] = None


class EmailTemplateRenderResponse(BaseModel):
    data: Data
    """
    Template object with `subject`, `html_body`, and `text_body` replaced by their
    Liquid-rendered values. Rendered content is not limited by the stored
    template-field lengths. All other template fields remain unchanged.
    """
