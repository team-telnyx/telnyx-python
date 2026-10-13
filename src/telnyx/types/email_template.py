# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .email_template_common import EmailTemplateCommon

__all__ = ["EmailTemplate"]


class EmailTemplate(EmailTemplateCommon):
    subject: Optional[str] = None
