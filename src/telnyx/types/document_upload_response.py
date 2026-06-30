# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .doc_service_document import DocServiceDocument

__all__ = ["DocumentUploadResponse"]


class DocumentUploadResponse(BaseModel):
    data: Optional[DocServiceDocument] = None
