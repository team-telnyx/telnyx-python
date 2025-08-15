# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortingOrderEndUserAdminParam"]


class PortingOrderEndUserAdminParam(TypedDict, total=False):
    account_number: str
    """The authorized person's account number with the current service provider"""

    auth_person_name: str
    """Name of person authorizing the porting order"""

    billing_phone_number: str
    """Billing phone number associated with these phone numbers"""

    business_identifier: str
    """European business identification number. Applicable only in the European Union"""

    entity_name: str
    """Person Name or Company name requesting the port"""

    pin_passcode: str
    """
    PIN/passcode possibly required by the old service provider for extra
    verification
    """

    tax_identifier: str
    """European tax identification number. Applicable only in the European Union"""
