# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ActionVerifyOwnershipResponse", "Data", "DataFound"]


class DataFound(BaseModel):
    id: Optional[str] = None
    """Identifies the resource."""

    number_val_e164: Optional[str] = None
    """The phone number in E.164 format"""


class Data(BaseModel):
    found: Optional[List[DataFound]] = None
    """The list of phone numbers which you own and are in an editable state"""

    not_found: Optional[List[str]] = None
    """Phone numbers that are not found in the account"""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class ActionVerifyOwnershipResponse(BaseModel):
    data: Optional[Data] = None
