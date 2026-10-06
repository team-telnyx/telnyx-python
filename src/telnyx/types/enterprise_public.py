# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .billing_contact import BillingContact
from .physical_address import PhysicalAddress
from .organization_contact import OrganizationContact

__all__ = ["EnterprisePublic"]


class EnterprisePublic(BaseModel):
    id: Optional[str] = None

    billing_address: Optional[PhysicalAddress] = None

    billing_contact: Optional[BillingContact] = None

    bpo_verification_rejection_reason: Optional[str] = None
    """
    Reason Telnyx rejected the BPO (Business Process Outsourcer) verification, when
    `bpo_verification_status` is `rejected`; `null` otherwise.
    """

    bpo_verification_status: Optional[Literal["pending", "approved", "rejected"]] = None
    """Whether Telnyx has approved this BPO (Business Process Outsourcer) account.

    Only set for accounts created with `role_type` `bpo`; `null` for normal
    enterprises. A BPO enterprise must be `approved` before a DIR can be linked to
    it through `bpo_authorizations`.
    """

    branded_calling_enabled: Optional[bool] = None
    """
    True once Branded Calling has been activated on this enterprise (see
    `POST /enterprises/{id}/branded_calling`).
    """

    corporate_registration_number: Optional[str] = None
    """
    The official number your company received when it was legally registered or
    incorporated (for example from your state or national business registry). It is
    on your certificate of incorporation.
    """

    country_code: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_reference: Optional[str] = None
    """Your own label for this account.

    Enter any reference that helps you find it in your records. Telnyx does not use
    it during vetting.
    """

    doing_business_as: Optional[str] = None
    """
    The trade name your business operates under if it is different from your legal
    name, also called a Doing Business As (DBA) name. Leave blank if you only use
    your legal name.
    """

    dun_bradstreet_number: Optional[str] = None
    """
    Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
    identifier for your business. Leave blank if you do not have one.
    """

    fein: Optional[str] = None
    """
    US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.
    """

    industry: Optional[str] = None
    """The industry your business operates in.

    Choose the closest match from the list; if your value is not accepted, pick the
    nearest category.
    """

    jurisdiction_of_incorporation: Optional[str] = None
    """
    The state, province, or country where your business was legally incorporated,
    for example Delaware.
    """

    legal_name: Optional[str] = None
    """
    Your business's full registered legal name, exactly as it appears on your
    incorporation or tax documents, 3 to 64 characters.
    """

    number_of_employees: Optional[str] = None
    """Approximate headcount range.

    Used for vetting heuristics; pick the bucket that contains your current employee
    count.
    """

    number_reputation_enabled: Optional[bool] = None
    """
    True once Phone Number Reputation has been enabled on this enterprise (see
    `POST /enterprises/{id}/reputation`).
    """

    organization_contact: Optional[OrganizationContact] = None

    organization_legal_type: Optional[str] = None
    """Legal-entity form. Pick the form that matches your incorporation documents:

    - `corporation` - C-corp or S-corp.
    - `llc` - limited liability company.
    - `partnership` - general/limited partnership.
    - `nonprofit` - non-profit corporation, charitable trust, or
      501(c)(3)/equivalent.
    - `other` - anything else (sole proprietorships, government bodies, DBAs, etc.).
      You may be asked for additional documents during vetting.
    """

    organization_physical_address: Optional[PhysicalAddress] = None

    organization_type: Optional[str] = None

    primary_business_domain_sic_code: Optional[str] = None
    """
    The 4-digit Standard Industrial Classification code for your main line of
    business, which tells us what industry you operate in. Look it up in the SIC
    code directory if you are unsure.
    """

    professional_license_number: Optional[str] = None
    """
    If your business operates under a professional license (for example legal,
    medical, or financial services), enter the license number issued by the
    licensing authority. Leave blank if it does not apply.
    """

    role_type: Optional[Literal["enterprise", "bpo"]] = None

    updated_at: Optional[datetime] = None

    website: Optional[str] = None
    """Your business's public website address, including https://.

    Leave blank if your business has no website.
    """
