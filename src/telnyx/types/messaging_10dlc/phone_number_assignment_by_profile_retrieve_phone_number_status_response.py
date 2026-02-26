# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .profile_assignment_phone_numbers import ProfileAssignmentPhoneNumbers

__all__ = ["PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse"]


class PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse(BaseModel):
    records: List[ProfileAssignmentPhoneNumbers]
