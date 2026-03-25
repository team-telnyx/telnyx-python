# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "EnterpriseUpdateParams",
    "BillingAddress",
    "BillingContact",
    "OrganizationContact",
    "OrganizationPhysicalAddress",
]


class EnterpriseUpdateParams(TypedDict, total=False):
    billing_address: BillingAddress

    billing_contact: BillingContact

    corporate_registration_number: str
    """Corporate registration number"""

    customer_reference: str
    """Customer reference identifier"""

    doing_business_as: str
    """DBA name"""

    dun_bradstreet_number: str
    """D-U-N-S Number"""

    fein: str
    """Federal Employer Identification Number. Format: XX-XXXXXXX or XXXXXXXXX"""

    industry: str
    """Industry classification"""

    legal_name: str
    """Legal name of the enterprise"""

    number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]
    """Employee count range"""

    organization_contact: OrganizationContact
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not
    'phone_number').
    """

    organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"]
    """Legal structure type"""

    organization_physical_address: OrganizationPhysicalAddress

    primary_business_domain_sic_code: str
    """SIC Code"""

    professional_license_number: str
    """Professional license number"""

    website: str
    """Company website URL"""


class BillingAddress(TypedDict, total=False):
    administrative_area: Required[str]
    """State or province"""

    city: Required[str]
    """City name"""

    country: Required[str]
    """Country name (e.g., United States)"""

    postal_code: Required[str]
    """ZIP or postal code"""

    street_address: Required[str]
    """Street address"""

    extended_address: Optional[str]
    """Additional address line (suite, apt, etc.)"""


class BillingContact(TypedDict, total=False):
    email: Required[str]
    """Contact's email address"""

    first_name: Required[str]
    """Contact's first name"""

    last_name: Required[str]
    """Contact's last name"""

    phone_number: Required[str]
    """Contact's phone number (10-15 digits)"""


class OrganizationContact(TypedDict, total=False):
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not 'phone_number').
    """

    email: Required[str]
    """Contact's email address"""

    first_name: Required[str]
    """Contact's first name"""

    job_title: Required[str]
    """Contact's job title (required)"""

    last_name: Required[str]
    """Contact's last name"""

    phone: Required[str]
    """Contact's phone number in E.164 format"""


class OrganizationPhysicalAddress(TypedDict, total=False):
    administrative_area: Required[str]
    """State or province"""

    city: Required[str]
    """City name"""

    country: Required[str]
    """Country name (e.g., United States)"""

    postal_code: Required[str]
    """ZIP or postal code"""

    street_address: Required[str]
    """Street address"""

    extended_address: Optional[str]
    """Additional address line (suite, apt, etc.)"""
