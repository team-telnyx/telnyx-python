# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_block import EmailBlock

__all__ = ["EmailBlockResponse"]


class EmailBlockResponse(BaseModel):
    data: EmailBlock
    """Suppression record.

    Schema fields hidden by the view: `account_id`, `bounce_category`, `dsn_code`,
    `meta`.
    """
