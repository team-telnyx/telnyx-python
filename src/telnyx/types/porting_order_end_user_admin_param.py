# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PortingOrderEndUserAdminParam"]


class PortingOrderEndUserAdminParam(TypedDict, total=False):
    account_number: Optional[str]
    """The authorized person's account number with the current service provider"""

    auth_person_name: Optional[str]
    """Name of person authorizing the porting order"""

    billing_phone_number: Optional[str]
    """Billing phone number associated with these phone numbers"""

    business_identifier: Optional[str]
    """European business identification number. Applicable only in the European Union"""

    entity_name: Optional[str]
    """Person Name or Company name requesting the port"""

    pin_passcode: Optional[str]
    """
    PIN/passcode possibly required by the old service provider for extra
    verification
    """

    tax_identifier: Optional[str]
    """European tax identification number. Applicable only in the European Union"""
