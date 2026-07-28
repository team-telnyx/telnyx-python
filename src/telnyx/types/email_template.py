# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailTemplate"]


class EmailTemplate(BaseModel):
    id: str

    created_at: datetime

    html_body: Optional[str] = None

    name: str

    record_type: Literal["email_template"]

    subject: Optional[str] = None

    text_body: Optional[str] = None

    updated_at: datetime

    variables: List[str]
