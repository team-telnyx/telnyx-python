# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EnterpriseCreateParams"]


class EnterpriseCreateParams(TypedDict, total=False):
    billing_address: Required["PhysicalAddressParam"]

    billing_contact: Required["BillingContactParam"]

    country_code: Required[str]
    """ISO 3166-1 alpha-2 country code. Currently `US` and `CA` are supported."""

    doing_business_as: Required[str]
    """
    The trade name your business operates under if it is different from your legal
    name, also called a Doing Business As (DBA) name. Leave blank if you only use
    your legal name.
    """

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
    """The industry your business operates in.

    Choose the closest match from the list; if your value is not accepted, pick the
    nearest category.
    """

    jurisdiction_of_incorporation: Required[str]
    """
    The state, province, or country where your business was legally incorporated,
    for example Delaware.
    """

    legal_name: Required[str]
    """
    Your business's full registered legal name, exactly as it appears on your
    incorporation or tax documents, 3 to 64 characters.
    """

    number_of_employees: Required[Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]]
    """Approximate headcount range.

    Used for vetting heuristics; pick the bucket that contains your current employee
    count.
    """

    organization_contact: Required["OrganizationContactParam"]

    organization_legal_type: Required[Literal["corporation", "llc", "partnership", "nonprofit", "other"]]
    """Legal-entity form. Pick the form that matches your incorporation documents:

    - `corporation` - C-corp or S-corp.
    - `llc` - limited liability company.
    - `partnership` - general/limited partnership.
    - `nonprofit` - non-profit corporation, charitable trust, or
      501(c)(3)/equivalent.
    - `other` - anything else (sole proprietorships, government bodies, DBAs, etc.).
      You may be asked for additional documents during vetting.
    """

    organization_physical_address: Required["PhysicalAddressParam"]

    organization_type: Required[Literal["commercial", "government", "non_profit"]]
    """Organization category for vetting purposes:

    - `commercial` - for-profit business entities (LLC, corp, partnership, sole
      proprietorship). Most callers fall here.
    - `government` - federal/state/local government bodies.
    - `non_profit` - registered 501(c)(3)/equivalent (incl. educational
      institutions, charities, religious organisations).
    """

    website: Required[str]
    """Your business's public website address, including https://.

    Leave blank if your business has no website.
    """

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

    dun_bradstreet_number: Optional[str]
    """
    Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
    identifier for your business. Leave blank if you do not have one.
    """

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

    role_type: Literal["enterprise", "bpo"]
    """
    `enterprise` for an organization registering its own DIRs (the default, and the
    right choice when the calls display your own brand). `bpo` for a Business
    Process Outsourcer: a call center that places calls on behalf of other
    enterprises and displays their brand. A `bpo` enterprise describes the call
    center itself and cannot own a DIR. Each client the call center calls for gets
    its own `enterprise` in the same account, with the client's DIR under it; that
    DIR is then linked to the `bpo` enterprise through `bpo_authorizations`. Fixed
    at creation.
    """


from .billing_contact_param import BillingContactParam
from .physical_address_param import PhysicalAddressParam
from .organization_contact_param import OrganizationContactParam
