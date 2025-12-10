# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusParams"]


class PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusParams(TypedDict, total=False):
    page: int

    records_per_page: Annotated[int, PropertyInfo(alias="recordsPerPage")]
