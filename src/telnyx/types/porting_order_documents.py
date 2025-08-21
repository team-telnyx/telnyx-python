# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PortingOrderDocuments"]


class PortingOrderDocuments(BaseModel):
    invoice: Optional[str] = None
    """Returned ID of the submitted Invoice via the Documents endpoint"""

    loa: Optional[str] = None
    """Returned ID of the submitted LOA via the Documents endpoint"""
