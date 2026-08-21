# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .email_block_import import EmailBlockImport

__all__ = ["EmailBlockImportResponse"]


class EmailBlockImportResponse(BaseModel):
    data: EmailBlockImport
    """Import job.

    Schema fields hidden: `account_id`, `csv_content`, `block_ttl_days`. Nullable
    fields use the omit-nullable pattern.
    """
