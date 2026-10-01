# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .billing_contact_param import BillingContactParam
from .physical_address_param import PhysicalAddressParam
from .organization_contact_param import OrganizationContactParam

__all__ = ["EnterpriseUpdateParams"]


class EnterpriseUpdateParams(TypedDict, total=False):
    billing_address: PhysicalAddressParam

    billing_contact: BillingContactParam

    corporate_registration_number: Optional[str]
    """
    The official number your company received when it was legally registered or
    incorporated (for example from your state or national business registry). It is
    on your certificate of incorporation.
    """

    customer_reference: str
    """Your own label for this account.

    Enter any reference that helps you find it in your records. Telnyx does not use
    it during vetting.
    """

    doing_business_as: str
    """
    The trade name your business operates under if it is different from your legal
    name, also called a Doing Business As (DBA) name. Leave blank if you only use
    your legal name.
    """

    dun_bradstreet_number: Optional[str]
    """
    Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
    identifier for your business. Leave blank if you do not have one.
    """

    fein: str
    """
    US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.
    """

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
    """The industry your business operates in.

    Choose the closest match from the list; if your value is not accepted, pick the
    nearest category.
    """

    jurisdiction_of_incorporation: str
    """
    The state, province, or country where your business was legally incorporated,
    for example Delaware.
    """

    legal_name: str
    """
    Your business's full registered legal name, exactly as it appears on your
    incorporation or tax documents, 3 to 64 characters.
    """

    number_of_employees: str
    """Approximate headcount range.

    Used for vetting heuristics; pick the bucket that contains your current employee
    count.
    """

    organization_contact: OrganizationContactParam

    organization_legal_type: str
    """Legal-entity form. Pick the form that matches your incorporation documents:

    - `corporation` - C-corp or S-corp.
    - `llc` - limited liability company.
    - `partnership` - general/limited partnership.
    - `nonprofit` - non-profit corporation, charitable trust, or
      501(c)(3)/equivalent.
    - `other` - anything else (sole proprietorships, government bodies, DBAs, etc.).
      You may be asked for additional documents during vetting.
    """

    organization_physical_address: PhysicalAddressParam

    primary_business_domain_sic_code: Optional[str]
    """
    The 4-digit Standard Industrial Classification code for your main line of
    business, which tells us what industry you operate in. Look it up in the SIC
    code directory if you are unsure.
    """

    professional_license_number: Optional[str]
    """
    If your business operates under a professional license (for example legal,
    medical, or financial services), enter the license number issued by the
    licensing authority. Leave blank if it does not apply.
    """

    website: str
    """Your business's public website address, including https://.

    Leave blank if your business has no website.
    """
