# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_template import EmailTemplate

__all__ = ["EmailTemplateRenderResponse", "Data"]


class Data(EmailTemplate):
    """
    Template object with `subject`, `html_body`, and `text_body` replaced by their Liquid-rendered values. All other template fields (id, name, variables, etc.) remain unchanged.
    """

    pass


class EmailTemplateRenderResponse(BaseModel):
    data: Data
    """
    Template object with `subject`, `html_body`, and `text_body` replaced by their
    Liquid-rendered values. All other template fields (id, name, variables, etc.)
    remain unchanged.
    """
