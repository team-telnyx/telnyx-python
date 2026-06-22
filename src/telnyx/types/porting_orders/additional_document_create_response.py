# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .porting_additional_document import PortingAdditionalDocument

__all__ = ["AdditionalDocumentCreateResponse"]


class AdditionalDocumentCreateResponse(BaseModel):
    data: Optional[List[PortingAdditionalDocument]] = None
