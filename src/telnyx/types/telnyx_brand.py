# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .entity_type import EntityType
from .stock_exchange import StockExchange
from .alt_business_id_type import AltBusinessIDType
from .brand_identity_status import BrandIdentityStatus

__all__ = ["TelnyxBrand", "OptionalAttributes"]


class OptionalAttributes(BaseModel):
    tax_exempt_status: Optional[str] = FieldInfo(alias="taxExemptStatus", default=None)
    """The tax exempt status of the brand"""


class TelnyxBrand(BaseModel):
    brand_relationship: Literal["BASIC_ACCOUNT", "SMALL_ACCOUNT", "MEDIUM_ACCOUNT", "LARGE_ACCOUNT", "KEY_ACCOUNT"] = (
        FieldInfo(alias="brandRelationship")
    )
    """Brand relationship to the CSP."""

    country: str
    """ISO2 2 characters country code. Example: US - United States"""

    display_name: str = FieldInfo(alias="displayName")
    """Display or marketing name of the brand."""

    email: str
    """Valid email address of brand support contact."""

    entity_type: EntityType = FieldInfo(alias="entityType")
    """Entity type behind the brand. This is the form of business establishment."""

    vertical: str
    """Vertical or industry segment of the brand."""

    alt_business_id: Optional[str] = FieldInfo(alias="altBusinessId", default=None)
    """Alternate business identifier such as DUNS, LEI, or GIIN"""

    alt_business_id_type: Optional[AltBusinessIDType] = FieldInfo(alias="altBusinessIdType", default=None)
    """An enumeration."""

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)
    """Unique identifier assigned to the brand."""

    business_contact_email: Optional[str] = FieldInfo(alias="businessContactEmail", default=None)
    """Business contact email.

    Required if `entityType` is `PUBLIC_PROFIT`.
    """

    city: Optional[str] = None
    """City name"""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """(Required for Non-profit/private/public) Legal company name."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Date and time that the brand was created at."""

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)
    """Unique identifier assigned to the csp by the registry."""

    ein: Optional[str] = None
    """(Required for Non-profit) Government assigned corporate tax ID.

    EIN is 9-digits in U.S.
    """

    failure_reasons: Optional[str] = FieldInfo(alias="failureReasons", default=None)
    """Failure reasons for brand"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """First name of business contact."""

    identity_status: Optional[BrandIdentityStatus] = FieldInfo(alias="identityStatus", default=None)
    """The verification status of an active brand"""

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)
    """IP address of the browser requesting to create brand identity."""

    is_reseller: Optional[bool] = FieldInfo(alias="isReseller", default=None)
    """Indicates whether this brand is known to be a reseller"""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Last name of business contact."""

    mobile_phone: Optional[str] = FieldInfo(alias="mobilePhone", default=None)
    """Valid mobile phone number in e.164 international format."""

    mock: Optional[bool] = None
    """Mock brand for testing purposes"""

    optional_attributes: Optional[OptionalAttributes] = FieldInfo(alias="optionalAttributes", default=None)

    phone: Optional[str] = None
    """Valid phone number in e.164 international format."""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """Postal codes. Use 5 digit zipcode for United States"""

    reference_id: Optional[str] = FieldInfo(alias="referenceId", default=None)
    """Unique identifier Telnyx assigned to the brand - the brandId"""

    state: Optional[str] = None
    """State. Must be 2 letters code for United States."""

    status: Optional[Literal["OK", "REGISTRATION_PENDING", "REGISTRATION_FAILED"]] = None
    """Status of the brand"""

    stock_exchange: Optional[StockExchange] = FieldInfo(alias="stockExchange", default=None)
    """(Required for public company) stock exchange."""

    stock_symbol: Optional[str] = FieldInfo(alias="stockSymbol", default=None)
    """(Required for public company) stock symbol."""

    street: Optional[str] = None
    """Street number and name."""

    tcr_brand_id: Optional[str] = FieldInfo(alias="tcrBrandId", default=None)
    """Unique identifier assigned to the brand by the registry."""

    universal_ein: Optional[str] = FieldInfo(alias="universalEin", default=None)
    """Universal EIN of Brand, Read Only."""

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)
    """Date and time that the brand was last updated at."""

    webhook_failover_url: Optional[str] = FieldInfo(alias="webhookFailoverURL", default=None)
    """Failover webhook to which brand status updates are sent."""

    webhook_url: Optional[str] = FieldInfo(alias="webhookURL", default=None)
    """Webhook to which brand status updates are sent."""

    website: Optional[str] = None
    """Brand website URL."""
