# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .billing_address_param import BillingAddressParam
from .billing_contact_param import BillingContactParam
from .physical_address_param import PhysicalAddressParam
from .organization_contact_param import OrganizationContactParam

__all__ = ["EnterpriseCreateParams"]


class EnterpriseCreateParams(TypedDict, total=False):
    billing_address: Required[BillingAddressParam]

    billing_contact: Required[BillingContactParam]

    country_code: Required[str]
    """ISO 3166-1 alpha-2 country code. Currently `US` and `CA` are supported."""

    doing_business_as: Required[str]

    fein: Required[str]
    """
    US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.
    """

    industry: Required[
        Literal[
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
    ]
    """Industry classification."""

    jurisdiction_of_incorporation: Required[str]

    legal_name: Required[str]
    """Legal name of the enterprise."""

    number_of_employees: Required[Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]]
    """Approximate headcount range.

    Used for vetting heuristics; pick the bucket that contains your current employee
    count.
    """

    organization_contact: Required[OrganizationContactParam]

    organization_legal_type: Required[Literal["corporation", "llc", "partnership", "nonprofit", "other"]]
    """Legal-entity form. Pick the form that matches your incorporation documents:

    - `corporation` — C-corp or S-corp.
    - `llc` — limited liability company.
    - `partnership` — general/limited partnership.
    - `nonprofit` — non-profit corporation, charitable trust, or
      501(c)(3)/equivalent.
    - `other` — anything else (sole proprietorships, government bodies, DBAs, etc.).
      You may be asked for additional documents during vetting.
    """

    organization_physical_address: Required[PhysicalAddressParam]

    organization_type: Required[Literal["commercial", "government", "non_profit"]]
    """Organization category for vetting purposes:

    - `commercial` — for-profit business entities (LLC, corp, partnership, sole
      proprietorship). Most callers fall here.
    - `government` — federal/state/local government bodies.
    - `non_profit` — registered 501(c)(3)/equivalent (incl. educational
      institutions, charities, religious organisations).
    """

    website: Required[str]

    corporate_registration_number: Optional[str]
    """Optional corporate-registration / company-number identifier."""

    customer_reference: str
    """Optional free-form string the caller can attach for their own bookkeeping.

    Telnyx does not interpret it.
    """

    dun_bradstreet_number: Optional[str]
    """Optional D-U-N-S Number."""

    primary_business_domain_sic_code: Optional[str]
    """Optional SIC code for the primary line of business."""

    professional_license_number: Optional[str]
    """Optional professional-license number for regulated industries."""

    role_type: Literal["enterprise", "bpo"]
    """
    `enterprise` for an organization registering its own DIRs; `bpo` for a Business
    Process Outsourcer placing calls on behalf of one or more enterprises.
    """
