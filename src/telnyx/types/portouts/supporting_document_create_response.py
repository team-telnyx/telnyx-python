# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .port_out_supporting_document import PortOutSupportingDocument

__all__ = ["SupportingDocumentCreateResponse"]


class SupportingDocumentCreateResponse(BaseModel):
    data: Optional[List[PortOutSupportingDocument]] = None
