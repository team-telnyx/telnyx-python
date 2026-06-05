# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .billing_address_param import BillingAddressParam
from .billing_contact_param import BillingContactParam
from .physical_address_param import PhysicalAddressParam
from .organization_contact_param import OrganizationContactParam

__all__ = ["EnterpriseUpdateParams"]


class EnterpriseUpdateParams(TypedDict, total=False):
    billing_address: BillingAddressParam

    billing_contact: BillingContactParam

    corporate_registration_number: Optional[str]

    customer_reference: str

    doing_business_as: str

    dun_bradstreet_number: Optional[str]

    fein: str

    industry: Literal[
        "accounting",
        "finance",
        "billing",
        "collections",
        "business",
        "charity",
        "nonprofit",
        "communications",
        "telecom",
        "customer service",
        "support",
        "delivery",
        "shipping",
        "logistics",
        "education",
        "financial",
        "banking",
        "government",
        "public",
        "healthcare",
        "health",
        "pharmacy",
        "medical",
        "insurance",
        "legal",
        "law",
        "notifications",
        "scheduling",
        "real estate",
        "property",
        "retail",
        "ecommerce",
        "sales",
        "marketing",
        "software",
        "technology",
        "tech",
        "media",
        "surveys",
        "market research",
        "travel",
        "hospitality",
        "hotel",
    ]

    jurisdiction_of_incorporation: str
    """Updated state/province/country of incorporation. Optional on update."""

    legal_name: str
    """Legal name of the enterprise."""

    number_of_employees: str

    organization_contact: OrganizationContactParam

    organization_legal_type: str

    organization_physical_address: PhysicalAddressParam

    primary_business_domain_sic_code: Optional[str]

    professional_license_number: Optional[str]

    website: str
