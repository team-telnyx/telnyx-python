# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerServiceRecordVerifyPhoneNumberCoverageResponse", "Data"]


class Data(BaseModel):
    additional_data_required: Optional[
        List[
            Literal[
                "name",
                "authorized_person_name",
                "account_number",
                "customer_code",
                "pin",
                "address_line_1",
                "city",
                "state",
                "zip_code",
                "billing_phone_number",
            ]
        ]
    ] = None
    """Additional data required to perform CSR for the phone number.

    Only returned if `has_csr_coverage` is true.
    """

    has_csr_coverage: Optional[bool] = None
    """Indicates whether the phone number is covered or not."""

    phone_number: Optional[str] = None
    """The phone number that is being verified."""

    reason: Optional[str] = None
    """The reason why the phone number is not covered.

    Only returned if `has_csr_coverage` is false.
    """

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class CustomerServiceRecordVerifyPhoneNumberCoverageResponse(BaseModel):
    data: Optional[List[Data]] = None
