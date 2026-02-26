# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .profile_assignment_phone_numbers import ProfileAssignmentPhoneNumbers

__all__ = ["PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse"]


class PhoneNumberAssignmentByProfileListPhoneNumberStatusResponse(BaseModel):
    records: List[ProfileAssignmentPhoneNumbers]
