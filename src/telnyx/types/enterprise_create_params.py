# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "EnterpriseCreateParams",
    "BillingAddress",
    "BillingContact",
    "OrganizationContact",
    "OrganizationPhysicalAddress",
]


class EnterpriseCreateParams(TypedDict, total=False):
    billing_address: Required[BillingAddress]

    billing_contact: Required[BillingContact]

    country_code: Required[str]
    """Country code. Currently only 'US' is accepted."""

    doing_business_as: Required[str]
    """Primary business name / DBA name"""

    fein: Required[str]
    """Federal Employer Identification Number.

    Format: XX-XXXXXXX or 9-digit number (minimum 9 digits).
    """

    industry: Required[str]
    """Industry classification.

    Case-insensitive. Accepted values: accounting, finance, billing, collections,
    business, charity, nonprofit, communications, telecom, customer service,
    support, delivery, shipping, logistics, education, financial, banking,
    government, public, healthcare, health, pharmacy, medical, insurance, legal,
    law, notifications, scheduling, real estate, property, retail, ecommerce, sales,
    marketing, software, technology, tech, media, surveys, market research, travel,
    hospitality, hotel
    """

    legal_name: Required[str]
    """Legal name of the enterprise"""

    number_of_employees: Required[Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]]
    """Employee count range"""

    organization_contact: Required[OrganizationContact]
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not
    'phone_number').
    """

    organization_legal_type: Required[Literal["corporation", "llc", "partnership", "nonprofit", "other"]]
    """Legal structure type"""

    organization_physical_address: Required[OrganizationPhysicalAddress]

    organization_type: Required[Literal["commercial", "government", "non_profit"]]
    """Type of organization"""

    website: Required[str]
    """Enterprise website URL. Accepts any string — no URL format validation enforced."""

    corporate_registration_number: str
    """Corporate registration number (optional)"""

    customer_reference: str
    """Optional customer reference identifier for your own tracking"""

    dun_bradstreet_number: str
    """D-U-N-S Number (optional)"""

    primary_business_domain_sic_code: str
    """SIC Code (optional)"""

    professional_license_number: str
    """Professional license number (optional)"""

    role_type: Literal["enterprise", "bpo"]
    """Role type in Branded Calling / Number Reputation services"""


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
