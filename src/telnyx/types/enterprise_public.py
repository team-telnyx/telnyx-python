# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .billing_address import BillingAddress
from .billing_contact import BillingContact
from .physical_address import PhysicalAddress
from .organization_contact import OrganizationContact

__all__ = ["EnterprisePublic"]


class EnterprisePublic(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the enterprise"""

    billing_address: Optional[BillingAddress] = None

    billing_contact: Optional[BillingContact] = None

    corporate_registration_number: Optional[str] = None
    """Corporate registration number"""

    country_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code"""

    created_at: Optional[datetime] = None
    """When the enterprise was created"""

    customer_reference: Optional[str] = None
    """Customer reference identifier"""

    doing_business_as: Optional[str] = None
    """DBA name"""

    dun_bradstreet_number: Optional[str] = None
    """D-U-N-S Number"""

    fein: Optional[str] = None
    """Federal Employer Identification Number"""

    industry: Optional[str] = None
    """Industry classification"""

    legal_name: Optional[str] = None
    """Legal name of the enterprise"""

    number_of_employees: Optional[Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]] = (
        None
    )
    """Employee count range"""

    organization_contact: Optional[OrganizationContact] = None
    """Organization contact information.

    Note: the response returns this object with the phone field as 'phone' (not
    'phone_number').
    """

    organization_legal_type: Optional[Literal["corporation", "llc", "partnership", "nonprofit", "other"]] = None
    """Legal structure type"""

    organization_physical_address: Optional[PhysicalAddress] = None

    organization_type: Optional[Literal["commercial", "government", "non_profit"]] = None
    """Type of organization"""

    primary_business_domain_sic_code: Optional[str] = None
    """SIC Code"""

    professional_license_number: Optional[str] = None
    """Professional license number"""

    role_type: Optional[Literal["enterprise", "bpo"]] = None
    """Role type in Branded Calling / Number Reputation services"""

    updated_at: Optional[datetime] = None
    """When the enterprise was last updated"""

    website: Optional[str] = None
    """Company website URL"""
