# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrandOptionalAttributes"]


class BrandOptionalAttributes(BaseModel):
    tax_exempt_status: Optional[str] = FieldInfo(alias="taxExemptStatus", default=None)
    """The tax exempt status of the brand"""
