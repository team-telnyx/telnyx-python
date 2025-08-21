# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PortingOrderEndUserAdmin"]


class PortingOrderEndUserAdmin(BaseModel):
    account_number: Optional[str] = None
    """The authorized person's account number with the current service provider"""

    auth_person_name: Optional[str] = None
    """Name of person authorizing the porting order"""

    billing_phone_number: Optional[str] = None
    """Billing phone number associated with these phone numbers"""

    business_identifier: Optional[str] = None
    """European business identification number. Applicable only in the European Union"""

    entity_name: Optional[str] = None
    """Person Name or Company name requesting the port"""

    pin_passcode: Optional[str] = None
    """
    PIN/passcode possibly required by the old service provider for extra
    verification
    """

    tax_identifier: Optional[str] = None
    """European tax identification number. Applicable only in the European Union"""
