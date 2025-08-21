# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .doc_service_document import DocServiceDocument

__all__ = ["DocumentRetrieveResponse"]


class DocumentRetrieveResponse(BaseModel):
    data: Optional[DocServiceDocument] = None
