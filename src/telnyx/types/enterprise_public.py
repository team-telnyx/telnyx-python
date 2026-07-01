# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .billing_address import BillingAddress
from .billing_contact import BillingContact
from .physical_address import PhysicalAddress
from .organization_contact import OrganizationContact

__all__ = ["EnterprisePublic"]


class EnterprisePublic(BaseModel):
    id: Optional[str] = None

    billing_address: Optional[BillingAddress] = None

    billing_contact: Optional[BillingContact] = None

    branded_calling_enabled: Optional[bool] = None
    """
    True once Branded Calling has been activated on this enterprise (see
    `POST /enterprises/{id}/branded_calling`).
    """

    corporate_registration_number: Optional[str] = None
    """Optional corporate-registration / company-number identifier."""

    country_code: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_reference: Optional[str] = None

    doing_business_as: Optional[str] = None

    dun_bradstreet_number: Optional[str] = None
    """Optional D-U-N-S Number issued by Dun & Bradstreet."""

    fein: Optional[str] = None

    industry: Optional[str] = None

    jurisdiction_of_incorporation: Optional[str] = None

    legal_name: Optional[str] = None

    number_of_employees: Optional[str] = None

    number_reputation_enabled: Optional[bool] = None
    """
    True once Phone Number Reputation has been enabled on this enterprise (see
    `POST /enterprises/{id}/reputation`).
    """

    organization_contact: Optional[OrganizationContact] = None

    organization_legal_type: Optional[str] = None

    organization_physical_address: Optional[PhysicalAddress] = None

    organization_type: Optional[str] = None

    primary_business_domain_sic_code: Optional[str] = None
    """Optional SIC code for the primary line of business."""

    professional_license_number: Optional[str] = None
    """Optional professional-license number for regulated industries."""

    role_type: Optional[str] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None
