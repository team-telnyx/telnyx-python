# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse", "Record"]


class Record(BaseModel):
    phone_number: str = FieldInfo(alias="phoneNumber")
    """The phone number that the status is being checked for."""

    status: str
    """The status of the associated phone number assignment."""

    task_id: str = FieldInfo(alias="taskId")
    """The ID of the task associated with the phone number."""


class PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse(BaseModel):
    records: List[Record]
