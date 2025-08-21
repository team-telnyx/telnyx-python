# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ActionValidateRegistrationCodesResponse", "Data"]


class Data(BaseModel):
    invalid_detail: Optional[str] = None
    """The validation message"""

    record_type: Optional[str] = None

    registration_code: Optional[str] = None
    """The 10-digit SIM card registration code"""

    valid: Optional[bool] = None
    """The attribute that denotes whether the code is valid or not"""


class ActionValidateRegistrationCodesResponse(BaseModel):
    data: Optional[List[Data]] = None
