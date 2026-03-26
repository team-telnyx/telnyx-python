# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .billing_address_param import BillingAddressParam
from .billing_contact_param import BillingContactParam
from .physical_address_param import PhysicalAddressParam
from .organization_contact_param import OrganizationContactParam

__all__ = ["EnterpriseUpdateParams"]


class EnterpriseUpdateParams(TypedDict, total=False):
    billing_address: BillingAddressParam

    billing_contact: BillingContactParam

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

    organization_contact: OrganizationContactParam
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not
    'phone_number').
    """

    organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"]
    """Legal structure type"""

    organization_physical_address: PhysicalAddressParam

    primary_business_domain_sic_code: str
    """SIC Code"""

    professional_license_number: str
    """Professional license number"""

    website: str
    """Company website URL"""
