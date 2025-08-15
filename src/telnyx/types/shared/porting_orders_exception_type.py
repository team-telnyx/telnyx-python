# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PortingOrdersExceptionType"]


class PortingOrdersExceptionType(BaseModel):
    code: Optional[
        Literal[
            "ACCOUNT_NUMBER_MISMATCH",
            "AUTH_PERSON_MISMATCH",
            "BTN_ATN_MISMATCH",
            "ENTITY_NAME_MISMATCH",
            "FOC_EXPIRED",
            "FOC_REJECTED",
            "LOCATION_MISMATCH",
            "LSR_PENDING",
            "MAIN_BTN_PORTING",
            "OSP_IRRESPONSIVE",
            "OTHER",
            "PASSCODE_PIN_INVALID",
            "PHONE_NUMBER_HAS_SPECIAL_FEATURE",
            "PHONE_NUMBER_MISMATCH",
            "PHONE_NUMBER_NOT_PORTABLE",
            "PORT_TYPE_INCORRECT",
            "PORTING_ORDER_SPLIT_REQUIRED",
            "POSTAL_CODE_MISMATCH",
            "RATE_CENTER_NOT_PORTABLE",
            "SV_CONFLICT",
            "SV_UNKNOWN_FAILURE",
        ]
    ] = None
    """Identifier of an exception type"""

    description: Optional[str] = None
    """Description of an exception type"""
