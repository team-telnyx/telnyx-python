# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BrandGetFeedbackResponse", "Category"]


class Category(BaseModel):
    id: str
    """One of `TAX_ID`, `STOCK_SYMBOL`, `GOVERNMENT_ENTITY`, `NONPROFIT`, and `OTHERS`"""

    description: str
    """Long-form description of the feedback with additional information"""

    display_name: str = FieldInfo(alias="displayName")
    """Human-readable version of the `id` field"""

    fields: List[str]
    """List of relevant fields in the originally-submitted brand json"""


class BrandGetFeedbackResponse(BaseModel):
    brand_id: str = FieldInfo(alias="brandId")
    """ID of the brand being queried about"""

    category: List[Category]
    """A list of reasons why brand creation/revetting didn't go as planned"""
