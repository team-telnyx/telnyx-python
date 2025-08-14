# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["IntegrationSecret"]


class IntegrationSecret(BaseModel):
    id: str

    created_at: datetime

    identifier: str

    record_type: str

    updated_at: Optional[datetime] = None
